#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fine-tuning CodeT5 para Robótica - VERSIÓN ARREGLADA
Archivo: training.py
Uso: %run training.py
"""

# =============================================================================
# ARREGLO DE DEPENDENCIAS PRIMERO
# =============================================================================

import os
import sys

print("🔧 Arreglando dependencias...")

# Instalar todo de golpe con versiones específicas
os.system("pip install torch==2.0.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 --quiet")
os.system("pip install transformers==4.21.0 datasets==2.3.2 tokenizers==0.12.1 --quiet")

print("✅ Dependencias instaladas")

# =============================================================================
# CONFIGURACIÓN INICIAL
# =============================================================================

from pathlib import Path

# Configurar paths
REPO_PATH = '/content/PRUEBA'
if REPO_PATH not in sys.path:
    sys.path.append(REPO_PATH)

# Verificar estructura
if not os.path.exists(os.path.join(REPO_PATH, 'DATA')):
    print(f"❌ Error: No se encuentra la carpeta DATA en {REPO_PATH}")
    sys.exit(1)

print(f"✅ Directorio configurado: {REPO_PATH}")

# =============================================================================
# IMPORTS (DESPUÉS DE ARREGLAR DEPENDENCIAS)
# =============================================================================

import torch
import json
import random
import numpy as np
from datetime import datetime

# Ahora importar transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AdamW
from torch.utils.data import Dataset, DataLoader

print("✅ Todas las librerías importadas correctamente")

# =============================================================================
# CARGAR DATOS
# =============================================================================

try:
    from DATA.train import train_data
    from DATA.val import val_data
    from DATA.test import test_data
    
    print(f"📊 Datos cargados:")
    print(f"   • Train: {len(train_data)} ejemplos")
    print(f"   • Validation: {len(val_data)} ejemplos")
    print(f"   • Test: {len(test_data)} ejemplos")
    
except ImportError as e:
    print(f"❌ Error cargando datos: {e}")
    print("Ejecuta primero el script de división de datos")
    sys.exit(1)

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

CONFIG = {
    'model_name': 'Salesforce/codet5-base',
    'batch_size': 2,  # Conservador para evitar problemas
    'learning_rate': 3e-5,
    'epochs': 3,     # Pocas épocas para prueba rápida
    'max_length': 128,  # Más corto para velocidad
    'save_path': './models/',
    'device': 'cuda' if torch.cuda.is_available() else 'cpu'
}

print(f"\\n⚙️ Configuración:")
for key, value in CONFIG.items():
    print(f"   • {key}: {value}")

os.makedirs(CONFIG['save_path'], exist_ok=True)

# =============================================================================
# VERIFICAR GPU
# =============================================================================

if torch.cuda.is_available():
    print(f"\\n🔧 GPU:")
    print(f"   • {torch.cuda.get_device_name(0)}")
    print(f"   • {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    # Limpiar memoria GPU
    torch.cuda.empty_cache()
else:
    print("⚠️ Sin GPU")

# =============================================================================
# DATASET
# =============================================================================

class RoboticsDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=128):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        item = self.data[idx]
        
        # Tokenizar más simple
        input_text = str(item['input'])
        target_text = str(item['output'])
        
        input_ids = self.tokenizer.encode(
            input_text, 
            max_length=self.max_length, 
            truncation=True, 
            padding='max_length'
        )
        
        target_ids = self.tokenizer.encode(
            target_text, 
            max_length=self.max_length, 
            truncation=True, 
            padding='max_length'
        )
        
        return {
            'input_ids': torch.tensor(input_ids, dtype=torch.long),
            'labels': torch.tensor(target_ids, dtype=torch.long)
        }

# =============================================================================
# CARGAR MODELO
# =============================================================================

print(f"\\n🤖 Cargando {CONFIG['model_name']}...")

try:
    tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
    model = AutoModelForSeq2SeqLM.from_pretrained(CONFIG['model_name'])
    model = model.to(CONFIG['device'])
    
    print(f"✅ Modelo cargado")
    print(f"✅ Parámetros: {model.num_parameters():,}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    # Modelo fallback más simple
    print("Intentando T5 como fallback...")
    from transformers import T5Tokenizer, T5ForConditionalGeneration
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    model = model.to(CONFIG['device'])
    print("✅ T5-small cargado como fallback")

# =============================================================================
# DATASETS
# =============================================================================

print("\\n📊 Creando datasets...")

train_dataset = RoboticsDataset(train_data, tokenizer, CONFIG['max_length'])
val_dataset = RoboticsDataset(val_data, tokenizer, CONFIG['max_length'])

train_loader = DataLoader(train_dataset, batch_size=CONFIG['batch_size'], shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=CONFIG['batch_size'], shuffle=False)

optimizer = AdamW(model.parameters(), lr=CONFIG['learning_rate'])

print("✅ Todo preparado")

# =============================================================================
# ENTRENAMIENTO SIMPLIFICADO
# =============================================================================

def train_simple():
    print("\\n🎯 ENTRENAMIENTO INICIADO")
    print("=" * 50)
    
    model.train()
    
    for epoch in range(CONFIG['epochs']):
        print(f"\\nÉpoca {epoch + 1}/{CONFIG['epochs']}")
        
        total_loss = 0
        for batch_idx, batch in enumerate(train_loader):
            
            input_ids = batch['input_ids'].to(CONFIG['device'])
            labels = batch['labels'].to(CONFIG['device'])
            
            # Forward
            outputs = model(input_ids=input_ids, labels=labels)
            loss = outputs.loss
            
            # Backward
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            
            print(f"  Batch {batch_idx + 1}: Loss = {loss.item():.4f}")
        
        avg_loss = total_loss / len(train_loader)
        print(f"📊 Época {epoch + 1} - Loss promedio: {avg_loss:.4f}")
    
    # Guardar modelo
    model_path = os.path.join(CONFIG['save_path'], 'robotics_model_simple.pth')
    torch.save(model.state_dict(), model_path)
    print(f"\\n💾 Modelo guardado: {model_path}")
    
    return model

# =============================================================================
# TEST RÁPIDO
# =============================================================================

def test_model():
    print("\\n🧪 PRUEBA RÁPIDA")
    
    model.eval()
    test_input = "Calcula matrices de transformación para q1=30°, q2=45°, q3=60°"
    
    inputs = tokenizer.encode(test_input, return_tensors="pt", max_length=CONFIG['max_length'], truncation=True)
    inputs = inputs.to(CONFIG['device'])
    
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=CONFIG['max_length'], num_beams=2)
    
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    print(f"INPUT: {test_input}")
    print(f"OUTPUT: {result}")
    
    return result

# =============================================================================
# MAIN
# =============================================================================

def main():
    print("\\n🚀 INICIANDO PROCESO COMPLETO")
    
    # Entrenar
    trained_model = train_simple()
    
    # Probar
    result = test_model()
    
    print("\\n🎉 ¡COMPLETADO!")
    print("Variables disponibles:")
    print("- model: Modelo entrenado")
    print("- tokenizer: Tokenizer")
    print("- CONFIG: Configuración")
    
    return trained_model, result

# =============================================================================
# EJECUCIÓN
# =============================================================================

if __name__ == "__main__":
    trained_model, test_result = main()