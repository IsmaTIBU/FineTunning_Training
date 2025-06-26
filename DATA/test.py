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
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show me everything about my manipulator's current pose",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
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
    
    # Estructuras conversacionales
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
        "input": "My robot is acting weird, can you analyze the current position?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases de troubleshooting
    {
        "input": "Something's wrong with my arm movement, need a full kinematic check",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show me what happens at joint config 0.3, 1.7, 2.9 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "0.3", "q2": "1.7", "q3": "2.9", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    # Cinemática Directa - 12 frases
    {
        "input": "Calculate robot position with motor angles 66°, 132°, 198°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "66", "q2": "132", "q3": "198", "unidad_angular": "grados"}}'
    },
    {
        "input": "What's the end effector location when joints are at 2.3, 1.7, 0.4 radians?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.3", "q2": "1.7", "q3": "0.4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward kinematics with configuration 12°, 48°, 96°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "12", "q2": "48", "q3": "96", "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct geometric model when angle1=7π/8, angle2=π/4, angle3=3π/2",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "7*np.pi/8", "q2": "np.pi/4", "q3": "3*np.pi/2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Where does the robot end up with angles 93°, 186°, 279°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "93", "q2": "186", "q3": "279", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate the end effector position with motors at 1.9, 0.3, 2.6 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.9", "q2": "0.3", "q3": "2.6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward geometric model for servo positions 21°, 84°, 147°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "21", "q2": "84", "q3": "147", "unidad_angular": "grados"}}'
    },
    {
        "input": "What is the robot position when θ1=5π/9, θ2=8π/9, θ3=2π/9?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "5*np.pi/9", "q2": "8*np.pi/9", "q3": "2*np.pi/9", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics calculation for angles 39°, 117°, 234°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "39", "q2": "117", "q3": "234", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate forward kinematics for configuration 0.7, 2.1, 1.4 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.7", "q2": "2.1", "q3": "1.4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Find the robot position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Show me the forward kinematics",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },

    # Cinemática Inversa - 12 frases
    {
        "input": "Calculate inverse kinematics to reach point (675, 1350, 2025) mm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "675", "y": "1350", "z": "2025", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "What angles do I need to position the robot at (1.4, 2.8, 0.7) meters?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "1.4", "y": "2.8", "z": "0.7", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Inverse geometric model for coordinates 87cm, 174cm, 261cm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "87", "y": "174", "z": "261", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Find joint angles to reach target position (560, 840, 1120) millimeters",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "560", "y": "840", "z": "1120", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "What configuration reaches coordinates x=3.1m, y=4.2m, z=1.8m?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "3.1", "y": "4.2", "z": "1.8", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Calculate angles for effector at 29cm, 58cm, 87cm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "29", "y": "58", "z": "87", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Inverse kinematics when end effector must reach (789, 1578, 2367) mm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "789", "y": "1578", "z": "2367", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "What robot configuration to reach point (0.9, 1.8, 3.6) meters?",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "0.9", "y": "1.8", "z": "3.6", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Position the robot at coordinates 44cm, 88cm, 176cm",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "44", "y": "88", "z": "176", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Inverse kinematics for target at coordinates (315, 630, 945) millimeters",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "315", "y": "630", "z": "945", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Calculate inverse kinematics for the target position",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I need angles to reach the desired location",
        "output": '{"operacion": "cinematica_inversa", "parametros": {"posicion_objetivo": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },

    # Jacobiano - 10 frases
    {
        "input": "Calculate jacobian with angles 57°, 114°, 171° and velocities 1.7, 3.4, 2.1 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "57", "q2": "114", "q3": "171", "unidad_angular": "grados", "q1_dot": "1.7", "q2_dot": "3.4", "q3_dot": "2.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian matrix for θ1=3π/7, θ2=6π/7, θ3=π/7 with velocities 2.8, 1.5, 3.9 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "3*np.pi/7", "q2": "6*np.pi/7", "q3": "np.pi/7", "unidad_angular": "radianes", "q1_dot": "2.8", "q2_dot": "1.5", "q3_dot": "3.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the robot speed at 78°, 156°, 234° with angular speeds 0.9, 2.7, 1.4 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "78", "q2": "156", "q3": "234", "unidad_angular": "grados", "q1_dot": "0.9", "q2_dot": "2.7", "q3_dot": "1.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian when configuration is 1.8, 0.9, 2.7 rad and velocities 3.2, 1.6, 2.4 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.8", "q2": "0.9", "q3": "2.7", "unidad_angular": "radianes", "q1_dot": "3.2", "q2_dot": "1.6", "q3_dot": "2.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate robot jacobian for angles 33°, 99°, 297° with speeds 2.5, 0.8, 3.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "33", "q2": "99", "q3": "297", "unidad_angular": "grados", "q1_dot": "2.5", "q2_dot": "0.8", "q3_dot": "3.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How fast moves the robot with π/11, 6π/11, 10π/11 and velocities 1.3, 2.9, 0.7 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/11", "q2": "6*np.pi/11", "q3": "10*np.pi/11", "unidad_angular": "radianes", "q1_dot": "1.3", "q2_dot": "2.9", "q3_dot": "0.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian calculation with velocities 4.1, 0.5, 2.8 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "4.1", "q2_dot": "0.5", "q3_dot": "2.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian for angles 69°, 138°, 207°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "69", "q2": "138", "q3": "207", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "What's the jacobian matrix?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "I need the robot's velocity analysis",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },

    # Matrices de Transformación - 8 frases
    {
        "input": "Calculate transformation matrices for 87°, 174°, 261°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "87", "q2": "174", "q3": "261", "unidad_angular": "grados"}}'
    },
    {
        "input": "T matrices for configuration 4π/7, 2π/7, 6π/7 radians",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "4*np.pi/7", "q2": "2*np.pi/7", "q3": "6*np.pi/7", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Homogeneous transformation for θ1=69°, θ2=138°, θ3=276°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "69", "q2": "138", "q3": "276", "unidad_angular": "grados"}}'
    },
    {
        "input": "I need T01, T12, T23 matrices for angles 2.4, 1.7, 0.9 rad",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "2.4", "q2": "1.7", "q3": "0.9", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate DH matrices for 24°, 72°, 216°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "24", "q2": "72", "q3": "216", "unidad_angular": "grados"}}'
    },
    {
        "input": "Transformation matrices for π/13, 7π/13, 12π/13",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "np.pi/13", "q2": "7*np.pi/13", "q3": "12*np.pi/13", "unidad_angular": "radianes"}}'
    },
    {
        "input": "I need the transformation matrices",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Calculate the T matrices for this configuration",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },

    # Simulación 3D - 8 frases
    {
        "input": "Simulate robot with angles 54°, 162°, 324°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "54", "q2": "162", "q3": "324", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D visualization when effector reaches (750, 1500, 2250) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "750", "y": "1500", "z": "2250", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Show robot in 3D with configuration 3π/11, 8π/11, 5π/11 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "3*np.pi/11", "q2": "8*np.pi/11", "q3": "5*np.pi/11", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the arm at position (37, 74, 111) centimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "37", "y": "74", "z": "111", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "3D simulation for 93°, 279°, 186°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "93", "q2": "279", "q3": "186", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Render robot when positioned at (2.9, 1.6, 4.3) meters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "2.9", "y": "1.6", "z": "4.3", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Show me the simulation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I want to see the 3D model",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    }
]

print(f"📊 Frases de usuario casual con labels: {len(test_data)} ejemplos")
