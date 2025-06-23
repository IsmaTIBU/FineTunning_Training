# =============================================================================
# FINE-TUNING CODET5 PARA EXTRACCIÓN DE PARÁMETROS EN ROBÓTICA
# Configuración inicial en Google Colab Pro
# =============================================================================

# Primero verificamos el tipo de GPU disponible
!nvidia-smi

print("=== VERIFICACIÓN DEL ENTORNO ===")
import torch
print(f"CUDA disponible: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memoria GPU: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

# =============================================================================
# INSTALACIÓN DE DEPENDENCIAS
# =============================================================================

print("\n=== INSTALANDO DEPENDENCIAS ===")
!pip install transformers==4.36.0
!pip install datasets==2.14.0
!pip install torch==2.1.0
!pip install accelerate==0.24.0
!pip install evaluate==0.4.0
!pip install tensorboard==2.14.0

# Opcional: para visualización y debugging
!pip install matplotlib seaborn pandas numpy

# =============================================================================
# IMPORTS NECESARIOS
# =============================================================================

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any
import re
import random
from datetime import datetime
from DATA import cinematica_directa_train, cinematica_inversa_train, jacobiano_train, matrices_train, simulacion_train

# Transformers y entrenamiento
from transformers import (
    AutoTokenizer, 
    AutoModelForSeq2SeqLM,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq,
    EarlyStoppingCallback
)
from datasets import Dataset, DatasetDict
import torch
from torch.utils.data import DataLoader

# Para evaluación
from evaluate import load
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# CONFIGURACIÓN DEL MODELO
# =============================================================================

# Usaremos CodeT5+ small que es más potente que base pero manejable en Colab Pro
MODEL_NAME = "Salesforce/codet5p-220m"  # 220M parámetros - buen balance
# Alternativas si quieres más potencia:
# "Salesforce/codet5p-770m"  # 770M parámetros - más potente pero más lento
# "Salesforce/codet5-base"   # Original CodeT5 base

print(f"\n=== CARGANDO MODELO: {MODEL_NAME} ===")

# Cargar tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Cargar modelo
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,  # Usar half precision para ahorrar memoria
    device_map="auto"
)

print(f"Modelo cargado exitosamente!")
print(f"Parámetros del modelo: {model.num_parameters():,}")

# =============================================================================
# CREAR DATASET PEQUEÑO PARA ROBÓTICA
# =============================================================================

def create_robotics_dataset():
    """
    Crea un dataset pequeño de 50 ejemplos para probar el concepto
    """
    
    dataset = []
    
    
    # Combinar todos los ejemplos
    all_examples = (cinematica_directa_train + cinematica_inversa_train + 
                    jacobiano_train + matrices_train + simulacion_train)
    
    return all_examples

# Crear el dataset
print("\n=== CREANDO DATASET DE ROBÓTICA ===")
robotics_data = create_robotics_dataset()
print(f"Dataset creado con {len(robotics_data)} ejemplos")

# Mostrar algunos ejemplos
print("\n=== EJEMPLOS DEL DATASET ===")
for i, example in enumerate(robotics_data[:3]):
    print(f"\nEjemplo {i+1}:")
    print(f"INPUT: {example['input']}")
    print(f"OUTPUT: {example['output']}")

# =============================================================================
# PREPARAR DATOS PARA ENTRENAMIENTO
# =============================================================================

def preprocess_function(examples):
    """
    Preprocesa los datos para el formato que espera CodeT5
    """
    inputs = examples['input']
    targets = examples['output']
    
    # Tokenizar inputs
    model_inputs = tokenizer(
        inputs, 
        max_length=256, 
        truncation=True, 
        padding=True
    )
    
    # Tokenizar targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            targets, 
            max_length=256, 
            truncation=True, 
            padding=True
        )
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Dividir datos: 70% train, 15% val, 15% test
print("\n=== DIVIDIENDO DATASET ===")
random.shuffle(robotics_data)

n_total = len(robotics_data)
n_train = int(0.7 * n_total)
n_val = int(0.15 * n_total)

train_data = robotics_data[:n_train]
val_data = robotics_data[n_train:n_train + n_val]
test_data = robotics_data[n_train + n_val:]

print(f"Train: {len(train_data)} ejemplos")
print(f"Validation: {len(val_data)} ejemplos") 
print(f"Test: {len(test_data)} ejemplos")

# Crear datasets de HuggingFace
train_dataset = Dataset.from_list(train_data)
val_dataset = Dataset.from_list(val_data)
test_dataset = Dataset.from_list(test_data)

# Aplicar preprocesamiento
train_dataset = train_dataset.map(preprocess_function, batched=True)
val_dataset = val_dataset.map(preprocess_function, batched=True)
test_dataset = test_dataset.map(preprocess_function, batched=True)

print("Datasets preprocesados exitosamente!")

# =============================================================================
# DATA COLLATOR
# =============================================================================

data_collator = DataCollatorForSeq2Seq(
    tokenizer=tokenizer,
    model=model,
    padding=True
)

print("\n=== CONFIGURACIÓN COMPLETA ===")
print("✅ Modelo cargado")
print("✅ Dataset creado y preprocesado") 
print("✅ Data collator configurado")
print("✅ Listo para configurar entrenamiento!")

# =============================================================================
# FUNCIÓN DE PRUEBA RÁPIDA
# =============================================================================

def test_model_before_training():
    """
    Prueba rápida del modelo antes del entrenamiento
    """
    print("\n=== PRUEBA PRE-ENTRENAMIENTO ===")
    
    test_input = "Calcula las matrices de transformación para q1=30°, q2=45°, q3=60°"
    
    # Tokenizar
    inputs = tokenizer(test_input, return_tensors="pt", max_length=256, truncation=True)
    
    # Mover a GPU si está disponible
    if torch.cuda.is_available():
        inputs = {k: v.cuda() for k, v in inputs.items()}
        model.cuda()
    
    # Generar
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=256,
            num_beams=3,
            temperature=0.7,
            do_sample=True
        )
    
    # Decodificar
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    print(f"INPUT: {test_input}")
    print(f"OUTPUT (pre-training): {result}")
    print("(Probablemente será incoherente antes del fine-tuning)")

# Ejecutar prueba
test_model_before_training()