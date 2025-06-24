cinematica_directa_train = [
    {
        "input": "Direct kinematics with q1=1.57 rad, q2=0.785 rad, q3=0 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 1.57, "q2": 0.785, "q3": 0, "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the end effector position with angles 30°, 45°, 60°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 30, "q2": 45, "q3": 60, "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward kinematics with configuration 90°, 0°, 45°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 90, "q2": 0, "q3": 45, "unidad_angular": "grados"}}'
    },
    {
        "input": "End effector position for theta1=0.5, theta2=1.2, theta3=0.8 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 0.5, "q2": 1.2, "q3": 0.8, "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the robot position with this configuration [pi/2, pi, -pi] in rad?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/2", "q2": "np.pi", "q3": "-np.pi", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Knowing that the robot angles are 20,45,2 deg, what is the end effector position?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 20, "q2": 45, "q3": 2, "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate the forward kinematics when angle1=pi/8, angle2=0, angle3=-3pi/2",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/8", "q2": 0, "q3": "-3*np.pi/2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the forward geometric model for q1=29, q2=90 and q3=-56 degrees",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 29, "q2": 90, "q3": -56, "unidad_angular": "grados"}}'
    },
    {
        "input": "I want to know the forward geometric model when angle1=8*pi, angle2=-7pi/3 and angle3=7pi/8",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "8*np.pi", "q2": "-7*pi/3", "q3": "7*np.pi/8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "When the first robot angle is 34 degrees, the second 56 and the last -3 what is the final robot position?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 34, "q2": 56, "q3": -3, "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward geometric model of the robot for theta1=π/4, theta2=π/3, theta3=π/6",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/4", "q2": "np.pi/3", "q3": "np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Final position when q1=45°, q2=30°, q3=90°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 45, "q2": 30, "q3": 90, "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct kinematics for configuration [2π, π/2, -π/4] radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2*np.pi", "q2": "np.pi/2", "q3": "-np.pi/4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Where will the end effector be if angle1=120 grad, angle2=60 grad, angle3=180 grad?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 120, "q2": 60, "q3": 180, "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate end effector position with 3π/4, -π/8, 5π/6",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3*np.pi/4", "q2": "-np.pi/8", "q3": "5*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics: first angle 15°, second angle 75°, third angle -45°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 15, "q2": 75, "q3": -45, "unidad_angular": "grados"}}'
    },
    {
        "input": "Robot position when θ1=π, θ2=π/3, θ3=2π/3 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi", "q2": "np.pi/3", "q3": "2*np.pi/3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the direct kinematics of the arm for angles 72°, 36°, 144°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 72, "q2": 36, "q3": 144, "unidad_angular": "grados"}}'
    },
    {
        "input": "With q1=-π/2, q2=3π/2, q3=-2π what is the final robot position?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "-np.pi/2", "q2": "3*np.pi/2", "q3": "-2*np.pi", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward geometric model for 270 degrees, 180 degrees and 0 degrees",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 270, "q2": 180, "q3": 0, "unidad_angular": "grados"}}'
    },
    {
        "input": "What is the cartesian position when angles are π/12, 7π/12, -π/12",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/12", "q2": "7*np.pi/12", "q3": "-np.pi/12", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics calculation: q1=33°, q2=66°, q3=99°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 33, "q2": 66, "q3": 99, "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward geometric model for angular configuration [4π/3, π/6, 5π/4] in radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "4*np.pi/3", "q2": "np.pi/6", "q3": "5*np.pi/4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "End effector final position with theta1=150 grad, theta2=210 grad, theta3=330 grad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 150, "q2": 210, "q3": 330, "unidad_angular": "grados"}}'
    },
    {
        "input": "Where does the robot end up if angle1=π/10, angle2=9π/10, angle3=π/5?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/10", "q2": "9*np.pi/10", "q3": "np.pi/5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics for joint1=12°, joint2=24°, joint3=48°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 12, "q2": 24, "q3": 48, "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct kinematics of the robotic arm with 7π/6, -π/3, 11π/6 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "7*np.pi/6", "q2": "-np.pi/3", "q3": "11*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the final position for 225°, 315°, 135°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 225, "q2": 315, "q3": 135, "unidad_angular": "grados"}}'
    },
    {
        "input": "Cartesian position for q1=3π/8, q2=5π/8, q3=7π/8",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3*np.pi/8", "q2": "5*np.pi/8", "q3": "7*np.pi/8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward geometric model when the three robot angles are respectively 84°, 156°, 228°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": 84, "q2": 156, "q3": 228, "unidad_angular": "grados"}}'
    }
]