# =============================================================================
# DIVIDIR Y GUARDAR DATASET EN ARCHIVOS SEPARADOS
# =============================================================================

import json
import random
import os
import sys

# Setup
sys.path.append('/content/PRUEBA')

# Cargar datos
from DATA import cinematica_directa_train, cinematica_inversa_train, jacobiano_train, matrices_train, simulacion_train

def main():
    all_data = cinematica_directa_train + cinematica_inversa_train + jacobiano_train + matrices_train + simulacion_train
    print(f"📊 Total de ejemplos: {len(all_data)}")

    # Mezclar datos aleatoriamente para división justa
    random.seed(42)  # Para reproducibilidad
    random.shuffle(all_data)

    # Calcular tamaños de división
    total_size = len(all_data)
    train_size = int(0.70 * total_size)
    val_size = int(0.15 * total_size)
    test_size = total_size - train_size - val_size  # El resto

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

    # Crear archivos .py para cada división
    def create_python_file(data, filename, variable_name):
        """Crea un archivo .py con los datos"""
        
        content = f'''# {filename.upper()} DATASET
    # Generado automáticamente

    {variable_name} = [
    '''
        
        for item in data:
            # Formatear cada entrada como diccionario Python
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

    # Train
    train_content = create_python_file(train_data, "train", "train_data")
    with open('/content/PRUEBA/DATA/train.py', 'w', encoding='utf-8') as f:
        f.write(train_content)

    # Validation
    val_content = create_python_file(val_data, "validation", "val_data")
    with open('/content/PRUEBA/DATA/val.py', 'w', encoding='utf-8') as f:
        f.write(val_content)

    # Test
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

    # Archivos de división de datos
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
        sys.path.append('/content/PRUEBA')
        from DATA.train import train_data
        from DATA.val import val_data  
        from DATA.test import test_data
        
        print(f"✅ train.py: {len(train_data)} ejemplos cargados")
        print(f"✅ val.py: {len(val_data)} ejemplos cargados")
        print(f"✅ test.py: {len(test_data)} ejemplos cargados")
        
        # Mostrar ejemplo de cada conjunto
        print(f"\n📋 Ejemplos de cada conjunto:")
        print(f"TRAIN: {train_data[0]['input'][:50]}...")
        print(f"VAL: {val_data[0]['input'][:50]}...")
        print(f"TEST: {test_data[0]['input'][:50]}...")
        
    except Exception as e:
        print(f"❌ Error verificando archivos: {e}")

    print(f"\n🎉 ¡DIVISIÓN COMPLETADA!")
    print(f"Ahora puedes usar:")
    print(f"   from DATA.train import train_data")
    print(f"   from DATA.val import val_data")
    print(f"   from DATA.test import test_data")

if __name__=="__main__":
    main()