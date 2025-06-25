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
    },
    # Correccion 1
    {
        "input": "Compute DH parameters and T matrices for joint configuration [15°, 75°, 165°]",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "15", "q2": "75", "q3": "165", "unidad_angular": "grados"}}'
    },
    {
        "input": "Execute inverse geometric model to achieve TCP coordinates at x=1.2m, y=0.8m, z=2.1m",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "1.2", "y": "0.8", "z": "2.1", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Generate velocity analysis using angular rates of first=2.3, second=1.7, third=3.1 rad/sec",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.3", "q2_dot": "1.7", "q3_dot": "3.1", "unidad_velocidad": "rad/s"}}'
    },
    
    # Frases muy casuales/naturales
    {
        "input": "My robot's at some weird position and I need help figuring out where it's pointing",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Hey, can you tell me how to get my arm to that spot over there at 15, 25, 35 centimeters?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "15", "y": "25", "z": "35", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Wondering what my robotic buddy looks like when I twist the joints to ninety, forty-five, and zero degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "90", "q2": "45", "q3": "0", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Estructuras originales con diferentes formas de especificar valores
    {
        "input": "Set q₁ to π/3, q₂ to 2π/3, and q₃ to π, then show me the forward kinematics",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/3", "q2": "2*np.pi/3", "q3": "np.pi", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Target coordinates: X→800mm, Y→1200mm, Z→400mm. What joint angles are required?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "800", "y": "1200", "z": "400", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Joint velocities are streaming at [0.8|2.4|1.6] radians per second, need jacobian analysis",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.8", "q2_dot": "2.4", "q3_dot": "1.6", "unidad_velocidad": "rad/s"}}'
    },
    
    # Casos sin valores específicos
    {
        "input": "Run a complete kinematic analysis on my current robot state",
        "output": '{"operacion": "", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "I need help with robot workspace calculations",
        "output": '{"operacion": "", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Show me everything about my manipulator's current pose",
        "output": '{"operacion": "", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    
    # Frases con múltiples operaciones implícitas
    {
        "input": "Calculate where my robot ends up with motors at 3π/4, π/8, 5π/6 rads",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3*np.pi/4", "q2": "np.pi/8", "q3": "5*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "I want to see my robot in 3D when it reaches coordinates (0.75, 1.25, 1.75) meters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "0.75", "y": "1.25", "z": "1.75", "unidad_posicion": "m"}}}'
    },
    {
        "input": "How do I configure my arm to pick up an object at point 450mm×300mm×150mm?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "450", "y": "300", "z": "150", "unidad_posicion": "mm"}}}'
    },
    
    # Frases con terminología mixta
    {
        "input": "Motor one at 35 degrees, motor two at seventy grados, motor three at 105°",
        "output": '{"operacion": "", "parametros": {"q1": "35", "q2": "70", "q3": "105", "unidad_angular": "grados"}}'
    },
    {
        "input": "Check the speed analysis when axis rotations are first=1.4 rad/s, second=2.8 rad/s, third=0.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.4", "q2_dot": "2.8", "q3_dot": "0.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Visualize my manipulator when theta angles equal π÷6, π÷4, and π÷2 respectively",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/6", "q2": "np.pi/4", "q3": "np.pi/2", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Estructuras conversacionales
    {
        "input": "So I've got this robot, right? And I need to move it to coordinates like... 2.3, 1.8, 0.9 meters",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "2.3", "y": "1.8", "z": "0.9", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Quick question: what transformation matrices do I get with angles being 66°, 132°, 198°?",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "66", "q2": "132", "q3": "198", "unidad_angular": "grados"}}'
    },
    {
        "input": "Urgent! Need to know where my robot arm points when joints are at 1.8, 0.6, 2.4 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.8", "q2": "0.6", "q3": "2.4", "unidad_angular": "radianes"}}'
    },
    
    # Frases con notaciones no estándar
    {
        "input": "Joint angles: first→120°, second→240°, third→360°, calculate direct kinematics please",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "120", "q2": "240", "q3": "360", "unidad_angular": "grados"}}'
    },
    {
        "input": "Run jacobian with configuration (1.1 rad, 2.2 rad, 3.3 rad) and velocities (0.5, 1.0, 1.5) rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.1", "q2": "2.2", "q3": "3.3", "unidad_angular": "radianes", "q1_dot": "0.5", "q2_dot": "1.0", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show 3D model: joints @ 48deg, 96deg, 144deg",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "48", "q2": "96", "q3": "144", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases técnicas avanzadas
    {
        "input": "Perform forward geometric transformation for angular displacement vector [5π/8, 3π/8, 7π/8]",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "5*np.pi/8", "q2": "3*np.pi/8", "q3": "7*np.pi/8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Determine optimal joint configuration for end-effector positioning at coordinates 33cm×67cm×101cm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "33", "y": "67", "z": "101", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Execute differential kinematics analysis with q̇₁=3.2, q̇₂=1.9, q̇₃=2.6 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "3.2", "q2_dot": "1.9", "q3_dot": "2.6", "unidad_velocidad": "rad/s"}}'
    },
    
    # Frases de troubleshooting
    {
        "input": "My robot is acting weird, can you analyze the current position?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Something's wrong with my arm movement, need a full kinematic check",
        "output": '{"operacion": "", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Debug mode: show me what happens at joint config 0.3, 1.7, 2.9 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.3", "q2": "1.7", "q3": "2.9", "unidad_angular": "radianes"}}'
    },
    
    # Casos edge con valores extremos
    {
        "input": "Test extreme configuration: -180°, 540°, -90°",
        "output": '{"operacion": "", "parametros": {"q1": "-180", "q2": "540", "q3": "-90", "unidad_angular": "grados"}}'
    }
]

print(f"📊 Frases de usuario casual con labels: {len(test_data)} ejemplos")
