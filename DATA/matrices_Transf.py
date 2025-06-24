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
    },
    {
        "input": "Cuando angulo1=20 grad, angulo2=-67grad y angulo3=0 grad, cual seria el calculo de la matriz de transofrmacion del robot?",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": 20, "q2": -67, "q3": 0, "unidad_angular": "grados"}}'
    },
    {
        "input": "Calcula las matrices de transformacion del robot cuando q1=pi/2, q2=pi y q3=-pi/3 ",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "np.pi/2", "q2": "np.pi", "q3": "-np.pi/3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Cuales serian las matrices de transformacion cuando q1=3pi/2, q2=5pi y q3=-8pi/3 ",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "3*np.pi/2", "q2": "5*np.pi", "q3": "-8*np.pi/3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Necesito las matrices de transformacion para los angulos siguientes en grados: -25, 89, 6 ",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": -25, "q2": 89, "q3": 6, "unidad_angular": "grados"}}'
    },
    {
        "input": "Quiero conocer las matrices T para estos angulos [pi/3, 6pi/4, -3pi/5] ",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "np.pi/3", "q2": "6*np.pi/4", "q3": "-3*np.pi/5", "unidad_angular": "radianes"}}'
    }
]