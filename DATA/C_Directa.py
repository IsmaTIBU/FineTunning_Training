cinematica_directa_train = [
    {
        "input": "Cinemática directa con q1=1.57 rad, q2=0.785 rad, q3=0 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 1.57, "q2": 0.785, "q3": 0, "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calcula la posición del efector final con ángulos 30°, 45°, 60°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 30, "q2": 45, "q3": 60, "unidad_angular": "grados"}}'
    },
    {
        "input": "Directa con configuración 90°, 0°, 45°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 90, "q2": 0, "q3": 45, "unidad_angular": "grados"}}'
    },
    {
        "input": "Posición del end effector para theta1=0.5, theta2=1.2, theta3=0.8 radianes",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 0.5, "q2": 1.2, "q3": 0.8, "unidad_angular": "radianes"}}'
    }
]