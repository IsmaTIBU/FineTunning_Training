# FRASES DE USUARIO CASUAL PARA TEST CON LABELS
# 20 frases naturales con sus outputs esperados para evaluación

test_data = [
    {
        "input": "How do I calculate the position of my robot arm?",
        "output": '{"operacion": "", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Can you help me find the angles to reach 50cm, 30cm, 20cm?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "50", "y": "30", "z": "20", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "I need to move my robot to position 0.8, 1.2, 0.5 meters",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "0.8", "y": "1.2", "z": "0.5", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Show me what happens when I set the joints to 45, 90, and 135 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "What's the end position if my robot angles are 30°, 60°, 90°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "30", "q2": "60", "q3": "90", "unidad_angular": "grados"}}'
    },
    {
        "input": "How fast can the robot move with angles 1.2, 0.8, 1.5 rad and speeds 2, 1, 3 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.2", "q2": "0.8", "q3": "1.5", "unidad_angular": "radianes", "q1_dot": "2", "q2_dot": "1", "q3_dot": "3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I want to see a 3D view of my robot at 120°, 240°, 60°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "120", "q2": "240", "q3": "60", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Calculate transformation matrices for 25, 50, 75 degrees please",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "25", "q2": "50", "q3": "75", "unidad_angular": "grados"}}'
    },
    {
        "input": "Can I get the jacobian for angles π/4, π/2, π radians with velocities 1.5, 2.0, 2.5?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "np.pi", "unidad_angular": "radianes", "q1_dot": "1.5", "q2_dot": "2.0", "q3_dot": "2.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Let me try positioning the arm at coordinates (100, 200, 300) mm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "100", "y": "200", "z": "300", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "What if I set angle1=pi/6, angle2=pi/3, angle3=pi/2?",
        "output": '{"operacion": "", "parametros": {"q1": "np.pi/6", "q2": "np.pi/3", "q3": "np.pi/2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Show me a simulation with the robot reaching (1.5, 1.0, 2.0) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1.5", "y": "1.0", "z": "2.0", "unidad_posicion": "m"}}}'
    },
    {
        "input": "What angles do I need to grab something at 25cm, 40cm, 15cm?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "25", "y": "40", "z": "15", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Can you display the robot when all joints are at 180 degrees?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "180", "q2": "180", "q3": "180", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I want to check the forward kinematics for 0.5, 1.0, 1.5 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.5", "q2": "1.0", "q3": "1.5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the jacobian matrix for my current setup: 60°, 120°, 45°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "60", "q2": "120", "q3": "45", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Show me the transformation matrices when q1=90°, q2=45°, q3=0°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "90", "q2": "45", "q3": "0", "unidad_angular": "grados"}}'
    },
    {
        "input": "Help me position the robot gripper at point (0.6, 0.8, 1.2) meters",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "0.6", "y": "0.8", "z": "1.2", "unidad_posicion": "m"}}}'
    },
    {
        "input": "I need to visualize my robot configuration with angles 72°, 144°, 216°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "What's the robot position when the motors are at 2.1, 0.9, 1.7 radians?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.1", "q2": "0.9", "q3": "1.7", "unidad_angular": "radianes"}}'
    }
]

print(f"📊 Frases de usuario casual con labels: {len(test_data)} ejemplos")
