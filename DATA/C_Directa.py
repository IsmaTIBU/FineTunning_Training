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