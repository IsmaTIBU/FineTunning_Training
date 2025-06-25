cinematica_directa_train = [
    {
        "input": "Direct kinematics with q1=1.57 rad, q2=0.785 rad, q3=0 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.57", "q2": "0.785", "q3": "0", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the end effector position with angles 30°, 45°, 60°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "30", "q2": "45", "q3": "60", "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward kinematics with configuration 90°, 0°, 45°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "90", "q2": "0", "q3": "45", "unidad_angular": "grados"}}'
    },
    {
        "input": "End effector position for theta1=0.5, theta2=1.2, theta3=0.8 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.5", "q2": "1.2", "q3": "0.8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the robot position with this configuration [pi/2, pi, -pi] in rad?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/2", "q2": "np.pi", "q3": "-np.pi", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Knowing that the robot angles are 20,45,2 deg, what is the end effector position?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "20", "q2": "45", "q3": "2", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate the forward kinematics when angle1=pi/8, angle2=0, angle3=-3pi/2",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/8", "q2": "0", "q3": "-3*np.pi/2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the forward geometric model for q1=29, q2=90 and q3=-56 degrees",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "29", "q2": "90", "q3": "-56", "unidad_angular": "grados"}}'
    },
    {
        "input": "I want to know the forward geometric model when angle1=8*pi, angle2=-7pi/3 and angle3=7pi/8",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "8*np.pi", "q2": "-7*np.pi/3", "q3": "7*np.pi/8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "When the first robot angle is 34 degrees, the second 56 and the last -3 what is the final robot position?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "34", "q2": "56", "q3": "-3", "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward geometric model of the robot for theta1=π/4, theta2=π/3, theta3=π/6",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/4", "q2": "np.pi/3", "q3": "np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Final position when q1=45°, q2=30°, q3=90°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "45", "q2": "30", "q3": "90", "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct kinematics for configuration [2π, π/2, -π/4] radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2*np.pi", "q2": "np.pi/2", "q3": "-np.pi/4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Where will the end effector be if angle1=120 deg, angle2=60 deg, angle3=180 deg?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "120", "q2": "60", "q3": "180", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate end effector position with 3π/4, -π/8, 5π/6",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3*np.pi/4", "q2": "-np.pi/8", "q3": "5*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics: first angle 15°, second angle 75°, third angle -45°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "15", "q2": "75", "q3": "-45", "unidad_angular": "grados"}}'
    },
    {
        "input": "Robot position when θ1=π, θ2=π/3, θ3=2π/3 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi", "q2": "np.pi/3", "q3": "2*np.pi/3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the direct kinematics of the arm for angles 72°, 36°, 144°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "72", "q2": "36", "q3": "144", "unidad_angular": "grados"}}'
    },
    {
        "input": "With q1=-π/2, q2=3π/2, q3=-2π what is the final robot position?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "-np.pi/2", "q2": "3*np.pi/2", "q3": "-2*np.pi", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward geometric model for 270 degrees, 180 degrees and 0 degrees",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "270", "q2": "180", "q3": "0", "unidad_angular": "grados"}}'
    },
    {
        "input": "What is the cartesian position when angles are π/12, 7π/12, -π/12",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/12", "q2": "7*np.pi/12", "q3": "-np.pi/12", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics calculation: q1=33°, q2=66°, q3=99°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "33", "q2": "66", "q3": "99", "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward geometric model for angular configuration [4π/3, π/6, 5π/4] in radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "4*np.pi/3", "q2": "np.pi/6", "q3": "5*np.pi/4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "End effector final position with theta1=150 deg, theta2=210 deg, theta3=330 deg",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "150", "q2": "210", "q3": "330", "unidad_angular": "grados"}}'
    },
    {
        "input": "Where does the robot end up if angle1=π/10, angle2=9π/10, angle3=π/5?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/10", "q2": "9*np.pi/10", "q3": "np.pi/5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics for joint1=12°, joint2=24°, joint3=48°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "12", "q2": "24", "q3": "48", "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct kinematics of the robotic arm with 7π/6, -π/3, 11π/6 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "7*np.pi/6", "q2": "-np.pi/3", "q3": "11*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the final position for 225°, 315°, 135°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "225", "q2": "315", "q3": "135", "unidad_angular": "grados"}}'
    },
    {
        "input": "Cartesian position for q1=3π/8, q2=5π/8, q3=7π/8",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3*np.pi/8", "q2": "5*np.pi/8", "q3": "7*np.pi/8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward geometric model when the three robot angles are respectively 84°, 156°, 228°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "84", "q2": "156", "q3": "228", "unidad_angular": "grados"}}'
    },
    # Correccion 1
    {
        "input": "Calculate the forward kinematics when angle1=pi/8, angle2=0, angle3=-3pi/2",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/8", "q2": "0", "q3": "-3*np.pi/2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "End effector final position with theta1=150 degrees, theta2=210 degrees, theta3=330 degrees",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "150", "q2": "210", "q3": "330", "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct kinematics of the robotic arm with 7π/6, -π/3, 11π/6 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "7*np.pi/6", "q2": "-np.pi/3", "q3": "11*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the end effector position when q1=45 degrees, q2=90 degrees, q3=135 degrees?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward geometric model when angle1=2π/3, angle2=π/4, angle3=5π/6 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2*np.pi/3", "q2": "np.pi/4", "q3": "5*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the end effector position with joint angles 25°, 85°, 165°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "25", "q2": "85", "q3": "165", "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct kinematics calculation with theta1=3π/8, theta2=7π/8, theta3=π/2 in radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3*np.pi/8", "q2": "7*np.pi/8", "q3": "np.pi/2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Where is the end effector when the robot angles are 72 degrees, 144 degrees, 288 degrees?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "72", "q2": "144", "q3": "288", "unidad_angular": "grados"}}'
    },
    {
        "input": "Which are the forward kinematics with joint configuration π/6, 5π/12, 11π/12 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/6", "q2": "5*np.pi/12", "q3": "11*np.pi/12", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the robot end effector position when q1=240°, q2=300°, q3=60°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "240", "q2": "300", "q3": "60", "unidad_angular": "grados"}}'
    },
    # Correccion 2 pt1
    {
        "input": "Calculate forward kinematics when angle1=2*pi, angle2=-pi/4, angle3=5*pi/6",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2*np.pi", "q2": "-np.pi/4", "q3": "5*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the end effector position when angle1=3*pi/2, angle2=pi/6, angle3=-2*pi/3",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3*np.pi/2", "q2": "np.pi/6", "q3": "-2*np.pi/3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward geometric model when angle1=5*pi/4, angle2=-3*pi/8, angle3=7*pi/12",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "5*np.pi/4", "q2": "-3*np.pi/8", "q3": "7*np.pi/12", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate robot position when angle1=pi/3, angle2=4*pi, angle3=-pi/12",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/3", "q2": "4*np.pi", "q3": "-np.pi/12", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics with angle1=7*pi/8, angle2=-5*pi/6, angle3=11*pi/12",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "7*np.pi/8", "q2": "-5*np.pi/6", "q3": "11*np.pi/12", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Find end effector position when angle1=9*pi/10, angle2=pi/8, angle3=-4*pi/5",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "9*np.pi/10", "q2": "np.pi/8", "q3": "-4*np.pi/5", "unidad_angular": "radianes"}}'
    },
    # pt 3
    {
        "input": "Calculate the end effector position with joint angles 42°, 84°, 126°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "42", "q2": "84", "q3": "126", "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward kinematics with motor angles 18°, 36°, 54°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "18", "q2": "36", "q3": "54", "unidad_angular": "grados"}}'
    },
    {
        "input": "What is the robot position with angles 63°, 126°, 189°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "63", "q2": "126", "q3": "189", "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct kinematics calculation with joint angles 27°, 54°, 81°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "27", "q2": "54", "q3": "81", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate end effector position using angles 75°, 150°, 225°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "75", "q2": "150", "q3": "225", "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward geometric model with rotation angles 39°, 78°, 117°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "39", "q2": "78", "q3": "117", "unidad_angular": "grados"}}'
    },
    {
        "input": "What is the final position with joint angles 51°, 102°, 153°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "51", "q2": "102", "q3": "153", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate robot end position with angles 33°, 66°, 99°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "33", "q2": "66", "q3": "99", "unidad_angular": "grados"}}'
    },
    {
        "input": "Direct kinematics with servo angles 21°, 42°, 63°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "21", "q2": "42", "q3": "63", "unidad_angular": "grados"}}'
    },
    {
        "input": "Forward kinematics calculation using angles 48°, 96°, 144°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "48", "q2": "96", "q3": "144", "unidad_angular": "grados"}}'
    },
    # Correccion 3
    {
        "input": "What's the robot position when the motors are at 2.1, 0.9, 1.7 radians?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.1", "q2": "0.9", "q3": "1.7", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate direct kinematics with motors positioned at 1.5, 2.8, 0.6 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.5", "q2": "2.8", "q3": "0.6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward kinematics when the three motors are at 3.2, 1.1, 2.4 radianes",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3.2", "q2": "1.1", "q3": "2.4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the end effector position with motors at 0.8, 1.9, 3.3 rad?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.8", "q2": "1.9", "q3": "3.3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics calculation when motors are configured to 2.7, 0.4, 1.8 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.7", "q2": "0.4", "q3": "1.8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the forward geometric model with motor angles 1.3, 2.6, 0.2 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.3", "q2": "2.6", "q3": "0.2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What's the robot's final position when motors are set to 3.8, 1.4, 2.9 radianes?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3.8", "q2": "1.4", "q3": "2.9", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward kinematics with motor configuration 0.5, 3.1, 1.6 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.5", "q2": "3.1", "q3": "1.6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate end effector position when the motors rotate to 2.2, 0.7, 3.5 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.2", "q2": "0.7", "q3": "3.5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics for motor positions 1.9, 2.3, 0.1 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.9", "q2": "2.3", "q3": "0.1", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What's the robot position when the axes are at 1.4, 2.7, 0.8 radians?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.4", "q2": "2.7", "q3": "0.8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate forward kinematics with axes positioned at 3.6, 1.2, 2.5 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3.6", "q2": "1.2", "q3": "2.5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics when the three axes are at 0.3, 1.8, 3.4 radianes",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.3", "q2": "1.8", "q3": "3.4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What is the end effector position with axes at 2.9, 0.6, 1.1 rad?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.9", "q2": "0.6", "q3": "1.1", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward geometric model calculation when axes are configured to 1.7, 3.0, 0.4 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.7", "q2": "3.0", "q3": "0.4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the direct kinematics with axis angles 2.8, 1.5, 3.7 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.8", "q2": "1.5", "q3": "3.7", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What's the robot's final position when axes are set to 0.9, 2.4, 1.3 radianes?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.9", "q2": "2.4", "q3": "1.3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Direct kinematics with axis configuration 3.3, 0.7, 2.1 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "3.3", "q2": "0.7", "q3": "2.1", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate end effector position when the axes rotate to 1.6, 2.9, 0.5 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.6", "q2": "2.9", "q3": "0.5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Forward kinematics for axis positions 2.0, 1.0, 3.8 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.0", "q2": "1.0", "q3": "3.8", "unidad_angular": "radianes"}}'
    },
    # Correccion 4
    {
        "input": "What's the robot position when the motors are at 2.1, 0.9, 1.7 radians?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.1", "q2": "0.9", "q3": "1.7", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the end effector position with motors set to 45°, 90°, 135°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados"}}'
    },
    {
        "input": "What position does the robot reach when motors are at π/4, π/2, 3π/4 radians?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "3*np.pi/4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Find the robot's position when all motors are positioned at 60°, 120°, 180°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "60", "q2": "120", "q3": "180", "unidad_angular": "grados"}}'
    },
    {
        "input": "I need to know the final position with motors at 1.2, 0.8, 1.5 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.2", "q2": "0.8", "q3": "1.5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What's the arm position when the three motors are set to 30°, 75°, 150°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "30", "q2": "75", "q3": "150", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate robot position with motors configured at π/6, 2π/3, 5π/6 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/6", "q2": "2*np.pi/3", "q3": "5*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Where is the end effector position when motors read 72°, 144°, 216°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados"}}'
    },
    {
        "input": "Tell me the robot position when motors are running at 0.5, 1.8, 2.3 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.5", "q2": "1.8", "q3": "2.3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What's the final position with motors adjusted to 15°, 45°, 90°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "15", "q2": "45", "q3": "90", "unidad_angular": "grados"}}'
    },
    {
        "input": "Get the arm position when motors are positioned at π/8, 3π/8, 7π/8 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/8", "q2": "3*np.pi/8", "q3": "7*np.pi/8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Show me the robot position with motors turned to 84°, 168°, 252°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "84", "q2": "168", "q3": "252", "unidad_angular": "grados"}}'
    },
    {
        "input": "What position will the robot be in when motors are at 2.7, 1.4, 0.6 radians?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.7", "q2": "1.4", "q3": "0.6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the manipulator position when motors are set to 36°, 108°, 252°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "36", "q2": "108", "q3": "252", "unidad_angular": "grados"}}'
    },
    {
        "input": "Determine the end position when all motors reach π/3, 4π/3, 2π/3 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/3", "q2": "4*np.pi/3", "q3": "2*np.pi/3", "unidad_angular": "radianes"}}'
    },
    # Correccion 5
    {
        "input": "Urgent! Need to know where my robot arm points when joints are at 1.8, 0.6, 2.4 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "1.8", "q2": "0.6", "q3": "2.4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the end effector position when joints are set to 45°, 90°, 135°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados"}}'
    },
    {
        "input": "Where does the robot point when all joints are positioned at π/4, π/2, 3π/4 radians?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "3*np.pi/4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Find the robot's final position with joints configured to 60°, 120°, 180°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "60", "q2": "120", "q3": "180", "unidad_angular": "grados"}}'
    },
    {
        "input": "What's the end position when joints rotate to 2.1, 0.9, 1.7 rad?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.1", "q2": "0.9", "q3": "1.7", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Tell me where the arm reaches when joints are at 30°, 75°, 150°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "30", "q2": "75", "q3": "150", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate forward kinematics with joints positioned at π/6, 2π/3, 5π/6 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/6", "q2": "2*np.pi/3", "q3": "5*np.pi/6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "I need the robot position when joints are adjusted to 72°, 144°, 216°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados"}}'
    },
    {
        "input": "Show me where the manipulator goes when joints move to 0.5, 1.8, 2.3 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "0.5", "q2": "1.8", "q3": "2.3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What's the end effector location with joints turned to 15°, 45°, 90°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "15", "q2": "45", "q3": "90", "unidad_angular": "grados"}}'
    },
    {
        "input": "Determine the arm position when joints are set to π/8, 3π/8, 7π/8 rad",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/8", "q2": "3*np.pi/8", "q3": "7*np.pi/8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Where will the robot end up with joints rotated to 84°, 168°, 252°?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "84", "q2": "168", "q3": "252", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate the final position when joints reach 2.7, 1.4, 0.6 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "2.7", "q2": "1.4", "q3": "0.6", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Get the robot coordinates when joints are oriented at 36°, 108°, 252°",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "36", "q2": "108", "q3": "252", "unidad_angular": "grados"}}'
    },
    {
        "input": "Find where the end effector points when joints are locked at π/3, 4π/3, 2π/3 radians",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "np.pi/3", "q2": "4*np.pi/3", "q3": "2*np.pi/3", "unidad_angular": "radianes"}}'
    }
]

cinematica_directa_NoValues =[
    {
        "input": "Calculate the forward kinematics",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "What's the position of my robot?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Show me the end effector position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Calculate direct kinematics please",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Where is my robot's end effector?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Find the robot's current position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "I need the forward geometric model",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Calculate where the robot arm ends up",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "What's the final position of the robot?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Show me the robot's end position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Compute the forward kinematics",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Tell me the cartesian position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Where does the robot reach?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Calculate the robot's workspace position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "I want to know the end effector coordinates",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Determine the robot's final location",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Show me where the arm points to",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Calculate the end point position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "What are the end effector coordinates?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Find the robot's tip position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Get the forward kinematics result",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Tell me the robot's reach position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Calculate the direct geometric model",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Where is the robot pointing?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Show me the current robot position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "I need the robot's end location",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Calculate where the robot ends up",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "What's the robot's current coordinates?",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Find the manipulator's end position",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    },
    {
        "input": "Give me the forward kinematics calculation",
        "output": '{"operacion": "cinematica_directa", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": ""}}'
    }
]

cinematica_directa_train = cinematica_directa_train + cinematica_directa_NoValues