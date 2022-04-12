# Projects by Aditya Arun Iyer

<a href = "https://github.com/LavaHawk0123/Projects/tree/main/Obstacle%20Avoidence%20in%20a%204%20wheeled%20bot"><h2>1) Autonomous Traversal of a 4 wheel bot using PID:</h2></a>
<h2>Task: Implementation of the autonomous traversal of the 4 wheel bot from one GPS Coordinate to another using a PID controller and Differential Drive system implementing obstacle avoidance.</h2>
Simulation Software: Gazebo
Framework: ROS & Python API
Dependencies used:
<ol><li>pyproj
<li>math
<li>Numpy
<li>time
<li>rospy</ol>

Sensors used:
1) Lidar (LaserScan values)
2) Ultrasonic Sensor
3) Imu 
4) GPS

<h3>
  Playlist Link: https://youtube.com/playlist?list=PLLzKWW1SmGsuiLZpaoPWihaU0b5HiueT1</h3>
  <h3>
  Basic ALgorithm Test : https://youtu.be/SZFT8iJmO-E
<br>
Extreme Algorithm Test : https://youtu.be/oQ7MTeyXL9Y
</h3>
<h3> Source Code : <a href = "https://github.com/LavaHawk0123/Projects/tree/main/Autonomous%20Traversal%20Of%20Rover%20in%20Gazebo"> CLICK HERE </a></h3>
<h2> Testing Environment Screenshot: </h2>

<img src="https://github.com/MRM-AI-TP-2022/Aditya-Arun-Iyer-MRM/blob/a7070f3d27a5416163236ecb25a2efb87e0d5830/Images/Map.png">
<br>
<h1>2)<a href = "https://github.com/LavaHawk0123/Projects/tree/main/UR5_Inverse_Kinematics_Package"> Implementing Inverse Kinematics on the UR5 using MoveIt framework </a></h1>

Simulation Software: Gazebo
Framework: ROS
Dependencies used:
<ol><li>MoveIt
<li>math
<li>Numpy
<li>time
<li>rospy</ol>

Sensors used:
1) Stereocamera 
2) Imu
3) UR5 Robotic Arm

<h3> Simulation output</h3>
<img src="https://github.com/LavaHawk0123/Projects/blob/main/UR5_Inverse_Kinematics_Package/ur5_sim.gif">

<h3> Video for testbench - https://youtu.be/IWIqN_8i9kc </h3>
<h3> Source Code : <a href = "https://github.com/LavaHawk0123/Projects/tree/main/UR5_Inverse_Kinematics_Package"> CLICK HERE </a></h3>
<h1>
3) Online Certificate Courses:</h1>
Courses Completed: 
<ol><li> <a href = "https://github.com/LavaHawk0123/Projects/tree/main/DeeplearningAI%20specialization%20-%20Neural%20networks">DeepLearning AI Specialisation on Machine Learning and CNN's using Python</a>
<li> <a href = "https://www.coursera.org/account/accomplishments/certificate/UNQXYUQHLTWC">Python specialisation by Google</a>
<li> <a href = "https://www.coursera.org/account/accomplishments/certificate/7493RSBYUPP6">Python for Data Science and AI by IBM</a>
<li><a href = "https://www.coursera.org/account/accomplishments/certificate/CGPZK25EW7VZ"> Mathematics for ML Linear Algebra </a>
<li><a href="https://www.coursera.org/account/accomplishments/certificate/Z5UF2LGKHVBG"> C for Everyone: Programming Fundamentals</a>
<li> An intorduction to particle physics by the University of Geneva, Switzerland
<li> Astrophysics - Exploring Exoplanets by HarvardX
<li> The evolving Universe and Science of the Universe by Caltech
<li> Contributed to IBM's Developer Skill's network</ol>
<h1>
4) <a href="https://github.com/LavaHawk0123/Projects/tree/main/Mathematics_Python"> Famous Mathematical implimentations in Python: </a></h1>
<h2><a href = "https://github.com/LavaHawk0123/Projects/tree/main/Finding%20a%20root%20of%20an%20equation%20using%20false%20positioning%20method"> Estimating roots of an equation using false postion method </a></h2>

```
git pull https://github.com/LavaHawk0123/Projects.git
cd Finding a root of an equation using false positioning method
python FalsePosition-final.py
```
<h2><a href = "https://github.com/LavaHawk0123/Projects/blob/main/Mathematics_Python/Bisection.py"> Estimating root of an equation by Bisection method</a></h2>

```
git pull https://github.com/LavaHawk0123/Projects.git
cd Mathematics_python
python Bisection.py
```

<h2><a href=https://github.com/LavaHawk0123/Projects/blob/main/Mathematics_Python/Elementary_Transform.py""> Elementary transformation of a matrix</a></h2>

```
git pull https://github.com/LavaHawk0123/Projects.git
cd Mathematics_python
python Elementary_transform.py
```
<h1>
5) ROS Simulations(Gazebo) and network applications</h1>
<h2> <a href = "https://github.com/LavaHawk0123/Projects/tree/main/IMU_Plugin_ROS"> Streaming Euler,Quartonian angles, Gyroscope and Magnetometer values</a></h2>
After installing ROS and configuring your work environement from: http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment

run the following commands in /  :

```
git pull https://github.com/LavaHawk0123/Projects.git
catkin_create_pkg IMU_stream
cd IMU_stream/src
mv IMU_Plugin_ROS/client_imu.py IMU_stream/src
mv IMU_Plugin_ROS/server_imu.py IMU_stream/src
catkin_make
```
Then to run the node:
```
cd IMU_stream
rosrun IMU_plugin_ROS server_imu.py
rosrun IMU_plugin_ROS client_imu.py
```

<h1>6)Machine Learning : Linear and Logistic regression</h1>
<ol>
<li><h2> <a href="https://github.com/LavaHawk0123/Projects/blob/main/Linear%20Regression%20Task%201.pdf"> Linear Regression : Finding the estimated cost of houses</a> </h2>
<li><h2><a href = "https://github.com/LavaHawk0123/Projects/blob/main/Logistic%20Regression.pdf"> Logistic Regression : Estimating the probability of a passenger chosen randomly from the titanic, died </a></h2>
  <li><h2> <a href="https://github.com/LavaHawk0123/Projects/blob/main/Economic_Dashboard.pdf"> Economic Dashboard using Pandas and Python </a></h2></ol>


<h1>5)Ball Tracking using OpenCV library and Python</h1>
<h3> Source Code : <a href = "https://github.com/LavaHawk0123/Projects/tree/main/Ball_Tracking_OpenCV"> CLICK HERE </a></h3>
<h2>Link : https://youtu.be/PqRq1DwuKRk </h2>

