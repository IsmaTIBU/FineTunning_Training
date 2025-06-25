simulacion_train = [
    {
        "input": "Simulate the robot with configuration 90, 45, 30 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "90", "q2": "45", "q3": "30", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D visualization with angles 1.57, 0.785, 0 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "1.57", "q2": "0.785", "q3": "0", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate robotic arm with final position at (15, 20, 25) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "15", "y": "20", "z": "25", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Simulation of the arm with the following configuration (15, 20, 25) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "15", "q2": "20", "q3": "25", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D visualization of the end effector at x=1223, y=899mm and z=-987 mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1223", "y": "899", "z": "-987", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Simulate the robot for me with the following configuration: (pi/34, -6pi, 12pi/3)",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/34", "q2": "-6*np.pi", "q3": "12*np.pi/3", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I want a simulation of the robot when its end effector reaches these coordinates (1432, 1644, 896) in millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1432", "y": "1644", "z": "896", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "I would like a simulation of the robotic arm with final position at (1500, 2100, 205) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1500", "y": "2100", "z": "205", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Show me a 3D representation of the end effector at x=1023, y=-399 and z=-987 mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1023", "y": "-399", "z": "-987", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Display the arm with the following configuration (15, 20, 25) in degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "15", "q2": "20", "q3": "25", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D simulation of the robot with angles π/4, π/2, 3π/4 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "3*np.pi/4", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the arm with configuration 60°, 120°, 180°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "60", "q2": "120", "q3": "180", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate robot with end effector at coordinates (800, 1200, 1600) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "800", "y": "1200", "z": "1600", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "3D representation for θ1=5π/6, θ2=π/3, θ3=2π/3 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "5*np.pi/6", "q2": "np.pi/3", "q3": "2*np.pi/3", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulation of the manipulator with joints at 45°, 90°, 135°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize robotic arm with end effector at (2.5, 3.8, 4.1) meters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "2.5", "y": "3.8", "z": "4.1", "unidad_posicion": "m"}}}'
    },
    {
        "input": "3D simulation for angular configuration 7π/12, π/6, 11π/12",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "7*np.pi/12", "q2": "np.pi/6", "q3": "11*np.pi/12", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show the robot with angles 72°, 144°, 216°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulation with final position of the effector at 45cm, 67cm, 89cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "45", "y": "67", "z": "89", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "3D visualization of the arm for θ1=2π/3, θ2=4π/3, θ3=π/6 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "2*np.pi/3", "q2": "4*np.pi/3", "q3": "np.pi/6", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the robot for me with configuration 84°, 168°, 252°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "84", "q2": "168", "q3": "252", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Representation of the manipulator with effector at coordinates (950, 1450, 1950) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "950", "y": "1450", "z": "1950", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "I want a 3D simulation for angles π/8, 5π/8, 7π/8 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/8", "q2": "5*np.pi/8", "q3": "7*np.pi/8", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I would like to visualize the arm with joints at 36°, 108°, 324°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "36", "q2": "108", "q3": "324", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulation of the robot with end effector at position (1.8, 2.4, 3.6) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1.8", "y": "2.4", "z": "3.6", "unidad_posicion": "m"}}}'
    },
    {
        "input": "What is the 3D representation for angular configuration 3π/8, π/4, 9π/8",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "3*np.pi/8", "q2": "np.pi/4", "q3": "9*np.pi/8", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show a simulation of the robot with angles such as 96°, 192°, 288°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "96", "q2": "192", "q3": "288", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "3D simulation with end effector at 78cm, 156cm, 234cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "78", "y": "156", "z": "234", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Visualization of the robotic arm for θ1=11π/12, θ2=π/12, θ3=13π/12 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "11*np.pi/12", "q2": "np.pi/12", "q3": "13*np.pi/12", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the manipulator for me with target position of the effector at (1350, 1800, 2250) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1350", "y": "1800", "z": "2250", "unidad_posicion": "mm"}}}'
    },
    # Correccion 1
    {
        "input": "Render the robot in 3D with joint angles 55°, 110°, 275°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "55", "q2": "110", "q3": "275", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Generate a 3D model of the arm positioned at coordinates (890, 1340, 670) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "890", "y": "1340", "z": "670", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Create a visual simulation with theta values of 4π/9, 8π/9, 2π/9 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "4*np.pi/9", "q2": "8*np.pi/9", "q3": "2*np.pi/9", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display a 3D scene where the robot reaches position x=2.7m, y=1.9m, z=3.4m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "2.7", "y": "1.9", "z": "3.4", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Animate the robotic manipulator with configuration 18°, 126°, 234°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "18", "q2": "126", "q3": "234", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Demonstrate the arm reaching target location (44, 88, 132) centimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "44", "y": "88", "z": "132", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Visualize the mechanical arm with joint rotations 3π/7, π/7, 6π/7",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "3*np.pi/7", "q2": "np.pi/7", "q3": "6*np.pi/7", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Model the robot in 3D space when positioned at 567mm, 1234mm, 890mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "567", "y": "1234", "z": "890", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Show a virtual representation with motor angles 102°, 204°, 306°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "102", "q2": "204", "q3": "306", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Build a 3D visualization of the end effector at coordinates (1.1, 2.2, 3.3) meters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1.1", "y": "2.2", "z": "3.3", "unidad_posicion": "m"}}}'
    },
    # Correccion 2 pt1
    {
        "input": "Generate 3D visualization at coordinates (1245, 2360, 3470) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1245", "y": "2360", "z": "3470", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Create robot model positioned at (675, 1125, 1575) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "675", "y": "1125", "z": "1575", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Display 3D arm at coordinates (850, 1700, 2550) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "850", "y": "1700", "z": "2550", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Render manipulator at position (444, 888, 1332) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "444", "y": "888", "z": "1332", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Show robot visualization at (333, 666, 999) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "333", "y": "666", "z": "999", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Build 3D model with effector at (1080, 2160, 3240) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1080", "y": "2160", "z": "3240", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Simulate arm positioned at coordinates (925, 1850, 2775) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "925", "y": "1850", "z": "2775", "unidad_posicion": "mm"}}}'
    },
    # pt2
    {
        "input": "Simulate robot with this joint configuration (18, 36, 54) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "18", "q2": "36", "q3": "54", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display arm with angles configuration (75, 150, 225) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "75", "q2": "150", "q3": "225", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Render robot with joint setup (42, 84, 126) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "42", "q2": "84", "q3": "126", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Generate 3D view with motor angles (33, 66, 99) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "33", "q2": "66", "q3": "99", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show manipulator with angular configuration (27, 54, 81) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "27", "q2": "54", "q3": "81", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize arm with rotation settings (51, 102, 153) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "51", "q2": "102", "q3": "153", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Create robot model with joint positions (39, 78, 117) degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "39", "q2": "78", "q3": "117", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    # pt3
    {
        "input": "Display robot positioned at 455mm, 910mm, 1365mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "455", "y": "910", "z": "1365", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Generate visualization with effector at 625mm, 1250mm, 1875mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "625", "y": "1250", "z": "1875", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Render arm positioned at 385mm, 770mm, 1155mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "385", "y": "770", "z": "1155", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Build robot model at location 295mm, 590mm, 885mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "295", "y": "590", "z": "885", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Create 3D scene at coordinates 715mm, 1430mm, 2145mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "715", "y": "1430", "z": "2145", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Simulate manipulator positioned at 165mm, 330mm, 495mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "165", "y": "330", "z": "495", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Visualize robot arm at coordinates 845mm, 1690mm, 2535mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "845", "y": "1690", "z": "2535", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Display 3D model with end effector at 525mm, 1050mm, 1575mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "525", "y": "1050", "z": "1575", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Show robot visualization at position 995mm, 1990mm, 2985mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "995", "y": "1990", "z": "2985", "unidad_posicion": "mm"}}}'
    },
    # pt4
    {
        "input": "Simulate robot with joint angles 24°, 48°, 72°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "24", "q2": "48", "q3": "72", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display arm with motor rotations 63°, 126°, 189°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "63", "q2": "126", "q3": "189", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Render manipulator with this joint configuration 87°, 174°, 261°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "87", "q2": "174", "q3": "261", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Generate 3D view with angles 21°, 42°, 63°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "21", "q2": "42", "q3": "63", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show robot with angular positions 48°, 96°, 144°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "48", "q2": "96", "q3": "144", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    # Correccion 3 pt1
    {
        "input": "Show me a simulation with the robot reaching (1.5, 1.0, 2.0) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1.5", "y": "1.0", "z": "2.0", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Simulate the robot when the end effector is at (250, 500, 750) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "250", "y": "500", "z": "750", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "3D visualization of the arm positioned at (35, 70, 105) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "35", "y": "70", "z": "105", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Display the robotic arm when it reaches coordinates (0.8, 1.6, 2.4) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "0.8", "y": "1.6", "z": "2.4", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Visualize the robot with effector at position (180, 360, 540) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "180", "y": "360", "z": "540", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Simulate the manipulator reaching target (12, 24, 36) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "12", "y": "24", "z": "36", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Show 3D representation when the robot is at (3.2, 1.8, 4.5) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "3.2", "y": "1.8", "z": "4.5", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Render the arm with end effector positioned at (420, 840, 1260) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "420", "y": "840", "z": "1260", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Create simulation of the robot at coordinates (55, 110, 165) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "55", "y": "110", "z": "165", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Display the robotic system when positioned at (2.7, 3.6, 1.9) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "2.7", "y": "3.6", "z": "1.9", "unidad_posicion": "m"}}}'
    },
    # pt2
    {
        "input": "Can you display the robot when all joints are at 180 degrees?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "180", "q2": "180", "q3": "180", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the robot with all angles set to 90 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "90", "q2": "90", "q3": "90", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show me the robot when the first two joints are at 45 degrees and the last at 135 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "45", "q2": "45", "q3": "135", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display the arm with the two first angles at 60° and the last one at 120°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "60", "q2": "60", "q3": "120", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the robot when the last joint is at 270 degrees and the first two at 0 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "0", "q2": "0", "q3": "270", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the manipulator with the last two joints at π/2 and the first at π radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi", "q2": "np.pi/2", "q3": "np.pi/2", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show the robot when all three joints are at π/4 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/4", "q2": "np.pi/4", "q3": "np.pi/4", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Render the arm with the first joint at 30° and the last two at 150°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "30", "q2": "150", "q3": "150", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display the robot when all motors are positioned at 240 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "240", "q2": "240", "q3": "240", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the robotic arm with the last angle at 3π/4 and the first two at π/6 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/6", "q2": "np.pi/6", "q3": "3*np.pi/4", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display the robot when all joints are at pi radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi", "q2": "np.pi", "q3": "np.pi", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show the arm with the first two angles at π and the last one at 2*pi",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi", "q2": "np.pi", "q3": "2*np.pi", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the robot when the last two joints are at π/3 and the first at -pi/2",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "-np.pi/2", "q2": "np.pi/3", "q3": "np.pi/3", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the manipulator with all three motors at 3*π/2 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "3*np.pi/2", "q2": "3*np.pi/2", "q3": "3*np.pi/2", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Render the arm when the first angle is at 5π/4, and the last two are at -π/4 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "5*np.pi/4", "q2": "-np.pi/4", "q3": "-np.pi/4", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    # Correccion 4 pt1
    {
        "input": "Show me what happens when I set the joints to 45, 90, and 135 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show me the robot configuration with angles 72, 144, and 216 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show the 3D model when joints are positioned at π/6, π/3, and π/2 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/6", "q2": "np.pi/3", "q3": "np.pi/2", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show me how the robot looks with motor angles 30, 60, and 120 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "30", "q2": "60", "q3": "120", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show the arm visualization with rotations 2π/3, π/4, and 5π/6 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "2*np.pi/3", "q2": "np.pi/4", "q3": "5*np.pi/6", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    # pt2
    {
        "input": "Simulate the robot with joint angles 15, 75, and 165 degrees",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "15", "q2": "75", "q3": "165", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the arm with motor positions 36, 108, and 252 deg",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "36", "q2": "108", "q3": "252", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display the robot when servo angles are 84, 168, and 336 °",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "84", "q2": "168", "q3": "336", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Render the manipulator with axis rotations 27, 81, and 243 grados",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "27", "q2": "81", "q3": "243", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Generate 3D view with stepper angles 51, 102, and 204 degree",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "51", "q2": "102", "q3": "204", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Create simulation with actuator positions 63, 126, and 189 graus",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "63", "q2": "126", "q3": "189", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Build robot model with drive angles 39, 78, and 156 degr",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "39", "q2": "78", "q3": "156", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the arm with encoder values 48, 96, and 192 grd",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "48", "q2": "96", "q3": "192", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Animate robot with joint orientations 21, 42, and 84 dgs",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "21", "q2": "42", "q3": "84", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show mechanical arm with shaft rotations 57, 114, and 228 degs",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "57", "q2": "114", "q3": "228", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Simulate the robot with joint angles π/8, 3π/8, and 5π/8 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/8", "q2": "3*np.pi/8", "q3": "5*np.pi/8", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the arm with motor positions 2π/7, 4π/7, and 6π/7 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "2*np.pi/7", "q2": "4*np.pi/7", "q3": "6*np.pi/7", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display the robot when servo angles are π/12, 7π/12, and 11π/12 radian",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/12", "q2": "7*np.pi/12", "q3": "11*np.pi/12", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Render the manipulator with axis rotations 3π/10, 7π/10, and 9π/10 radianes",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "3*np.pi/10", "q2": "7*np.pi/10", "q3": "9*np.pi/10", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Generate 3D view with stepper angles π/15, 8π/15, and 14π/15 rads",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/15", "q2": "8*np.pi/15", "q3": "14*np.pi/15", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Create simulation with actuator positions π/9, 4π/9, and 8π/9 radiant",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/9", "q2": "4*np.pi/9", "q3": "8*np.pi/9", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Build robot model with drive angles 5π/12, π/4, and 7π/12 radns",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "5*np.pi/12", "q2": "np.pi/4", "q3": "7*np.pi/12", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize the arm with encoder values 2π/11, 9π/11, and 6π/11 rdns",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "2*np.pi/11", "q2": "9*np.pi/11", "q3": "6*np.pi/11", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Animate robot with joint orientations π/16, 9π/16, and 15π/16 rdn",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/16", "q2": "9*np.pi/16", "q3": "15*np.pi/16", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show mechanical arm with shaft rotations 4π/3, π/6, and 5π/4 radianss",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "4*np.pi/3", "q2": "np.pi/6", "q3": "5*np.pi/4", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    # Correccion 5
    {
        "input": "I want to see my robot in 3D when it reaches coordinates (0.75, 1.25, 1.75) meters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "0.75", "y": "1.25", "z": "1.75", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Can I see a 3D visualization at position (450, 680, 920) mm?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "450", "y": "680", "z": "920", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Show me the 3D model when the effector is at (35, 70, 105) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "35", "y": "70", "z": "105", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "I'd like to see how it looks when positioned at (1.8, 2.4, 3.2) meters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "1.8", "y": "2.4", "z": "3.2", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Display the robot in 3D at coordinates (250, 500, 750) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "250", "y": "500", "z": "750", "unidad_posicion": "mm"}}}'
    },
    
    # Frases con ángulos específicos
    {
        "input": "Let me see the 3D view with angles 45°, 90°, 135°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I want to see what happens in 3D with joints at π/4, π/2, 3π/4 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "3*np.pi/4", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show me a 3D representation with configuration 72°, 144°, 216°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Can I see how the robot looks in 3D when set to 1.2, 0.8, 1.5 radians?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "1.2", "q2": "0.8", "q3": "1.5", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I'd love to see the 3D model with angles 30°, 60°, 120°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "30", "q2": "60", "q3": "120", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases mixtas y variadas
    {
        "input": "Generate a 3D scene so I can see the robot at (12, 24, 36) cm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "12", "y": "24", "z": "36", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "I need to see what the 3D visualization looks like at position (890, 1340, 670) mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "890", "y": "1340", "z": "670", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Could you show me a 3D render so I can see the arm at coordinates (2.1, 3.5, 1.8) meters?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "2.1", "y": "3.5", "z": "1.8", "unidad_posicion": "m"}}}'
    },
    {
        "input": "I want to see the robot in 3D space when joints are at π/6, 5π/6, π/3 radians",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "np.pi/6", "q2": "5*np.pi/6", "q3": "np.pi/3", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Let me see how it appears in 3D when positioned at (55, 110, 165) centimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "55", "y": "110", "z": "165", "unidad_posicion": "cm"}}}'
    },
    {
        "input": "Create a 3D model so I can see the manipulator with angles 84°, 168°, 252°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "84", "q2": "168", "q3": "252", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I'd like to see a 3D view of the robot reaching (420, 840, 1260) millimeters",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "420", "y": "840", "z": "1260", "unidad_posicion": "mm"}}}'
    },
    {
        "input": "Show me the 3D simulation so I can see what happens at 2.7, 1.4, 0.6 rad",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "2.7", "q2": "1.4", "q3": "0.6", "unidad_angular": "radianes", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I want to see the robot in 3D when it's at coordinates (0.95, 1.15, 1.35) m",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "0.95", "y": "1.15", "z": "1.35", "unidad_posicion": "m"}}}'
    },
    {
        "input": "Can I see how the 3D model looks when configured to 15°, 75°, 165°?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "15", "q2": "75", "q3": "165", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    }
]

simulacion_NoValues = [
    # Frases cortas y directas
    {
        "input": "Simulate it",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show me the simulation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "How would it look?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Visualize this",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Run simulation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases casuales y naturales
    {
        "input": "Can you show me what this looks like in 3D?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I want to see how my robot would appear",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Could you render this for me?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "What would this configuration look like?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Let me see the visual representation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases conversacionales largas
    {
        "input": "I'm curious to see how my robotic arm would look in this position, can you simulate it?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Hey, would it be possible to get a 3D view of what we're working with here?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Mind showing me what this setup would actually look like in real life?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I'd love to see a virtual model of how the robot is positioned right now",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Can you give me a visual of what's happening with the manipulator?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Variaciones técnicas
    {
        "input": "Generate a 3D visualization of the current state",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Execute visual simulation protocol",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Render the workspace visualization",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Initiate 3D model generation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Display spatial configuration analysis",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases de pregunta/curiosidad
    {
        "input": "What does it look like from this angle?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "How does the robot appear in this setup?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Can I get a preview of what this looks like?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "What would the end result look like visually?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Is there a way to see this in action?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases con contexto emocional
    {
        "input": "I'm having trouble picturing this, could you show me?",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "This is confusing me, I need a visual",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "I'm excited to see how this turns out!",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Honestly, I have no idea what this would look like",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Help me understand this by showing me the visualization",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Variaciones informales
    {
        "input": "Gimme the visual",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show me what we got",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Let's see it in action",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Hit me with the simulation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Fire up the 3D view",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases de proceso/workflow
    {
        "input": "Next step: show me the visualization",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Now let's see what this looks like",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Time to visualize this setup",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Ready for the 3D representation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Final step: render the simulation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    
    # Frases de validación/verificación
    {
        "input": "I need to verify this visually",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Let me double-check by seeing the simulation",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    }
]

simulation_train = simulacion_train + simulacion_NoValues