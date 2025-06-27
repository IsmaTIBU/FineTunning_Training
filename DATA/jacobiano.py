jacobiano_train = [
   {
       "input": "Calculate the jacobian with q1=30°, q2=45°, q3=60° and velocities 2, 1.5, 3 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "30", "q2": "45", "q3": "60", "unidad_angular": "grados", "q1_dot": "2", "q2_dot": "1.5", "q3_dot": "3", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian for angles 0.5, 1.2, 0.8 rad and angular velocities 1, 2, 1.5 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "0.5", "q2": "1.2", "q3": "0.8", "unidad_angular": "radianes", "q1_dot": "1", "q2_dot": "2", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "I need the jacobian with configuration 90°, 45°, 0° and velocities 0.5, 1, 2 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "90", "q2": "45", "q3": "0", "unidad_angular": "grados", "q1_dot": "0.5", "q2_dot": "1", "q3_dot": "2", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "I would like to know what the jacobian is when the first angle is 23 degrees, the second is 43 and the last 3 and when their joint velocities are 2 rad/s, 3 and 6.7",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "23", "q2": "43", "q3": "3", "unidad_angular": "grados", "q1_dot": "2", "q2_dot": "3", "q3_dot": "6.7", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian when angular velocity is -1rad/s, 2.2 rad/s, 1.5 rad/s and angles are 3, -45, 23 degrees",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "3", "q2": "-45", "q3": "23", "unidad_angular": "grados", "q1_dot": "1", "q2_dot": "2.2", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "What is the jacobian when q1=30°, q2=45°, q3=60° and velocities 2, 1.5, 3 radians per second",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "30", "q2": "45", "q3": "60", "unidad_angular": "grados", "q1_dot": "2", "q2_dot": "1.5", "q3_dot": "3", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "I want the jacobian when angle1=90°, angle2=45°, angle3=0° and velocities -0.5, 1, -2 radians per second",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "90", "q2": "45", "q3": "0", "unidad_angular": "grados", "q1_dot": "0.5", "q2_dot": "1", "q3_dot": "2", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Show me the Jacobian for angles -pi/3, pi/2, -8pi/3 and velocities 0.8, 2, 0.5 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "-np.pi/3", "q2": "np.pi/2", "q3": "-8*np.pi/3", "unidad_angular": "radianes", "q1_dot": "0.8", "q2_dot": "2", "q3_dot": "0.5", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian with -pi/3, pi/2, -8pi/3 and 0.8, 2, 0.5 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "-np.pi/3", "q2": "np.pi/2", "q3": "-8*np.pi/3", "unidad_angular": "radianes", "q1_dot": "0.8", "q2_dot": "2", "q3_dot": "0.5", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Calculate the Jacobian with -3pi/2, -pi/2 and -8pi/3 and 0.2, 2 and -0.5 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "-3np.pi/2", "q2": "-np.pi/2", "q3": "-8*np.pi/3", "unidad_angular": "radianes", "q1_dot": "0.2", "q2_dot": "2", "q3_dot": "-0.5", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian for θ1=π/4, θ2=π/2, θ3=3π/4 and velocities 1.5, 2.5, 3.5 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "3*np.pi/4", "unidad_angular": "radianes", "q1_dot": "1.5", "q2_dot": "2.5", "q3_dot": "3.5", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Calculate jacobian with angles 60°, 120°, 180° and velocities 0.8, 1.2, 1.6 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "60", "q2": "120", "q3": "180", "unidad_angular": "grados", "q1_dot": "0.8", "q2_dot": "1.2", "q3_dot": "1.6", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian matrix for configuration π/6, 5π/6, -π/3 with velocities 2.1, 1.8, 2.4 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/6", "q2": "5*np.pi/6", "q3": "-np.pi/3", "unidad_angular": "radianes", "q1_dot": "2.1", "q2_dot": "1.8", "q3_dot": "2.4", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian when q1=45 deg, q2=90 deg, q3=135 deg and angular velocities 1.0, 2.0, 3.0 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados", "q1_dot": "1.0", "q2_dot": "2.0", "q3_dot": "3.0", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian calculation for angles 2π/3, π/12, 7π/12 and dq = [1.7, 2.3, 1.9] rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "2*np.pi/3", "q2": "np.pi/12", "q3": "7*np.pi/12", "unidad_angular": "radianes", "q1_dot": "1.7", "q2_dot": "2.3", "q3_dot": "1.9", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Robot jacobian with theta1=72°, theta2=144°, theta3=216° and velocities dq1=0.5, dq2=1.5, dq3=2.5 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados", "q1_dot": "0.5", "q2_dot": "1.5", "q3_dot": "2.5", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian matrix when angles are π/8, 3π/8, 5π/8 rad and velocities 2.8, 1.4, 3.2 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/8", "q2": "3*np.pi/8", "q3": "5*np.pi/8", "unidad_angular": "radianes", "q1_dot": "2.8", "q2_dot": "1.4", "q3_dot": "3.2", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "I need jacobian for configuration 15°, 75°, 165° with angular velocities dq1=1.1, dq2=2.2, dq3=3.3 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "15", "q2": "75", "q3": "165", "unidad_angular": "grados", "q1_dot": "1.1", "q2_dot": "2.2", "q3_dot": "3.3", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian for θ1=4π/3, θ2=5π/3, θ3=π/3 and q1_dot=1.6, q2_dot=2.6, q3_dot=3.6 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "4*np.pi/3", "q2": "5*np.pi/3", "q3": "np.pi/3", "unidad_angular": "radianes", "q1_dot": "1.6", "q2_dot": "2.6", "q3_dot": "3.6", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Calculate the jacobian with joints at 105, 195 and 285 degrees and velocities 0.9, 1.8, 2.7 radians per second",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "105", "q2": "195", "q3": "285", "unidad_angular": "grados", "q1_dot": "0.9", "q2_dot": "1.8", "q3_dot": "2.7", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Manipulator jacobian for π/10, 9π/10, 2π/5 rad with velocities [2.0, 1.3, 2.9] rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/10", "q2": "9*np.pi/10", "q3": "2*np.pi/5", "unidad_angular": "radianes", "q1_dot": "2.0", "q2_dot": "1.3", "q3_dot": "2.9", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian matrix when q1=36 deg, q2=108 deg, q3=252 deg and velocities 1.4, 2.1, 2.8 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "36", "q2": "108", "q3": "252", "unidad_angular": "grados", "q1_dot": "1.4", "q2_dot": "2.1", "q3_dot": "2.8", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian for angular configuration 7π/8, π/16, 15π/16 and angular velocities 3.1, 1.7, 2.2 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "7*np.pi/8", "q2": "np.pi/16", "q3": "15*np.pi/16", "unidad_angular": "radianes", "q1_dot": "3.1", "q2_dot": "1.7", "q3_dot": "2.2", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Calculate jacobian for angles 84°, 168°, 252° with q_dot = 0.7, 1.9, 3.1 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "84", "q2": "168", "q3": "252", "unidad_angular": "grados", "q1_dot": "0.7", "q2_dot": "1.9", "q3_dot": "3.1", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Robotic arm jacobian with θ1=11π/12, θ2=π/24, θ3=13π/12 and velocities 2.5, 1.1, 3.4 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "11*np.pi/12", "q2": "np.pi/24", "q3": "13*np.pi/12", "unidad_angular": "radianes", "q1_dot": "2.5", "q2_dot": "1.1", "q3_dot": "3.4", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian matrix for 51°, 102°, 204° and joint velocities 1.8, 2.4, 1.2 radians per second",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "51", "q2": "102", "q3": "204", "unidad_angular": "grados", "q1_dot": "1.8", "q2_dot": "2.4", "q3_dot": "1.2", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian when first angle=3π/16, second angle=9π/16, third angle=21π/16 with velocities 2.7, 1.5, 3.0 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "3*np.pi/16", "q2": "9*np.pi/16", "q3": "21*np.pi/16", "unidad_angular": "radianes", "q1_dot": "2.7", "q2_dot": "1.5", "q3_dot": "3.0", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Calculate jacobian for joint angles 63, 126, 189 deg and joint velocities 0.6, 2.7, 1.8 rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "63", "q2": "126", "q3": "189", "unidad_angular": "grados", "q1_dot": "0.6", "q2_dot": "2.7", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "System jacobian for π/20, 19π/20, 3π/5 radians and velocities [3.5, 1.0, 2.6] rad/s",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/20", "q2": "19*np.pi/20", "q3": "3*np.pi/5", "unidad_angular": "radianes", "q1_dot": "3.5", "q2_dot": "1.0", "q3_dot": "2.6", "unidad_velocidad": "rad/s"}}'
   },
   {
       "input": "Jacobian matrix for configuration 27°, 81°, 243° with angular velocities 2.3, 1.6, 2.9 radians per second",
       "output": '{"operacion": "jacobiano", "parametros": {"q1": "27", "q2": "81", "q3": "243", "unidad_angular": "grados", "q1_dot": "2.3", "q2_dot": "1.6", "q3_dot": "2.9", "unidad_velocidad": "rad/s"}}'
   },
    # Correccion 1
    {
        "input": "Calculate jacobian matrix with angles π/6, 5π/6, π/3 and angular velocities [2.8, 1.4, 3.7] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/6", "q2": "5*np.pi/6", "q3": "np.pi/3", "unidad_angular": "radianes", "q1_dot": "2.8", "q2_dot": "1.4", "q3_dot": "3.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian computation for joint angles 2π/7, 4π/7, 6π/7 with velocity vector [1.9, 3.2, 0.8] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2*np.pi/7", "q2": "4*np.pi/7", "q3": "6*np.pi/7", "unidad_angular": "radianes", "q1_dot": "1.9", "q2_dot": "3.2", "q3_dot": "0.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find robot jacobian with configuration π/8, 7π/8, 3π/4 and joint velocities [4.1, 2.3, 1.6] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/8", "q2": "7*np.pi/8", "q3": "3*np.pi/4", "unidad_angular": "radianes", "q1_dot": "4.1", "q2_dot": "2.3", "q3_dot": "1.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian analysis for angular positions π/12, 11π/12, 5π/6 using velocities [0.7, 2.9, 3.4] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/12", "q2": "11*np.pi/12", "q3": "5*np.pi/6", "unidad_angular": "radianes", "q1_dot": "0.7", "q2_dot": "2.9", "q3_dot": "3.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate manipulator jacobian for angles 3π/10, 7π/10, 9π/10 with speed array [3.6, 1.2, 2.8] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "3*np.pi/10", "q2": "7*np.pi/10", "q3": "9*np.pi/10", "unidad_angular": "radianes", "q1_dot": "3.6", "q2_dot": "1.2", "q3_dot": "2.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian matrix calculation with θ values π/15, 8π/15, 14π/15 and velocity list [2.1, 3.8, 1.5] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/15", "q2": "8*np.pi/15", "q3": "14*np.pi/15", "unidad_angular": "radianes", "q1_dot": "2.1", "q2_dot": "3.8", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Determine jacobian for robot joints at π/9, 4π/9, 8π/9 radians with rotational speeds [1.3, 2.7, 4.2] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/9", "q2": "4*np.pi/9", "q3": "8*np.pi/9", "unidad_angular": "radianes", "q1_dot": "1.3", "q2_dot": "2.7", "q3_dot": "4.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Robot jacobian evaluation at angles 5π/12, π/4, 7π/12 with angular velocity set [3.9, 0.6, 2.4] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "5*np.pi/12", "q2": "np.pi/4", "q3": "7*np.pi/12", "unidad_angular": "radianes", "q1_dot": "3.9", "q2_dot": "0.6", "q3_dot": "2.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Compute jacobian matrix for configuration 2π/11, 9π/11, 6π/11 using joint velocity vector [2.5, 4.0, 1.8] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2*np.pi/11", "q2": "9*np.pi/11", "q3": "6*np.pi/11", "unidad_angular": "radianes", "q1_dot": "2.5", "q2_dot": "4.0", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian derivation with motor angles π/16, 9π/16, 15π/16 and velocity parameters [1.7, 3.1, 2.2] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/16", "q2": "9*np.pi/16", "q3": "15*np.pi/16", "unidad_angular": "radianes", "q1_dot": "1.7", "q2_dot": "3.1", "q3_dot": "2.2", "unidad_velocidad": "rad/s"}}'
    },
    # Correccion 2
    {
        "input": "How fast can the robot move with angles 45°, 90°, 135° and speeds 2, 1.5, 3 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados", "q1_dot": "2", "q2_dot": "1.5", "q3_dot": "3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the robot speed when angles are 30°, 60°, 90° and moving at 1, 2, 1.5 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "30", "q2": "60", "q3": "90", "unidad_angular": "grados", "q1_dot": "1", "q2_dot": "2", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How quick can my robot be with these settings: 0.5, 1.0, 1.5 rad and speeds 2.5, 1.8, 3.2 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0.5", "q2": "1.0", "q3": "1.5", "unidad_angular": "radianes", "q1_dot": "2.5", "q2_dot": "1.8", "q3_dot": "3.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Can you tell me how fast the robot moves at 60°, 120°, 180° with speeds 1.2, 2.4, 1.8 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "60", "q2": "120", "q3": "180", "unidad_angular": "grados", "q1_dot": "1.2", "q2_dot": "2.4", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What speed can I get with robot at π/4, π/2, π rad and moving 1.5, 2.0, 2.5 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "np.pi", "unidad_angular": "radianes", "q1_dot": "1.5", "q2_dot": "2.0", "q3_dot": "2.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How fast does the robot go when positioned at 72°, 144°, 216° and rotating at 0.8, 1.6, 2.4 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados", "q1_dot": "0.8", "q2_dot": "1.6", "q3_dot": "2.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the maximum speed with angles 36°, 72°, 108° and motor speeds 3.0, 1.5, 2.8 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "36", "q2": "72", "q3": "108", "unidad_angular": "grados", "q1_dot": "3.0", "q2_dot": "1.5", "q3_dot": "2.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How quickly can the robot move when set to 1.2, 0.8, 1.5 rad with speeds 2, 1, 3 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.2", "q2": "0.8", "q3": "1.5", "unidad_angular": "radianes", "q1_dot": "2", "q2_dot": "1", "q3_dot": "3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Can you calculate how fast my robot goes with 25°, 50°, 75° and rotation speeds 1.7, 2.3, 1.9 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "25", "q2": "50", "q3": "75", "unidad_angular": "grados", "q1_dot": "1.7", "q2_dot": "2.3", "q3_dot": "1.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the robot's movement speed at π/6, π/3, π/2 radians with 2.1, 1.4, 2.7 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/6", "q2": "np.pi/3", "q3": "np.pi/2", "unidad_angular": "radianes", "q1_dot": "2.1", "q2_dot": "1.4", "q3_dot": "2.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How fast will the robot be moving with these joint angles: 15°, 30°, 45° and speeds 0.9, 1.8, 2.7 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "15", "q2": "30", "q3": "45", "unidad_angular": "grados", "q1_dot": "0.9", "q2_dot": "1.8", "q3_dot": "2.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Tell me the speed when robot is at 2π/3, π/4, 5π/6 rad and moving at 1.3, 2.6, 1.1 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2*np.pi/3", "q2": "np.pi/4", "q3": "5*np.pi/6", "unidad_angular": "radianes", "q1_dot": "1.3", "q2_dot": "2.6", "q3_dot": "1.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How quick is my robot when positioned at 54°, 108°, 162° with motor speeds 2.4, 1.7, 3.1 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "54", "q2": "108", "q3": "162", "unidad_angular": "grados", "q1_dot": "2.4", "q2_dot": "1.7", "q3_dot": "3.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the robot velocity with angles 0.7, 1.4, 2.1 rad and rotating at 1.6, 2.9, 0.8 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0.7", "q2": "1.4", "q3": "2.1", "unidad_angular": "radianes", "q1_dot": "1.6", "q2_dot": "2.9", "q3_dot": "0.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How fast does the arm move when at 81°, 162°, 243° and turning at speeds 3.5, 1.2, 2.0 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "81", "q2": "162", "q3": "243", "unidad_angular": "grados", "q1_dot": "3.5", "q2_dot": "1.2", "q3_dot": "2.0", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Can you show me the speed with robot set to π/8, 3π/8, 5π/8 and speeds 2.2, 1.9, 2.6 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/8", "q2": "3*np.pi/8", "q3": "5*np.pi/8", "unidad_angular": "radianes", "q1_dot": "2.2", "q2_dot": "1.9", "q3_dot": "2.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the movement speed at 42°, 84°, 126° with joint speeds 1.4, 2.8, 1.1 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "42", "q2": "84", "q3": "126", "unidad_angular": "grados", "q1_dot": "1.4", "q2_dot": "2.8", "q3_dot": "1.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How quickly will the robot respond with 1.8, 0.6, 2.4 rad angles and 0.7, 3.2, 1.5 rad/s speeds?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.8", "q2": "0.6", "q3": "2.4", "unidad_angular": "radianes", "q1_dot": "0.7", "q2_dot": "3.2", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Tell me how fast the robot can be with 63°, 126°, 189° and rotation rates 2.5, 1.0, 2.1 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "63", "q2": "126", "q3": "189", "unidad_angular": "grados", "q1_dot": "2.5", "q2_dot": "1.0", "q3_dot": "2.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What speed can I expect when robot is at 7π/12, π/12, 11π/12 and moving 1.8, 2.4, 1.2 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "7*np.pi/12", "q2": "np.pi/12", "q3": "11*np.pi/12", "unidad_angular": "radianes", "q1_dot": "1.8", "q2_dot": "2.4", "q3_dot": "1.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How fast is the robot moving with angles 27°, 54°, 81° and angular speeds 3.0, 1.6, 2.3 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "27", "q2": "54", "q3": "81", "unidad_angular": "grados", "q1_dot": "3.0", "q2_dot": "1.6", "q3_dot": "2.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Can you calculate the speed when positioned at 0.9, 1.8, 2.7 rad with speeds 2.0, 1.3, 2.9 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0.9", "q2": "1.8", "q3": "2.7", "unidad_angular": "radianes", "q1_dot": "2.0", "q2_dot": "1.3", "q3_dot": "2.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the robot's quickness with 48°, 96°, 144° and motor speeds 1.1, 2.7, 1.9 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "48", "q2": "96", "q3": "144", "unidad_angular": "grados", "q1_dot": "1.1", "q2_dot": "2.7", "q3_dot": "1.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How fast does it go when set to π/5, 2π/5, 3π/5 radians and turning 2.8, 1.4, 2.2 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/5", "q2": "2*np.pi/5", "q3": "3*np.pi/5", "unidad_angular": "radianes", "q1_dot": "2.8", "q2_dot": "1.4", "q3_dot": "2.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Tell me the velocity when robot angles are 33°, 66°, 99° and speeds are 1.9, 3.1, 0.6 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "33", "q2": "66", "q3": "99", "unidad_angular": "grados", "q1_dot": "1.9", "q2_dot": "3.1", "q3_dot": "0.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How quickly can the robot move when at 1.1, 2.2, 0.3 rad with rotation speeds 2.6, 1.7, 3.4 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.1", "q2": "2.2", "q3": "0.3", "unidad_angular": "radianes", "q1_dot": "2.6", "q2_dot": "1.7", "q3_dot": "3.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the speed at 57°, 114°, 171° with joint rotation rates 1.5, 2.2, 2.8 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "57", "q2": "114", "q3": "171", "unidad_angular": "grados", "q1_dot": "1.5", "q2_dot": "2.2", "q3_dot": "2.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "How fast will the arm be with 4π/9, π/9, 8π/9 radians and moving at 3.3, 1.8, 2.1 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "4*np.pi/9", "q2": "np.pi/9", "q3": "8*np.pi/9", "unidad_angular": "radianes", "q1_dot": "3.3", "q2_dot": "1.8", "q3_dot": "2.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Can you show me how quick the robot is at 21°, 42°, 63° with speeds 2.4, 3.0, 1.3 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "21", "q2": "42", "q3": "63", "unidad_angular": "grados", "q1_dot": "2.4", "q2_dot": "3.0", "q3_dot": "1.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the movement velocity when positioned at 0.4, 1.6, 2.8 rad and rotating at 1.2, 2.5, 1.9 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0.4", "q2": "1.6", "q3": "2.8", "unidad_angular": "radianes", "q1_dot": "1.2", "q2_dot": "2.5", "q3_dot": "1.9", "unidad_velocidad": "rad/s"}}'
    },
    # Correccion 3
    {
        "input": "Calculate the jacobian when all angles are 45° and all velocities are 1.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "45", "q2": "45", "q3": "45", "unidad_angular": "grados", "q1_dot": "1.5", "q2_dot": "1.5", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian matrix when all joints are at 30 degrees and all speeds are 2.0 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "30", "q2": "30", "q3": "30", "unidad_angular": "grados", "q1_dot": "2.0", "q2_dot": "2.0", "q3_dot": "2.0", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian for all angles set to 90° and all velocities at 0.8 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "90", "q2": "90", "q3": "90", "unidad_angular": "grados", "q1_dot": "0.8", "q2_dot": "0.8", "q3_dot": "0.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me the jacobian when all joint angles are 60 degrees and all angular speeds are 1.2 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "60", "q2": "60", "q3": "60", "unidad_angular": "grados", "q1_dot": "1.2", "q2_dot": "1.2", "q3_dot": "1.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian with all angles at 1.0 radians and all velocities at -0.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.0", "q2": "1.0", "q3": "1.0", "unidad_angular": "radianes", "q1_dot": "-0.5", "q2_dot": "-0.5", "q3_dot": "-0.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I need the jacobian when all joints are positioned at 120° and all speeds equal 2.5 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "120", "q2": "120", "q3": "120", "unidad_angular": "grados", "q1_dot": "2.5", "q2_dot": "2.5", "q3_dot": "2.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian if all angles are 0 degrees and all angular velocities are 3.0 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0", "q2": "0", "q3": "0", "unidad_angular": "grados", "q1_dot": "3.0", "q2_dot": "3.0", "q3_dot": "3.0", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find jacobian matrix when all joint angles equal π/2 radians and all velocities are 1.8 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/2", "q2": "np.pi/2", "q3": "np.pi/2", "unidad_angular": "radianes", "q1_dot": "1.8", "q2_dot": "1.8", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Give me the jacobian with all angles set to -45 degrees and all speeds at 0.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "-45", "q2": "-45", "q3": "-45", "unidad_angular": "grados", "q1_dot": "0.7", "q2_dot": "0.7", "q3_dot": "0.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show jacobian when all joint positions are 1.57 radians and all joint velocities are 2.1 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.57", "q2": "1.57", "q3": "1.57", "unidad_angular": "radianes", "q1_dot": "2.1", "q2_dot": "2.1", "q3_dot": "2.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian when all angles are 45° and velocities are 1.2, -0.8, 2.3 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "45", "q2": "45", "q3": "45", "unidad_angular": "grados", "q1_dot": "1.2", "q2_dot": "-0.8", "q3_dot": "2.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian matrix when all joints are at 30° and speeds are 0.5, 1.8, -1.1 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "30", "q2": "30", "q3": "30", "unidad_angular": "grados", "q1_dot": "0.5", "q2_dot": "1.8", "q3_dot": "-1.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian for all angles set to 90° and velocities at 2.7, 0.3, -1.9 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "90", "q2": "90", "q3": "90", "unidad_angular": "grados", "q1_dot": "2.7", "q2_dot": "0.3", "q3_dot": "-1.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me the jacobian when all joint angles are 60 degrees and angular speeds are -0.4, 2.1, 0.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "60", "q2": "60", "q3": "60", "unidad_angular": "grados", "q1_dot": "-0.4", "q2_dot": "2.1", "q3_dot": "0.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian with all angles at 1.5 radians and velocities 1.6, -2.4, 0.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.5", "q2": "1.5", "q3": "1.5", "unidad_angular": "radianes", "q1_dot": "1.6", "q2_dot": "-2.4", "q3_dot": "0.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I need the jacobian when all joints are positioned at 120° and speeds are 0.8, 1.3, -0.6 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "120", "q2": "120", "q3": "120", "unidad_angular": "grados", "q1_dot": "0.8", "q2_dot": "1.3", "q3_dot": "-0.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian if all angles are 0 degrees and angular velocities are 3.2, -1.7, 2.5 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0", "q2": "0", "q3": "0", "unidad_angular": "grados", "q1_dot": "3.2", "q2_dot": "-1.7", "q3_dot": "2.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find jacobian matrix when all joint angles equal π/4 radians and velocities are -1.0, 0.2, 1.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/4", "q2": "np.pi/4", "q3": "np.pi/4", "unidad_angular": "radianes", "q1_dot": "-1.0", "q2_dot": "0.2", "q3_dot": "1.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Give me the jacobian with all angles set to -30 degrees and speeds at 2.0, -0.1, 1.4 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "-30", "q2": "-30", "q3": "-30", "unidad_angular": "grados", "q1_dot": "2.0", "q2_dot": "-0.1", "q3_dot": "1.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show jacobian when all joint positions are 2.1 radians and joint velocities are 0.6, -2.8, 1.1 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2.1", "q2": "2.1", "q3": "2.1", "unidad_angular": "radianes", "q1_dot": "0.6", "q2_dot": "-2.8", "q3_dot": "1.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian when all angles are 75° and velocities are 1.7, 0.4, -2.3 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "75", "q2": "75", "q3": "75", "unidad_angular": "grados", "q1_dot": "1.7", "q2_dot": "0.4", "q3_dot": "-2.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian matrix when all joints are at 135 degrees and speeds are -0.9, 2.6, 0.1 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "135", "q2": "135", "q3": "135", "unidad_angular": "grados", "q1_dot": "-0.9", "q2_dot": "2.6", "q3_dot": "0.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian for all angles set to π/2 radians and velocities at 3.1, -1.5, 0.8 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/2", "q2": "np.pi/2", "q3": "np.pi/2", "unidad_angular": "radianes", "q1_dot": "3.1", "q2_dot": "-1.5", "q3_dot": "0.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me the jacobian when all joint angles are 15 degrees and angular speeds are 1.3, -0.7, 2.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "15", "q2": "15", "q3": "15", "unidad_angular": "grados", "q1_dot": "1.3", "q2_dot": "-0.7", "q3_dot": "2.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian with all angles at 0.8 radians and velocities 2.4, 1.0, -1.6 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0.8", "q2": "0.8", "q3": "0.8", "unidad_angular": "radianes", "q1_dot": "2.4", "q2_dot": "1.0", "q3_dot": "-1.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian when angles are 20°, 45°, 90° and all velocities are 1.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "20", "q2": "45", "q3": "90", "unidad_angular": "grados", "q1_dot": "1.5", "q2_dot": "1.5", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian matrix when joint angles are 30°, -60°, 120° and all speeds are 2.3 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "30", "q2": "-60", "q3": "120", "unidad_angular": "grados", "q1_dot": "2.3", "q2_dot": "2.3", "q3_dot": "2.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian for angles 75°, 135°, 0° and all velocities set to 0.8 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "75", "q2": "135", "q3": "0", "unidad_angular": "grados", "q1_dot": "0.8", "q2_dot": "0.8", "q3_dot": "0.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me the jacobian when joint angles are 1.2, 0.5, 2.8 radians and all angular speeds are 1.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.2", "q2": "0.5", "q3": "2.8", "unidad_angular": "radianes", "q1_dot": "1.9", "q2_dot": "1.9", "q3_dot": "1.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian with angles 45°, 15°, -30° and all velocities at 2.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "45", "q2": "15", "q3": "-30", "unidad_angular": "grados", "q1_dot": "2.7", "q2_dot": "2.7", "q3_dot": "2.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I need the jacobian when joints are positioned at 60°, 180°, 270° and all speeds equal 0.4 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "60", "q2": "180", "q3": "270", "unidad_angular": "grados", "q1_dot": "0.4", "q2_dot": "0.4", "q3_dot": "0.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian if angles are π/6, π/3, π/2 radians and all angular velocities are 3.1 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/6", "q2": "np.pi/3", "q3": "np.pi/2", "unidad_angular": "radianes", "q1_dot": "3.1", "q2_dot": "3.1", "q3_dot": "3.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find jacobian matrix when joint angles are 105°, -45°, 225° and all velocities are 1.6 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "105", "q2": "-45", "q3": "225", "unidad_angular": "grados", "q1_dot": "1.6", "q2_dot": "1.6", "q3_dot": "1.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Give me the jacobian with angles 0°, 90°, 180° and all speeds at 2.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0", "q2": "90", "q3": "180", "unidad_angular": "grados", "q1_dot": "2.5", "q2_dot": "2.5", "q3_dot": "2.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show jacobian when joint positions are 0.7, -1.4, 2.1 radians and all joint velocities are 0.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0.7", "q2": "-1.4", "q3": "2.1", "unidad_angular": "radianes", "q1_dot": "0.9", "q2_dot": "0.9", "q3_dot": "0.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian when angles are 165°, 30°, 75° and all velocities are 1.8 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "165", "q2": "30", "q3": "75", "unidad_angular": "grados", "q1_dot": "1.8", "q2_dot": "1.8", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian matrix when joint angles are 2.5, 0.3, 1.7 radians and all speeds are 2.2 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2.5", "q2": "0.3", "q3": "1.7", "unidad_angular": "radianes", "q1_dot": "2.2", "q2_dot": "2.2", "q3_dot": "2.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian for angles 315°, 210°, 150° and all velocities set to 0.6 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "315", "q2": "210", "q3": "150", "unidad_angular": "grados", "q1_dot": "0.6", "q2_dot": "0.6", "q3_dot": "0.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me the jacobian when joint angles are π/4, 3π/4, π radians and all angular speeds are 1.3 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/4", "q2": "3*np.pi/4", "q3": "np.pi", "unidad_angular": "radianes", "q1_dot": "1.3", "q2_dot": "1.3", "q3_dot": "1.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian with angles 240°, 300°, 36° and all velocities at 2.9 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "240", "q2": "300", "q3": "36", "unidad_angular": "grados", "q1_dot": "2.9", "q2_dot": "2.9", "q3_dot": "2.9", "unidad_velocidad": "rad/s"}}'
    }
]

jacobiano_NoValues = [
    {
        "input": "Calculate the jacobian with velocities 2.1, 1.8, 3.2 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.1", "q2_dot": "1.8", "q3_dot": "3.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I need the jacobian matrix with angular velocities 1.5, 2.7, 0.9 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.5", "q2_dot": "2.7", "q3_dot": "0.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Compute jacobian using joint velocities 3.4, 1.2, 2.8 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "3.4", "q2_dot": "1.2", "q3_dot": "2.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian with rotational speeds 0.8, 3.1, 1.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.8", "q2_dot": "3.1", "q3_dot": "1.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian calculation with velocity vector [2.5, 1.9, 3.6] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.5", "q2_dot": "1.9", "q3_dot": "3.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian when motor speeds are 1.3, 2.4, 3.8 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.3", "q2_dot": "2.4", "q3_dot": "3.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Robot jacobian with angular velocities dq = 4.1, 0.7, 2.2 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "4.1", "q2_dot": "0.7", "q3_dot": "2.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate manipulator jacobian using speeds 1.6, 3.3, 2.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.6", "q2_dot": "3.3", "q3_dot": "2.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I want the jacobian with joint velocities 2.8, 1.1, 3.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.8", "q2_dot": "1.1", "q3_dot": "3.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Determine jacobian matrix for velocities 0.5, 2.6, 1.4 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.5", "q2_dot": "2.6", "q3_dot": "1.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me the jacobian with velocity array [3.2, 2.0, 1.8] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "3.2", "q2_dot": "2.0", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian computation with q_dot values 1.9, 3.5, 0.6 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.9", "q2_dot": "3.5", "q3_dot": "0.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Get the system jacobian using angular speeds 2.7, 1.3, 4.0 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.7", "q2_dot": "1.3", "q3_dot": "4.0", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian matrix with rotational velocities 1.0, 2.9, 3.4 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.0", "q2_dot": "2.9", "q3_dot": "3.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I need jacobian analysis with velocity parameters 3.8, 0.9, 2.3 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "3.8", "q2_dot": "0.9", "q3_dot": "2.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian derivation using joint speeds 1.7, 2.1, 3.9 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.7", "q2_dot": "2.1", "q3_dot": "3.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What is the jacobian when velocities are 2.4, 3.6, 1.2 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.4", "q2_dot": "3.6", "q3_dot": "1.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate robot jacobian with angular velocity set [0.8, 1.5, 2.7] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.8", "q2_dot": "1.5", "q3_dot": "2.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find jacobian matrix using speed vector 3.1, 2.6, 1.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "3.1", "q2_dot": "2.6", "q3_dot": "1.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Compute the jacobian with motor velocities 1.4, 3.7, 0.3 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.4", "q2_dot": "3.7", "q3_dot": "0.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian evaluation with velocity list [2.2, 1.6, 3.0] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.2", "q2_dot": "1.6", "q3_dot": "3.0", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Determine the jacobian using rotational speeds 4.3, 2.8, 1.1 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "4.3", "q2_dot": "2.8", "q3_dot": "1.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show jacobian calculation with joint velocities 0.7, 2.5, 3.8 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.7", "q2_dot": "2.5", "q3_dot": "3.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I want the jacobian matrix using angular speeds 1.8, 4.1, 2.4 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.8", "q2_dot": "4.1", "q3_dot": "2.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate manipulator jacobian with velocity array [3.5, 1.7, 0.9] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "3.5", "q2_dot": "1.7", "q3_dot": "0.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian matrix computation using speeds 2.9, 3.2, 1.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.9", "q2_dot": "3.2", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Get the robot jacobian with rotational velocities 1.3, 0.6, 2.8 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.3", "q2_dot": "0.6", "q3_dot": "2.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find jacobian using motor velocity vector [4.0, 2.3, 1.6] rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "4.0", "q2_dot": "2.3", "q3_dot": "1.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Jacobian analysis with joint speed parameters 0.4, 3.6, 2.1 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.4", "q2_dot": "3.6", "q3_dot": "2.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the system jacobian using angular velocities 2.7, 1.0, 3.3 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.7", "q2_dot": "1.0", "q3_dot": "3.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian with q1=45°, q2=90°, q3=135°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "45", "q2": "90", "q3": "135", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "I need the jacobian matrix for angles 30, 60, 120 degrees",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "30", "q2": "60", "q3": "120", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Compute jacobian using joint configuration π/4, π/2, 3π/4",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/4", "q2": "np.pi/2", "q3": "3*np.pi/4", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Find the jacobian with robot angles 72°, 144°, 216°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "72", "q2": "144", "q3": "216", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Jacobian calculation for configuration [π/6, 5π/6, π/3]",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/6", "q2": "5*np.pi/6", "q3": "np.pi/3", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "What's the jacobian when motor angles are 15°, 75°, 165°?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "15", "q2": "75", "q3": "165", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Robot jacobian for angular positions θ1=π/8, θ2=3π/8, θ3=5π/8",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/8", "q2": "3*np.pi/8", "q3": "5*np.pi/8", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Calculate manipulator jacobian using angles 105°, 195°, 285°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "105", "q2": "195", "q3": "285", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "I want the jacobian with joint angles 2π/3, π/12, 7π/12",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2*np.pi/3", "q2": "np.pi/12", "q3": "7*np.pi/12", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Determine jacobian matrix for configuration 36°, 108°, 252°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "36", "q2": "108", "q3": "252", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Show me the jacobian with angle array [π/12, 11π/12, 5π/6]",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/12", "q2": "11*np.pi/12", "q3": "5*np.pi/6", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Jacobian computation for q values 84°, 168°, 252°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "84", "q2": "168", "q3": "252", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Get the system jacobian using angular configuration 4π/3, 5π/3, π/3",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "4*np.pi/3", "q2": "5*np.pi/3", "q3": "np.pi/3", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Calculate the jacobian matrix with joint positions 51°, 102°, 204°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "51", "q2": "102", "q3": "204", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "I need jacobian analysis for angles π/10, 9π/10, 2π/5",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/10", "q2": "9*np.pi/10", "q3": "2*np.pi/5", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Jacobian derivation using joint angles 63°, 126°, 189°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "63", "q2": "126", "q3": "189", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "What is the jacobian when theta values are 7π/8, π/16, 15π/16?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "7*np.pi/8", "q2": "np.pi/16", "q3": "15*np.pi/16", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Calculate robot jacobian with angular configuration [27°, 81°, 243°]",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "27", "q2": "81", "q3": "243", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Find jacobian matrix using position vector 11π/12, π/24, 13π/12",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "11*np.pi/12", "q2": "np.pi/24", "q3": "13*np.pi/12", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Compute the jacobian with motor positions 39°, 78°, 156°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "39", "q2": "78", "q3": "156", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Jacobian evaluation for angle configuration 3π/16, 9π/16, 21π/16",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "3*np.pi/16", "q2": "9*np.pi/16", "q3": "21*np.pi/16", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Determine the jacobian using joint positions 48°, 96°, 192°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "48", "q2": "96", "q3": "192", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Show jacobian calculation for angles π/20, 19π/20, 3π/5",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/20", "q2": "19*np.pi/20", "q3": "3*np.pi/5", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "I want the jacobian matrix using angular positions 21°, 42°, 84°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "21", "q2": "42", "q3": "84", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Calculate manipulator jacobian for configuration 2π/11, 9π/11, 6π/11",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2*np.pi/11", "q2": "9*np.pi/11", "q3": "6*np.pi/11", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Jacobian matrix computation using angles 57°, 114°, 228°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "57", "q2": "114", "q3": "228", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Get the robot jacobian with joint configuration π/16, 9π/16, 15π/16",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/16", "q2": "9*np.pi/16", "q3": "15*np.pi/16", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Find jacobian using motor angle vector [33°, 66°, 132°]",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "33", "q2": "66", "q3": "132", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Jacobian analysis for joint position parameters 2π/7, 4π/7, 6π/7",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2*np.pi/7", "q2": "4*np.pi/7", "q3": "6*np.pi/7", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Calculate the system jacobian using angular positions 69°, 138°, 276°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "69", "q2": "138", "q3": "276", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    # Correccion 3
    {
        "input": "What's the jacobian when joint velocities are 1.2, -0.5, 0.8 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.2", "q2_dot": "-0.5", "q3_dot": "0.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian with velocities 2.1, 0.9, -1.3 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.1", "q2_dot": "0.9", "q3_dot": "-1.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me the jacobian for joint speeds of 0.6, 1.8, -0.4 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.6", "q2_dot": "1.8", "q3_dot": "-0.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I need the jacobian when all joint velocities are 1.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.5", "q2_dot": "1.5", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian with angular speeds 0.3, -2.1, 1.7 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.3", "q2_dot": "-2.1", "q3_dot": "1.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian for velocities -0.8, 2.5, 0.1 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "-0.8", "q2_dot": "2.5", "q3_dot": "0.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian matrix when joint speeds are 1.9, 0.7, -1.1 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.9", "q2_dot": "0.7", "q3_dot": "-1.1", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Give me the jacobian analysis for velocities 0.4, -1.6, 2.3 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.4", "q2_dot": "-1.6", "q3_dot": "2.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show jacobian when all speeds are 0.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.9", "q2_dot": "0.9", "q3_dot": "0.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian with joint velocities -1.4, 0.2, 1.8 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "-1.4", "q2_dot": "0.2", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I want the jacobian for angular velocities 2.7, -0.3, 0.6 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.7", "q2_dot": "-0.3", "q3_dot": "0.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find jacobian matrix for speeds 1.1, 2.4, -0.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.1", "q2_dot": "2.4", "q3_dot": "-0.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian when velocities are 0.0, 1.3, -2.2 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.0", "q2_dot": "1.3", "q3_dot": "-2.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Compute jacobian with joint speeds -0.1, -1.9, 1.4 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "-0.1", "q2_dot": "-1.9", "q3_dot": "1.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me jacobian for angular speeds 3.0, 0.5, -1.0 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "3.0", "q2_dot": "0.5", "q3_dot": "-1.0", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian when all joint velocities are -0.6 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "-0.6", "q2_dot": "-0.6", "q3_dot": "-0.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I need jacobian analysis with velocities 1.0, -2.8, 0.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.0", "q2_dot": "-2.8", "q3_dot": "0.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian for speeds 2.2, 1.6, -0.9 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.2", "q2_dot": "1.6", "q3_dot": "-0.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian matrix for joint velocities -1.7, 0.8, 2.9 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "-1.7", "q2_dot": "0.8", "q3_dot": "2.9", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Give me jacobian when angular speeds are 0.7, -1.2, 1.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.7", "q2_dot": "-1.2", "q3_dot": "1.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show jacobian calculation for velocities 2.6, 0.4, -1.8 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.6", "q2_dot": "0.4", "q3_dot": "-1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian with all speeds at 2.0 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.0", "q2_dot": "2.0", "q3_dot": "2.0", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I want the jacobian for joint velocities -0.5, 3.1, 0.3 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "-0.5", "q2_dot": "3.1", "q3_dot": "0.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find jacobian matrix when speeds are 1.3, -0.4, 2.7 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.3", "q2_dot": "-0.4", "q3_dot": "2.7", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian when all angular velocities are 1.8 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.8", "q2_dot": "1.8", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate the jacobian when all angles are 30 degrees",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "30", "q2": "30", "q3": "30", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "What's the jacobian matrix when all joints are at 45°?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "45", "q2": "45", "q3": "45", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Find the jacobian for all angles set to 0 degrees",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "0", "q2": "0", "q3": "0", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Show me the jacobian when all joint angles are 90°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "90", "q2": "90", "q3": "90", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Calculate jacobian with all angles at 1.5 radians",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "1.5", "q2": "1.5", "q3": "1.5", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "I need the jacobian when all joints are positioned at 60 degrees",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "60", "q2": "60", "q3": "60", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "What's the jacobian if all angles are π/4 radians?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "np.pi/4", "q2": "np.pi/4", "q3": "np.pi/4", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Find jacobian matrix when all joint angles equal 120°",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "120", "q2": "120", "q3": "120", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Give me the jacobian with all angles set to -30 degrees",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "-30", "q2": "-30", "q3": "-30", "unidad_angular": "grados", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Show jacobian when all joint positions are 2.1 radians",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "2.1", "q2": "2.1", "q3": "2.1", "unidad_angular": "radianes", "q1_dot": "", "q2_dot": "", "q3_dot": "", "unidad_velocidad": ""}}'
    },
    {
        "input": "Calculate the jacobian when all velocities are 1.2 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.2", "q2_dot": "1.2", "q3_dot": "1.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian matrix when all speeds are 0.8 radians per second?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.8", "q2_dot": "0.8", "q3_dot": "0.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find the jacobian for all joint velocities set to 2.5 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.5", "q2_dot": "2.5", "q3_dot": "2.5", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show me the jacobian when all angular speeds are 0.6 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.6", "q2_dot": "0.6", "q3_dot": "0.6", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Calculate jacobian with all velocities at -1.3 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "-1.3", "q2_dot": "-1.3", "q3_dot": "-1.3", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "I need the jacobian when all joint speeds equal 3.0 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "3.0", "q2_dot": "3.0", "q3_dot": "3.0", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "What's the jacobian if all angular velocities are 1.8 rad/s?",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "1.8", "q2_dot": "1.8", "q3_dot": "1.8", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Find jacobian matrix when all speeds are 0.4 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "0.4", "q2_dot": "0.4", "q3_dot": "0.4", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Give me the jacobian with all velocities set to 2.2 rad/s",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "2.2", "q2_dot": "2.2", "q3_dot": "2.2", "unidad_velocidad": "rad/s"}}'
    },
    {
        "input": "Show jacobian when all joint velocities are -0.9 radians per second",
        "output": '{"operacion": "jacobiano", "parametros": {"q1": "", "q2": "", "q3": "", "unidad_angular": "", "q1_dot": "-0.9", "q2_dot": "-0.9", "q3_dot": "-0.9", "unidad_velocidad": "rad/s"}}'
    }
]

jacobiano_train = jacobiano_train + jacobiano_NoValues