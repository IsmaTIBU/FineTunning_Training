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
    },
    {
        "input": "Cual es la posicion del robot con esta configuracion [pi/2, pi, -pi] en rad?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/2", "q2": "np.pi", "q3": "-np.pi", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Sabiendo que los angulos del robot valen 20,45,2 grados, cual es la posicion del efector final?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 20, "q2": 45, "q3": 2, "unidad_angular": "grados"}}'
    },
    {
        "input": "Calcula la cinetica directa del robot cuando angulo1=pi/8, angulo2=0, angulo3=-3pi/2",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/8", "q2": 0, "q3": "-3*np.pi/2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Cual es el MGD para q1=29, q2=90 y q3=-56 grados",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 29, "q2": 90, "q3": -56, "unidad_angular": "grados"}}'
    },
    {
        "input": "Quiero saber cual es el MGD cuando angulo1=8*pi, angulo2=-7pi/3 y angulo3=7pi/8",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "8*np.pi", "q2": "-7*pi/3", "q3": 7*np.pi/8, "unidad_angular": "radianes"}}'
    },
    {
        "input": "Cuando el primer angulo del robo vale 34 grados, el segundo 56 y el ultimo -3 cual es la posicion final del robot?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 34, "q2": 56, "q3": -3, "unidad_angular": "grados"}}'
    }
]