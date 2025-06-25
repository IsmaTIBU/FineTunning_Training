matrices_train = [
    {
        "input": "Calculate the transformation matrices for q1=30°, q2=45°, q3=60°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "30", "q2": "45", "q3": "60", "unidad_angular": "grados"}}'
    },
    {
        "input": "I need the T matrices with angles 0.5, 1.2, 0.8 radians",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "0.5", "q2": "1.2", "q3": "0.8", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Get T01, T12, T23 and T03 with q1=90°, q2=0°, q3=45°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "90", "q2": "0", "q3": "45", "unidad_angular": "grados"}}'
    },
    {
        "input": "Homogeneous transformation matrices for configuration 1.57, 0, 0.785 rad",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "1.57", "q2": "0", "q3": "0.785", "unidad_angular": "radianes"}}'
    },
    {
        "input": "I want the T matrices for theta1=45°, theta2=30°, theta3=60°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "45", "q2": "30", "q3": "60", "unidad_angular": "grados"}}'
    },
    {
        "input": "When angle1=20 degrees, angle2=-67 degrees and angle3=0 degrees, what would be the robot transformation matrix calculation?",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "20", "q2": "-67", "q3": "0", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate the robot transformation matrices when q1=pi/2, q2=pi and q3=-pi/3",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "np.pi/2", "q2": "np.pi", "q3": "-np.pi/3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "What would be the transformation matrices when q1=3pi/2, q2=5pi and q3=-8pi/3",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "3*np.pi/2", "q2": "5*np.pi", "q3": "-8*np.pi/3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "I need the transformation matrices for the following angles in degrees: -25, 89, 6",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "-25", "q2": "89", "q3": "6", "unidad_angular": "grados"}}'
    },
    {
        "input": "I want to know the T matrices for these angles [pi/3, 6pi/4, -3pi/5]",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "np.pi/3", "q2": "6*np.pi/4", "q3": "-3*np.pi/5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "T matrices for configuration π/3, 2π/3, π radians",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "np.pi/3", "q2": "2*np.pi/3", "q3": "np.pi", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate transformation matrices for 36°, 72°, 108°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "36", "q2": "72", "q3": "108", "unidad_angular": "grados"}}'
    },
    {
        "input": "Homogeneous matrices for θ1=5π/6, θ2=π/6, θ3=4π/3",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "5*np.pi/6", "q2": "np.pi/6", "q3": "4*np.pi/3", "unidad_angular": "radianes"}}'
    },
    {
        "input": "I need the T matrices for angles 135°, 225°, 315°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "135", "q2": "225", "q3": "315", "unidad_angular": "grados"}}'
    },
    {
        "input": "Transformations for angular configuration [7π/12, 11π/12, 5π/4] rad",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "7*np.pi/12", "q2": "11*np.pi/12", "q3": "5*np.pi/4", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Transformation matrices when q1=84 degrees, q2=168 degrees, q3=252 degrees",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "84", "q2": "168", "q3": "252", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculation of T matrices for θ1=π/8, θ2=7π/8, θ3=3π/2",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "np.pi/8", "q2": "7*np.pi/8", "q3": "3*np.pi/2", "unidad_angular": "radianes"}}'
    },
    {
        "input": "I want the homogeneous transformation for joints at 54°, 162°, 270°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "54", "q2": "162", "q3": "270", "unidad_angular": "grados"}}'
    },
    {
        "input": "T01, T12, T23, T03 matrices for configuration 13π/12, π/12, 17π/12 radians",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "13*np.pi/12", "q2": "np.pi/12", "q3": "17*np.pi/12", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate transformations for angles 48°, 96°, 192°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "48", "q2": "96", "q3": "192", "unidad_angular": "grados"}}'
    },
    {
        "input": "Robot transformation matrices for π/5, 3π/5, 6π/5",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "np.pi/5", "q2": "3*np.pi/5", "q3": "6*np.pi/5", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Homogeneous transformation for theta1=66 degrees, theta2=132 degrees, theta3=198 degrees",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "66", "q2": "132", "q3": "198", "unidad_angular": "grados"}}'
    },
    {
        "input": "T matrices for angular configuration 9π/16, 3π/16, 15π/16 rad",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "9*np.pi/16", "q2": "3*np.pi/16", "q3": "15*np.pi/16", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the transformation matrices for 78°, 156°, 234°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "78", "q2": "156", "q3": "234", "unidad_angular": "grados"}}'
    },
    {
        "input": "Homogeneous matrices when angles are 2π/9, 4π/9, 8π/9 radians",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "2*np.pi/9", "q2": "4*np.pi/9", "q3": "8*np.pi/9", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Transformations for joint1=42°, joint2=126°, joint3=294°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "42", "q2": "126", "q3": "294", "unidad_angular": "grados"}}'
    },
    {
        "input": "T matrices of the robotic arm for θ1=11π/16, θ2=5π/16, θ3=13π/16",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "11*np.pi/16", "q2": "5*np.pi/16", "q3": "13*np.pi/16", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Calculate the matrices for configuration 93°, 186°, 279°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "93", "q2": "186", "q3": "279", "unidad_angular": "grados"}}'
    },
    {
        "input": "Transformation matrices for angles 4π/7, 2π/7, 6π/7 rad",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "4*np.pi/7", "q2": "2*np.pi/7", "q3": "6*np.pi/7", "unidad_angular": "radianes"}}'
    },
    {
        "input": "Homogeneous transformation of the manipulator for 21°, 105°, 189°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "21", "q2": "105", "q3": "189", "unidad_angular": "grados"}}'
    },
    # Correccion 1
    {
        "input": "Calculate transformation matrices for angles 45°, 186°, 315°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "45", "q2": "186", "q3": "315", "unidad_angular": "grados"}}'
    },
    {
        "input": "I need the T matrices for configuration 72°, 162°, 288°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "72", "q2": "162", "q3": "288", "unidad_angular": "grados"}}'
    },
    {
        "input": "Homogeneous matrices for joint angles 36°, 174°, 252°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "36", "q2": "174", "q3": "252", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate the matrices for robot configuration 84°, 168°, 336°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "84", "q2": "168", "q3": "336", "unidad_angular": "grados"}}'
    },
    {
        "input": "Transformation matrices when q1=60°, q2=180°, q3=240°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "60", "q2": "180", "q3": "240", "unidad_angular": "grados"}}'
    },
    {
        "input": "Get T01, T12, T23 matrices for angles 27°, 165°, 294°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "27", "q2": "165", "q3": "294", "unidad_angular": "grados"}}'
    },
    {
        "input": "I want transformation matrices for configuration 48°, 183°, 267°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "48", "q2": "183", "q3": "267", "unidad_angular": "grados"}}'
    },
    {
        "input": "Calculate T matrices with joint setup 33°, 177°, 321°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "33", "q2": "177", "q3": "321", "unidad_angular": "grados"}}'
    },
    {
        "input": "Homogeneous transformation for angles 51°, 189°, 258°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "51", "q2": "189", "q3": "258", "unidad_angular": "grados"}}'
    },
    {
        "input": "Transformation matrices for robot joints at 39°, 171°, 303°",
        "output": '{"operacion": "matrices_transformacion", "parametros": {"q1": "39", "q2": "171", "q3": "303", "unidad_angular": "grados"}}'
    }
]