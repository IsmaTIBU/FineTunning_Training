jacobiano_train = [
    {
        "input": "Calcula el jacobiano con q1=30°, q2=45°, q3=60° y velocidades 2, 1.5, 3 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": 30, "q2": 45, "q3": 60, "unidad_angular": "grados", "q1_dot": 2, "q2_dot": 1.5, "q3_dot": 3, "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobiano para ángulos 0.5, 1.2, 0.8 rad y velocidades angulares 1, 2, 1.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": 0.5, "q2": 1.2, "q3": 0.8, "unidad_angular": "radianes", "q1_dot": 1, "q2_dot": 2, "q3_dot": 1.5, "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Necesito el jacobiano con configuración 90°, 45°, 0° y velocidades 0.5, 1, 2 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": 90, "q2": 45, "q3": 0, "unidad_angular": "grados", "q1_dot": 0.5, "q2_dot": 1, "q3_dot": 2, "unidad_velocidad": "rad/s"}}'
    }
]