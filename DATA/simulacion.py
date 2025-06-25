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
        "input": "Simulate robot with joint configuration (18, 36, 54) degrees",
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
        "input": "Show 3D model at coordinates 775mm, 1550mm, 2325mm",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "posicion_efector": {"x": "775", "y": "1550", "z": "2325", "unidad_posicion": "mm"}}}'
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
        "input": "Render manipulator with joint configuration 87°, 174°, 261°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "87", "q2": "174", "q3": "261", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Generate 3D view with angles 21°, 42°, 63°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "21", "q2": "42", "q3": "63", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    },
    {
        "input": "Show robot with angular positions 48°, 96°, 144°",
        "output": '{"operacion": "simulacion_3d", "parametros": {"q1": "48", "q2": "96", "q3": "144", "unidad_angular": "grados", "posicion_efector": {"x": "", "y": "", "z": "", "unidad_posicion": ""}}}'
    }
]