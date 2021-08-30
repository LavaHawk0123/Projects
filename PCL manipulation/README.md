
<h1>Task: Manipulating a point cloud to filter the PointCloud and cluster objects</h1>
Simulation Software: Gazebo and ROSCPP
Framework: ROS
<ol><li>Filtering
<li> Segmentation
<li>Ground Plane Elimination
<li>Clustering
</ol>

Algorithms used : 
<ol><li>Filtering: FVoxel Filtering using Downs Sampling
<li> Ground Plane Elimination: SAC Segmentation
<li>Clustering : Colour-Based reigon growing segmentation
</ol>

Sensors used:
1) Kinect RGB Depth Camera

<h1> To run the code</h1>
Pull the mybot_pcl folder into the src folder of your workspace. Change the project(mybot_pcl) in Line 2 of CMakeList file to project( {insert your workspace name} ).
  
### Open the terminal and run
```
catkin build
```

### Then run:
```
rosrun {insert your workspace name} rgbgrowing
```

### In a new terminal run:
```
rosrun {insert your workspace name} rgbgrowing
```
### In a new terminal run Rviz and visualize the pointcloud:
```
rviz
```

<h2> Testing Environment Screenshot: </h2>
<h4>Original DepthCloud :  </h4>
<img src="https://github.com/MRM-AI-TP-2022/Aditya-Arun-Iyer-MRM/blob/062f30e8d4cb169f2936ac7005c65538dec69b3e/PCL%20manipulation/pcl%20task%20images/pcl_normal.png">

<h4> Clustering 3 objects : </h4>
<img src="https://github.com/MRM-AI-TP-2022/Aditya-Arun-Iyer-MRM/blob/062f30e8d4cb169f2936ac7005c65538dec69b3e/PCL%20manipulation/pcl%20task%20images/3_object_clustered.png">

<h4> Clustering 5 objects : </h4>
<img src="https://github.com/MRM-AI-TP-2022/Aditya-Arun-Iyer-MRM/blob/062f30e8d4cb169f2936ac7005c65538dec69b3e/PCL%20manipulation/pcl%20task%20images/5_obj_clustering.png">

<h4>Ground Plane Elimination: </h4>
<img src="https://github.com/MRM-AI-TP-2022/Aditya-Arun-Iyer-MRM/blob/062f30e8d4cb169f2936ac7005c65538dec69b3e/PCL%20manipulation/pcl%20task%20images/Ground_plane_elimination_pcl.png">

<h4>Voxel Filtering Output :  </h4>
<img src="https://github.com/MRM-AI-TP-2022/Aditya-Arun-Iyer-MRM/blob/062f30e8d4cb169f2936ac7005c65538dec69b3e/PCL%20manipulation/pcl%20task%20images/filtered_pcl.png">


<h4>Objects in close proximity :  </h4>
<img src="https://github.com/MRM-AI-TP-2022/Aditya-Arun-Iyer-MRM/blob/062f30e8d4cb169f2936ac7005c65538dec69b3e/PCL%20manipulation/pcl%20task%20images/close_object_pcl.png">

