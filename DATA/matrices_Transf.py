matrices_train = [
    {
        "input": "Calcula las matrices de transformación para q1=30°, q2=45°, q3=60°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": 30, "q2": 45, "q3": 60, "unidad_angular": "grados"}}'
    },
    {
        "input": "Necesito las matrices T con ángulos 0.5, 1.2, 0.8 radianes",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": 0.5, "q2": 1.2, "q3": 0.8, "unidad_angular": "radianes"}}'
    },
    {
        "input": "Obtén T01, T12, T23 y T03 con q1=90°, q2=0°, q3=45°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": 90, "q2": 0, "q3": 45, "unidad_angular": "grados"}}'
    },
    {
        "input": "Matrices de transformación homogénea para configuración 1.57, 0, 0.785 rad",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": 1.57, "q2": 0, "q3": 0.785, "unidad_angular": "radianes"}}'
    },
    {
        "input": "Quiero las matrices T para theta1=45°, theta2=30°, theta3=60°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": 45, "q2": 30, "q3": 60, "unidad_angular": "grados"}}'
    }
]