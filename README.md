# Projects by Aditya Arun Iyer

<h2>1) Autonomous Traversal of a 4 wheel bot:</h2>
<h2>Task: Implementation of the autonomous traversal of the 4 wheel bot from one GPS Coordinate to another implementing obstacle avoidance.</h2>
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

<h2> Testing Environment Screenshot: </h2>

<img src="https://github.com/MRM-AI-TP-2022/Aditya-Arun-Iyer-MRM/blob/a7070f3d27a5416163236ecb25a2efb87e0d5830/Images/Map.png">

<h1>
2) Online Certificate Courses:</h1>
Courses Completed: 
<ol><li> DeepLearning AI Specialisation on Machine Learning and CNN's using Python
<li> Python specialisation by Google
<li> Python forr Data Science and AI by IBM
<li> An intorduction to particle physics by the University of Geneva, Switzerland
<li> Astrophysics - Exploring Exoplanets by HarvardX
<li> The evolving Universe and Science of the Universe by Caltech
<li> Contributed to IBM's Developer Skill's network</ol>
<h1>
3) Mathematical implimentation of Python:</h1>
<h2> Estimating roots of an equation using false postion method</h2>

```
git pull https://github.com/LavaHawk0123/Projects.git
cd Finding a root of an equation using false positioning method
python FalsePosition-final.py
```
<h2> Estimating root of an equation by Bisection method</h2>

```
git pull https://github.com/LavaHawk0123/Projects.git
cd Mathematics_python
python Bisection.py
```

<h2> Elementary transformation of a matrix</h2>

```
git pull https://github.com/LavaHawk0123/Projects.git
cd Mathematics_python
python Elementary_transform.py
```
<h1>
4) ROS Simulations(Gazebo) and network applications</h1>
<h2> Streaming Euler,Quartonian angles, Gyroscope and Magnetometer values</h2>
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

<h1>5)Machine Learning : Linear and Logistic regression</h1>
<ol>
<li><h2> Linear Regression : Finding the estimated cost of houses</h2>
<li><h2> Logistic Regression : Estimating the probability of a passenger chosen died</h2>
  <li><h2> Economic Dashboard using Pandas and Python</h2></ol>


<h1>5)Ball Tracking using OpenCV library and Python</h1>
<h2>Link : https://youtu.be/PqRq1DwuKRk </h2>

