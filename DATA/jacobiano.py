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
    },
    {
        "input": "Me gustaria saber cual es el jacobiano cuando el primer angulo vale 23 grados, el segundo vale 43 y el ultimo 3 y cuando sus velocidades de articlacion son 2 rad/s, 3 y 6.7",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": 23, "q2": 43, "q3": 3, "unidad_angular": "grados", "q1_dot": 2, "q2_dot": 3, "q3_dot": 6.7, "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobiano cuando la velocidad angular es -1rad/s, 2.2 rad/s, 1.5 rad/s y los angulos son 3, -45, 23 grados",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": 3, "q2": -45, "q3": 23, "unidad_angular": "grados", "q1_dot": 1, "q2_dot": 2.2, "q3_dot": 1.5, "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Cual es el jacobiano cuando q1=30°, q2=45°, q3=60° y las velocidades 2, 1.5, 3 radianes por segundo",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": 30, "q2": 45, "q3": 60, "unidad_angular": "grados", "q1_dot": 2, "q2_dot": 1.5, "q3_dot": 3, "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Quiero el jacobiano cuando angulo1=90°, angulo2=45°, angulo3=0° y velocidades -0.5, 1, -2 radianes por segundo",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": 90, "q2": 45, "q3": 0, "unidad_angular": "grados", "q1_dot": 0.5, "q2_dot": 1, "q3_dot": 2, "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Muestrame el Jacobiano para ángulos -pi/3, pi/2, -8pi/3 y las velocidades 0.8, 2, 0.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "-np.pi/3", "q2": "np.pi/2", "q3": "-8*np.pi/3", "unidad_angular": "radianes", "q1_dot": 0.8, "q2_dot": 2, "q3_dot": 0.5, "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobiano con -pi/3, pi/2, -8pi/3 y 0.8, 2, 0.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "-np.pi/3", "q2": "np.pi/2", "q3": "-8*np.pi/3", "unidad_angular": "radianes", "q1_dot": 0.8, "q2_dot": 2, "q3_dot": 0.5, "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calcula el Jacobiano con -3pi/2, -pi/2 y -8pi/3 y 0.2, 2 y -0.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "-3np.pi/2", "q2": "-np.pi/2", "q3": "-8*np.pi/3", "unidad_angular": "radianes", "q1_dot": 0.2, "q2_dot": 2, "q3_dot": -0.5, "unidad_velocidad": "rad/s"}}'
    }
]