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
   }
]