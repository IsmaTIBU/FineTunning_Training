simulacion_train = [
    {
        "input": "Simulate the robot with configuration 90, 45, 30 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 90, "q2": 45, "q3": 30, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D visualization with angles 1.57, 0.785, 0 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "1.57", "q2": "0.785", "q3": "0", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate robotic arm with final position at (15, 20, 25) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 15, "y": 20, "z": 25, "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Simulation of the arm with the following configuration (15, 20, 25) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 15, "q2": 20, "q3": 25, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D visualization of the end effector at x=1223, y=899mm and z=-987 mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 1223, "y": 899, "z": -987, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Simulate the robot for me with the following configuration: (pi/34, -6pi, 12pi/3)",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/34", "q2": "-6*np.pi", "q3": "12*np.pi/3", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I want a simulation of the robot when its end effector reaches these coordinates (1432, 1644, 896) in millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 1432, "y": 1644, "z": 896, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "I would like a simulation of the robotic arm with final position at (1500, 2100, 205) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 1500, "y": 2100, "z": 205, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Show me a 3D representation of the end effector at x=1023, y=-399 and z=-987 mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 1023, "y": -399, "z": -987, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Display the arm with the following configuration (15, 20, 25) in degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 15, "q2": 20, "q3": 25, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D simulation of the robot with angles π/4, π/2, 3π/4 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "3*np.pi/4", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the arm with configuration 60°, 120°, 180°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 60, "q2": 120, "q3": 180, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate robot with end effector at coordinates (800, 1200, 1600) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 800, "y": 1200, "z": 1600, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "3D representation for θ1=5π/6, θ2=π/3, θ3=2π/3 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "5*np.pi/6", "q2": "np.pi/3", "q3": "2*np.pi/3", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulation of the manipulator with joints at 45°, 90°, 135°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 45, "q2": 90, "q3": 135, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize robotic arm with end effector at (2.5, 3.8, 4.1) meters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 2.5, "y": 3.8, "z": 4.1, "unidad_posicion": "m"}}}'
    },
    {
        "input": "3D simulation for angular configuration 7π/12, π/6, 11π/12",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "7*np.pi/12", "q2": "np.pi/6", "q3": "11*np.pi/12", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show the robot with angles 72°, 144°, 216°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 72, "q2": 144, "q3": 216, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulation with final position of the effector at 45cm, 67cm, 89cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 45, "y": 67, "z": 89, "unidad_posicion": "cm"}}}'
    },
    {
        "input": "3D visualization of the arm for θ1=2π/3, θ2=4π/3, θ3=π/6 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "2*np.pi/3", "q2": "4*np.pi/3", "q3": "np.pi/6", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the robot for me with configuration 84°, 168°, 252°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 84, "q2": 168, "q3": 252, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Representation of the manipulator with effector at coordinates (950, 1450, 1950) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 950, "y": 1450, "z": 1950, "unidad_posicion": "mm"}}}'
    },
    {
        "input": "I want a 3D simulation for angles π/8, 5π/8, 7π/8 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/8", "q2": "5*np.pi/8", "q3": "7*np.pi/8", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I would like to visualize the arm with joints at 36°, 108°, 324°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 36, "q2": 108, "q3": 324, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulation of the robot with end effector at position (1.8, 2.4, 3.6) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 1.8, "y": 2.4, "z": 3.6, "unidad_posicion": "m"}}}'
    },
    {
        "input": "What is the 3D representation for angular configuration 3π/8, π/4, 9π/8",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "3*np.pi/8", "q2": "np.pi/4", "q3": "9*np.pi/8", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show a simulation of the robot with angles such as 96°, 192°, 288°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": 96, "q2": 192, "q3": 288, "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D simulation with end effector at 78cm, 156cm, 234cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 78, "y": 156, "z": 234, "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Visualization of the robotic arm for θ1=11π/12, θ2=π/12, θ3=13π/12 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "11*np.pi/12", "q2": "np.pi/12", "q3": "13*np.pi/12", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the manipulator for me with target position of the effector at (1350, 1800, 2250) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": 1350, "y": 1800, "z": 2250, "unidad_posicion": "mm"}}}'
    }
]