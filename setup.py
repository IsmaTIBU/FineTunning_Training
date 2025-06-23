# =============================================================================
# SETUP: DIVIDIR Y GUARDAR DATASET EN ARCHIVOS SEPARADOS
# =============================================================================

import json
import random
import os
import sys

# Setup
sys.path.append('/content/PRUEBA')

# Cargar datos originales
from DATA import cinematica_directa_train, cinematica_inversa_train, jacobiano_train, matrices_train, simulacion_train

all_data = cinematica_directa_train + cinematica_inversa_train + jacobiano_train + matrices_train + simulacion_train
print(f"📊 Total de ejemplos: {len(all_data)}")

# Mezclar datos aleatoriamente para división justa
random.seed(42)  # Para reproducibilidad
random.shuffle(all_data)

# Calcular tamaños de división: 70% train, 15% val, 15% test
total_size = len(all_data)
train_size = int(0.70 * total_size)
val_size = int(0.15 * total_size)
test_size = total_size - train_size - val_size

print(f"📈 División de datos:")
print(f"   • Train: {train_size} ejemplos (70%)")
print(f"   • Validation: {val_size} ejemplos (15%)")
print(f"   • Test: {test_size} ejemplos (15%)")

# Dividir datos
train_data = all_data[:train_size]
val_data = all_data[train_size:train_size + val_size]
test_data = all_data[train_size + val_size:]

# Verificar divisiones
print(f"\n✅ Verificación:")
print(f"   • Train: {len(train_data)} ejemplos")
print(f"   • Val: {len(val_data)} ejemplos")
print(f"   • Test: {len(test_data)} ejemplos")
print(f"   • Total: {len(train_data) + len(val_data) + len(test_data)}")

# Función para crear archivos .py
def create_python_file(data, filename, variable_name):
    """Crea un archivo .py con los datos"""
    
    content = f'''# {filename.upper()} DATASET
# Generado automáticamente - División 70/15/15

{variable_name} = [
'''
    
    for item in data:
        input_str = repr(item['input'])
        output_str = repr(item['output'])
        
        content += f'''    {{
        "input": {input_str},
        "output": {output_str}
    }},
'''
    
    content += f''']

# Estadísticas del {filename}
print(f"📊 {filename.capitalize()} dataset: {{len({variable_name})}} ejemplos")
'''
    
    return content

# Crear archivos
print(f"\n📁 Creando archivos en /content/PRUEBA/DATA/...")

# train.py
train_content = create_python_file(train_data, "train", "train_data")
with open('/content/PRUEBA/DATA/train.py', 'w', encoding='utf-8') as f:
    f.write(train_content)

# val.py
val_content = create_python_file(val_data, "validation", "val_data")
with open('/content/PRUEBA/DATA/val.py', 'w', encoding='utf-8') as f:
    f.write(val_content)

# test.py
test_content = create_python_file(test_data, "test", "test_data")
with open('/content/PRUEBA/DATA/test.py', 'w', encoding='utf-8') as f:
    f.write(test_content)

print("✅ Archivos creados:")
print("   • /content/PRUEBA/DATA/train.py")
print("   • /content/PRUEBA/DATA/val.py") 
print("   • /content/PRUEBA/DATA/test.py")

# Actualizar __init__.py para incluir los nuevos archivos
init_content = '''from .C_Directa import cinematica_directa_train
from .C_Inversa import cinematica_inversa_train
from .jacobiano import jacobiano_train
from .matrices_Transf import matrices_train
from .simulacion import simulacion_train 

# Archivos de división de datos (70/15/15)
from .train import train_data
from .val import val_data
from .test import test_data

__all__ = [
    'C_Directa', 'C_Inversa', 'jacobiano', 'matrices_Transf', 'simulacion',
    'train_data', 'val_data', 'test_data'
]
'''

with open('/content/PRUEBA/DATA/__init__.py', 'w', encoding='utf-8') as f:
    f.write(init_content)

print("✅ __init__.py actualizado")

# Verificar que los archivos funcionan
print(f"\n🧪 Verificando archivos creados...")

try:
    # Importar para verificar
    from DATA.train import train_data as test_train
    from DATA.val import val_data as test_val
    from DATA.test import test_data as test_test
    
    print(f"✅ train.py: {len(test_train)} ejemplos cargados")
    print(f"✅ val.py: {len(test_val)} ejemplos cargados")
    print(f"✅ test.py: {len(test_test)} ejemplos cargados")
    
    # Mostrar ejemplo de cada conjunto
    print(f"\n📋 Ejemplos de cada conjunto:")
    print(f"TRAIN: {test_train[0]['input'][:50]}...")
    print(f"VAL: {test_val[0]['input'][:50]}...")
    print(f"TEST: {test_test[0]['input'][:50]}...")
    
except Exception as e:
    print(f"❌ Error verificando archivos: {e}")

print(f"\n🎉 ¡DIVISIÓN COMPLETADA!")
print(f"Ahora puedes usar:")
print(f"   from DATA.train import train_data")
print(f"   from DATA.val import val_data")
print(f"   from DATA.test import test_data")
print(f"\n🚀 Listo para la siguiente celda de entrenamiento!")