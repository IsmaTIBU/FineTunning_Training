cinematica_inversa_train = [
    {
        "input": "Cinemática inversa para alcanzar el punto (15, 20, 25) cm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 15, "y": 20, "z": 25, "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Calcula los ángulos necesarios para llegar a posición (100, 150, 200) mm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 100, "y": 150, "z": 200, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Cinematica inversa para coordenadas (0.3, 0.4, 0.5) metros",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 0.3, "y": 0.4, "z": 0.5, "unidad_posicion": "m"}}}'
    },
    {
        "input": "Necesito los ángulos para que el efector final esté en (80, 120, 160) mm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 80, "y": 120, "z": 160, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Qué configuracion necesita el robot para alcalzar el punto x=0.3, y=0.5 y z=1.2 m?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 0.3, "y": 0.5, "z": 1.2, "unidad_posicion": "m"}}}'
    },
    {
        "input": "Si quiero que el robot llegue a (123, 56, -675)mm qué angulos necesita?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 123, "y": 56, "z": -675, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Quiero que el efector final del fobot se encuentre en estas coordenadas: 345, -123, 9 en milimetros",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 345, "y": -123, "z": 9, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Sabiendo que x=-0.6, y=2.3 y z=-0.23m, cual es la configuracion angular del robot?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": -0.6, "y": 2.3, "z": -0.23, "unidad_posicion": "m"}}}'
    },
    {
        "input": "Calcula la cinematica inversa para alcanzar 67mm, 786mm y -34mm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 67, "y": 786, "z": -34, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Cual seria la configuracion del robot para llegar a las coordenadas siguientes en metros: 0.9, 1.9, -0.6",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": 0.9, "y": 1.9, "z": -0.6, "unidad_posicion": "m"}}}'
    }
]