# =============================================================================
# CONFIGURACIÓN DE ENTRENAMIENTO OPTIMIZADA PARA A100
# =============================================================================

import os
from datetime import datetime
import json

# =============================================================================
# CONFIGURACIÓN DE ENTRENAMIENTO AGRESIVA PARA A100
# =============================================================================

def setup_training_arguments():
    """
    Configura argumentos de entrenamiento optimizados para GPU A100
    """
    
    # Crear directorio para checkpoints
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"./codet5_robotics_finetuned_{timestamp}"
    
    training_args = TrainingArguments(
        # Directorios
        output_dir=output_dir,
        logging_dir=f"{output_dir}/logs",
        
        # Configuración agresiva para A100 (40GB VRAM)
        per_device_train_batch_size=16,      # Batch grande aprovechando A100
        per_device_eval_batch_size=32,       # Eval batch aún más grande
        gradient_accumulation_steps=2,        # Total effective batch = 32
        
        # Learning rate optimizado para fine-tuning
        learning_rate=3e-5,                  # Agresivo pero seguro
        weight_decay=0.01,                   # Regularización
        adam_epsilon=1e-8,
        warmup_steps=100,                    # Warmup steps
        
        # Épocas y evaluación
        num_train_epochs=5,                  # Suficiente para aprender
        eval_strategy="steps",               # Evaluar cada X steps
        eval_steps=50,                       # Evaluación frecuente
        save_strategy="steps",
        save_steps=50,                       # Guardar checkpoints frecuentemente
        
        # Early stopping y mejores modelos
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        save_total_limit=3,                  # Solo 3 checkpoints máximo
        
        # Logging y monitoreo
        logging_steps=10,                    # Log cada 10 steps
        report_to="tensorboard",             # TensorBoard logging
        
        # Optimizaciones de memoria y velocidad para A100
        fp16=True,                           # Mixed precision training
        dataloader_pin_memory=True,          # Optimización de memoria
        dataloader_num_workers=4,            # Paralelización
        remove_unused_columns=False,         # Mantener columnas
        
        # Configuración de gradientes
        max_grad_norm=1.0,                   # Gradient clipping
        
        # Reproducibilidad
        seed=42,
        data_seed=42,
        
        # Configuración adicional
        predict_with_generate=True,          # Para evaluación con generación
    )
    
    return training_args, output_dir

# Configurar argumentos
print("\n=== CONFIGURANDO ENTRENAMIENTO PARA A100 ===")
training_args, output_dir = setup_training_arguments()
print(f"Directorio de salida: {output_dir}")
print(f"Batch size efectivo: {training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps}")

# =============================================================================
# MÉTRICAS DE EVALUACIÓN PERSONALIZADAS
# =============================================================================

def compute_metrics(eval_preds):
    """
    Métricas personalizadas para evaluar la extracción de parámetros
    """
    predictions, labels = eval_preds
    
    # Decodificar predicciones y labels
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    
    # Reemplazar -100 en labels (tokens ignorados)
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    
    # Métricas personalizadas
    exact_matches = 0
    json_valid = 0
    operation_correct = 0
    
    for pred, label in zip(decoded_preds, decoded_labels):
        # Exact match
        if pred.strip() == label.strip():
            exact_matches += 1
            
        # JSON válido
        try:
            pred_json = json.loads(pred)
            json_valid += 1
            
            # Operación correcta
            try:
                label_json = json.loads(label)
                if pred_json.get('operacion') == label_json.get('operacion'):
                    operation_correct += 1
            except:
                pass
        except:
            pass
    
    total = len(decoded_preds)
    
    return {
        'exact_match': exact_matches / total,
        'json_valid_rate': json_valid / total,
        'operation_accuracy': operation_correct / total,
    }

# =============================================================================
# CONFIGURAR TRAINER
# =============================================================================

# Callback para early stopping
early_stopping = EarlyStoppingCallback(
    early_stopping_patience=3,
    early_stopping_threshold=0.001
)

# Crear trainer
print("\n=== CONFIGURANDO TRAINER ===")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
    callbacks=[early_stopping]
)

print("✅ Trainer configurado exitosamente!")

# =============================================================================
# FUNCIÓN DE ENTRENAMIENTO CON MONITOREO
# =============================================================================

def start_training():
    """
    Inicia el entrenamiento con monitoreo completo
    """
    print("\n" + "="*50)
    print("🚀 INICIANDO FINE-TUNING")
    print("="*50)
    
    print(f"📊 Estadísticas del entrenamiento:")
    print(f"   • Modelo: {MODEL_NAME}")
    print(f"   • GPU: {torch.cuda.get_device_name(0)}")
    print(f"   • Datos entrenamiento: {len(train_dataset)}")
    print(f"   • Datos validación: {len(val_dataset)}")
    print(f"   • Batch size efectivo: {training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps}")
    print(f"   • Learning rate: {training_args.learning_rate}")
    print(f"   • Épocas: {training_args.num_train_epochs}")
    
    # Limpiar memoria GPU antes de empezar
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    
    # Iniciar entrenamiento
    print(f"\n⏰ Iniciando entrenamiento a las {datetime.now().strftime('%H:%M:%S')}")
    print("💡 Tip: Puedes monitorear el progreso en tiempo real con TensorBoard")
    print(f"   Comando: %tensorboard --logdir {output_dir}/logs")
    
    try:
        # ¡ENTRENAR!
        trainer.train()
        
        print("\n🎉 ¡ENTRENAMIENTO COMPLETADO!")
        
        # Guardar modelo final
        trainer.save_model()
        tokenizer.save_pretrained(output_dir)
        
        print(f"💾 Modelo guardado en: {output_dir}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error durante el entrenamiento: {e}")
        return False

# =============================================================================
# FUNCIÓN DE EVALUACIÓN POST-ENTRENAMIENTO
# =============================================================================

def evaluate_final_model():
    """
    Evaluación completa del modelo entrenado
    """
    print("\n" + "="*50)
    print("📊 EVALUACIÓN FINAL")
    print("="*50)
    
    # Evaluar en test set
    test_results = trainer.evaluate(test_dataset)
    
    print("📈 Métricas en test set:")
    for metric, value in test_results.items():
        if isinstance(value, float):
            print(f"   • {metric}: {value:.4f}")
    
    # Pruebas cualitativas
    print("\n🧪 Pruebas cualitativas:")
    
    test_cases = [
        "Calcula las matrices de transformación para q1=30°, q2=45°, q3=60°",
        "Jacobiano con ángulos 0.5, 1.2, 0.8 rad y velocidades 2, 1.5, 3 rad/s",
        "Cinemática inversa para posición (100, 150, 200) mm",
        "Simula robot con q1=90°, q2=45°, q3=30°",
        "Cinemática directa para q1=1.57, q2=0.785, q3=0 radianes"
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n--- Prueba {i} ---")
        print(f"INPUT: {test_case}")
        
        # Tokenizar y generar
        inputs = tokenizer(test_case, return_tensors="pt", max_length=256, truncation=True)
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=256,
                num_beams=5,  # Beam search más agresivo
                temperature=0.1,  # Más determinístico
                do_sample=False
            )
        
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"OUTPUT: {result}")
        
        # Validar JSON
        try:
            parsed = json.loads(result)
            print("✅ JSON válido")
            print(f"   Operación: {parsed.get('operacion', 'N/A')}")
        except:
            print("❌ JSON inválido")

print("\n=== CONFIGURACIÓN LISTA ===")
print("🎯 Para iniciar el entrenamiento, ejecuta: start_training()")
print("📊 Para evaluar después: evaluate_final_model()")
print("📺 Para TensorBoard: %tensorboard --logdir ./codet5_robotics_finetuned_*/logs")