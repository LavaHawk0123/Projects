#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/filters/passthrough.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_types.h>
#include <pcl/filters/extract_indices.h>
#include <pcl/sample_consensus/method_types.h>
#include <pcl/sample_consensus/model_types.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/features/normal_3d.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/search/search.h>
#include <pcl/search/kdtree.h>
#include <pcl/visualization/cloud_viewer.h>
#include <pcl/filters/filter_indices.h>
#include <pcl/segmentation/region_growing_rgb.h>
#include <pcl/io/pcd_io.h>
#include <pcl/ml/kmeans.h>
#include <pcl/filters/filter_indices.h>
#include <pcl/segmentation/region_growing.h>
#include <pcl/features/normal_3d.h>
#include <pcl/segmentation/extract_clusters.h>

ros::Publisher pub,pub_filtered,pub_gpe,pub_colored; //Global Publishers Declared

void 
cloud_callback (const sensor_msgs::PointCloud2ConstPtr& cloud_msg)
{

  //Cloud variable Declerations
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGB>), cloud_f (new pcl::PointCloud<pcl::PointXYZRGB>);
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_filtered (new pcl::PointCloud<pcl::PointXYZRGB>);
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_filtered_prime (new pcl::PointCloud<pcl::PointXYZRGB>);
  pcl::fromROSMsg(*cloud_msg, *cloud);
  //Implimenting Voxel Filter
  pcl::VoxelGrid<pcl::PointXYZRGB> vox;
  vox.setInputCloud (cloud);
  vox.setLeafSize (0.01, 0.01, 0.01);
  vox.filter (*cloud);
  pub_filtered.publish (*cloud);

  //Ground Plane elimination using SAC Segmentation
  pcl::SACSegmentation<pcl::PointXYZRGB> segment_gpe;
  pcl::PointIndices::Ptr ground_indices(new pcl::PointIndices);
  pcl::ModelCoefficients::Ptr coefficients (new pcl::ModelCoefficients);
  segment_gpe.setOptimizeCoefficients(true);
  segment_gpe.setModelType(pcl::SACMODEL_PLANE);
  segment_gpe.setMethodType(pcl::SAC_RANSAC);
  segment_gpe.setDistanceThreshold(0.05);
  segment_gpe.setInputCloud(cloud);
  segment_gpe.segment(*ground_indices, *coefficients);
  pcl::ExtractIndices<pcl::PointXYZRGB> extract;
  extract.setInputCloud(cloud);
  extract.setIndices(ground_indices);
  extract.setNegative(true);
  extract.filter(*cloud);
  pub_gpe.publish(*cloud);


}

int main (int argc, char** argv)
{
  ros::init (argc,argv,"pcl_tutorial");
  ros::NodeHandle nh;
  ROS_DEBUG("Reached Main");
  pub = nh.advertise<sensor_msgs::PointCloud2> ("pcl/points", 1);
  pub_filtered = nh.advertise<sensor_msgs::PointCloud2> ("pcl/points/filtered", 1);
  pub_gpe = nh.advertise<sensor_msgs::PointCloud2> ("pcl/points/gpe", 1);
  ros::Subscriber sub = nh.subscribe<sensor_msgs::PointCloud2> ("camera/depth/points", 1, cloud_callback);
  ROS_INFO("Obtained PointCloud Data");
  ros::spin ();
  return(0);
}

