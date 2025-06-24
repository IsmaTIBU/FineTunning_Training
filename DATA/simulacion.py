simulacion_train = [
    {
        "input": "Simula el robot con configuración 90, 45, 30 grad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 90, "q2": 45, "q3": 30, "unidad_angular": "grados", "posicion_efector": {"x": , "y": , "z": , "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualización 3D con ángulos 1.57, 0.785, 0 rad ",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 1.57, "q2": 0.785, "q3": 0, "unidad_angular": "radianes", "posicion_efector": {"x": , "y": , "z": , "unidad_posicion": ""}}}'
    },
    {
        "input": "Simular brazo robótico con posición final en (15, 20, 25) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": , "q2": , "q3": , "unidad_angular": "", "posicion_efector": {"x": 15, "y": 20, "z": 25, "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Simulacion del brazo con configuracion siguiente (15, 20, 25) grados",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 15, "q2": 20, "q3": 25, "unidad_angular": "grados", "posicion_efector": {"x": , "y": , "z": , "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualizacion 3D del efector final x=1223, y=899mm y z=-987 mm ",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": , "q2": , "q3": , "unidad_angular": "", "posicion_efector": {"x": 1223, "y": 899, "z": -987, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Simulame el robot con la configuracion siguiente: (pi/34, -6pi, 12pi/3)",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/34", "q2": "-6*np.pi", "q3": "12*np.pi/3", "unidad_angular": "radianes", "posicion_efector": {"x": , "y": , "z": , "unidad_posicion": ""}}}'
    },
    {
        "input": "Quiero una simulacion del robot cuando su efector final llega a estas coordenadas (1432, 1644, 896) en milimetros",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": , "q2": , "q3": , "unidad_angular": "", "posicion_efector": {"x": 1432, "y": 1644, "z": 896, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Quisiera una simulacion del brazo robótico con posición final en (1500, 2100, 205) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": , "q2": , "q3": , "unidad_angular": "", "posicion_efector": {"x": 1500, "y": 2100, "z": 205, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Muestrame una representacion 3D del efector final x=1023, y=-399 y z=-987 mm ",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": , "q2": , "q3": , "unidad_angular": "", "posicion_efector": {"x": 1023, "y": -399, "z": -987, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Muestra el brazo con la configuracion siguiente (15, 20, 25) en grados",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 15, "q2": 20, "q3": 25, "unidad_angular": "", "posicion_efector": {"x": , "y": , "z": , "unidad_posicion": ""}}}'
    }
]