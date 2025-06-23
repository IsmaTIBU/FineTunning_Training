# =============================================================================
# ENTRENAMIENTO CON DATOS DIVIDIDOS - VERSIÓN COMPLETA
# =============================================================================

import sys
import os
import json
from datetime import datetime

# Setup path
sys.path.append('/content/PRUEBA')

# Importar transformers (CORREGIDO)
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW  # ← De torch, no de transformers
import torch

# Cargar datos divididos (creados en setup.py)
from DATA.train import train_data
from DATA.val import val_data
from DATA.test import test_data

print(f"📊 Datos divididos cargados:")
print(f"   • Train: {len(train_data)} ejemplos")
print(f"   • Val: {len(val_data)} ejemplos")
print(f"   • Test: {len(test_data)} ejemplos")

# CONFIGURACIÓN PARA A100 (ESTO FALTABA)
CONFIG = {
    'model_name': 'Salesforce/codet5-base',
    'batch_size': 4,        # Conservador para dataset pequeño
    'learning_rate': 1e-4,
    'epochs': 10,
    'max_length': 256,
    'device': 'cuda'
}

print(f"\n⚙️ Configuración:")
for key, value in CONFIG.items():
    print(f"   • {key}: {value}")

# Cargar modelo
print(f"\n🤖 Cargando {CONFIG['model_name']}...")
tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
model = AutoModelForSeq2SeqLM.from_pretrained(CONFIG['model_name'])
model = model.to(CONFIG['device'])

print(f"✅ Modelo cargado en GPU")
print(f"✅ Parámetros: {model.num_parameters():,}")

# Dataset clase
class RoboticsDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=256):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        item = self.data[idx]
        
        # Tokenizar input
        input_encoding = self.tokenizer(
            item['input'],
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        
        # Tokenizar target
        target_encoding = self.tokenizer(
            item['output'],
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        
        return {
            'input_ids': input_encoding['input_ids'].flatten(),
            'attention_mask': input_encoding['attention_mask'].flatten(),
            'labels': target_encoding['input_ids'].flatten()
        }

# Crear datasets
train_dataset = RoboticsDataset(train_data, tokenizer, CONFIG['max_length'])
val_dataset = RoboticsDataset(val_data, tokenizer, CONFIG['max_length'])
test_dataset = RoboticsDataset(test_data, tokenizer, CONFIG['max_length'])

# Crear dataloaders
train_loader = DataLoader(train_dataset, batch_size=CONFIG['batch_size'], shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=CONFIG['batch_size'], shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=CONFIG['batch_size'], shuffle=False)

# Optimizador
optimizer = AdamW(model.parameters(), lr=CONFIG['learning_rate'])

print("✅ Datasets y optimizador configurados")

print("🚀 INICIANDO FINE-TUNING EN A100")
print("=" * 60)

# Crear directorio para modelos
os.makedirs('./models', exist_ok=True)

# Función de entrenamiento
def train_epoch(model, dataloader, optimizer, device):
    model.train()
    total_loss = 0
    
    for batch_idx, batch in enumerate(dataloader):
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        
        # Forward pass
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )
        
        loss = outputs.loss
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        
        print(f"   Batch {batch_idx+1}/{len(dataloader)}, Loss: {loss.item():.4f}")
    
    return total_loss / len(dataloader)

# Función de validación
def validate(model, dataloader, device):
    model.eval()
    total_loss = 0
    
    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)
            
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels
            )
            
            total_loss += outputs.loss.item()
    
    return total_loss / len(dataloader)

# ENTRENAMIENTO PRINCIPAL
best_val_loss = float('inf')
training_history = []

for epoch in range(CONFIG['epochs']):
    print(f"\n📈 ÉPOCA {epoch + 1}/{CONFIG['epochs']}")
    print("-" * 40)
    
    # Entrenar
    train_loss = train_epoch(model, train_loader, optimizer, CONFIG['device'])
    
    # Validar
    val_loss = validate(model, val_loader, CONFIG['device'])
    
    # Guardar mejor modelo
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        torch.save(model.state_dict(), './models/best_robotics_model.pth')
        print(f"   💾 Mejor modelo guardado (val_loss: {val_loss:.4f})")
    
    # Log
    print(f"   📊 Train Loss: {train_loss:.4f}")
    print(f"   📊 Val Loss: {val_loss:.4f}")
    
    training_history.append({
        'epoch': epoch + 1,
        'train_loss': train_loss,
        'val_loss': val_loss
    })

# Evaluación final
print(f"\n🧪 EVALUACIÓN EN TEST SET")
test_loss = validate(model, test_loader, CONFIG['device'])
print(f"📊 Test Loss: {test_loss:.4f}")

# Pruebas cualitativas
print(f"\n🔍 PRUEBAS CUALITATIVAS")
model.eval()

test_examples = [item['input'] for item in test_data]

perfect=0
bad=0
total=0
for i, test_input in enumerate(test_examples):
    print(f"\n--- Prueba {i+1} ---")
    print(f"INPUT: {test_input}")
    
    inputs = tokenizer(test_input, return_tensors="pt", max_length=CONFIG['max_length'], truncation=True)
    inputs = {k: v.to(CONFIG['device']) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=CONFIG['max_length'],
            num_beams=5,
            temperature=0.1,
            do_sample=False
        )
    
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"OUTPUT: {result}")
    
    # Validar JSON
    try:
        parsed = json.loads(result)
        print(f"✅ JSON válido - Operación: {parsed.get('operacion', 'N/A')}")
    except:
        print(f"❌ JSON inválido")

    expected_output = test_data[i]['output']  # Output esperado
    print(f"ESPERADO: {expected_output}")
    print(f"OBTENIDO: {result}")

    # Comparación exacta
    if result.strip() == expected_output.strip():
      print("✅ PREDICCIÓN PERFECTA")
      perfect=perfect+1
    else:
      print("❌ DIFERENCIAS ENCONTRADAS")
      bad=bad+1
    total=total+1
print(f"\n📊Performance del modelo\nCasos perfectos: {perfect/total}, ({(perfect/total)*100}%)\nCasos malos: {bad/total}, ({(bad/total)*100}%)")

# Guardar modelo final
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
torch.save(model.state_dict(), f'./models/robotics_codet5_final_{timestamp}.pth')

print(f"\n🎉 ¡FINE-TUNING COMPLETADO!")
print(f"💾 Modelos guardados en ./models/")

# Mostrar resumen
print(f"\n📊 RESUMEN:")
for h in training_history:
    print(f"   Época {h['epoch']}: Train={h['train_loss']:.4f}, Val={h['val_loss']:.4f}")
    
print(f"\n🚀 Modelo entrenado y listo para usar!")