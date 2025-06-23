simulacion_train = [
    {
        "input": "Simula el robot con configuración 90°, 45°, 30° y efector en posición (100, 50, 200) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 90, "q2": 45, "q3": 30, "unidad_angular": "grados", "posicion_efector": {"x": 100, "y": 50, "z": 200, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Visualización 3D con ángulos 1.57, 0.785, 0 rad y efector en (0.5, 0.3, 0.8) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 1.57, "q2": 0.785, "q3": 0, "unidad_angular": "radianes", "posicion_efector": {"x": 0.5, "y": 0.3, "z": 0.8, "unidad_posicion": "m"}}}'
    },
    {
        "input": "Simular brazo robótico con q1=45°, q2=60°, q3=30° y posición final (15, 20, 25) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 45, "q2": 60, "q3": 30, "unidad_angular": "grados", "posicion_efector": {"x": 15, "y": 20, "z": 25, "unidad_posicion": "cm"}}}'
    }
]