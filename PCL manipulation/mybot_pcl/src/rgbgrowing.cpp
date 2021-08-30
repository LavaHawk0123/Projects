#include <ros/ros.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/filters/passthrough.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/point_types.h>
#include <pcl/io/pcd_io.h>
#include <pcl/filters/extract_indices.h>
#include <iostream>
#include <thread>
#include <vector>
#include <pcl/point_types.h>
#include <pcl/io/pcd_io.h>
#include <pcl/search/search.h>
#include <pcl/search/kdtree.h>
#include <pcl/visualization/cloud_viewer.h>
#include <pcl/filters/filter_indices.h>
#include <pcl/segmentation/region_growing_rgb.h>

ros::Publisher pub_clust; //Global Publishers Declared

void 
cloud_clustering_rgb (const sensor_msgs::PointCloud2ConstPtr& cloud_msg)
{

  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGB>);
  pcl::fromROSMsg(*cloud_msg, *cloud);

 pcl::search::Search <pcl::PointXYZRGB>::Ptr tree (new pcl::search::KdTree<pcl::PointXYZRGB>);

  pcl::IndicesPtr indices (new std::vector <int>);
  pcl::removeNaNFromPointCloud (*cloud, *indices);

  pcl::RegionGrowingRGB<pcl::PointXYZRGB> clust;
  clust.setInputCloud (cloud);
  clust.setIndices (indices);
  clust.setSearchMethod (tree);
  clust.setDistanceThreshold (10);
  clust.setPointColorThreshold (6);
  clust.setRegionColorThreshold (1);
  clust.setMinClusterSize (600);

  std::vector <pcl::PointIndices> cluster_indices;
  clust.extract (cluster_indices);

int j = 0;
int r,g,b;
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_cluster (new pcl::PointCloud<pcl::PointXYZRGB>);
  for (std::vector<pcl::PointIndices>::const_iterator iter = cluster_indices.begin (); iter != cluster_indices.end (); ++iter)
  {
     r = 255*(1024*rand() / (RAND_MAX + 1.0f));
     g = 255*(1024*rand() / (RAND_MAX + 1.0f));
     b = 255*(1024*rand() / (RAND_MAX + 1.0f));
    for (std::vector<int>::const_iterator point_iter = iter->indices.begin (); point_iter != iter->indices.end (); ++point_iter)
{ //*
    (*cloud)[*point_iter].r = r;
    (*cloud)[*point_iter].g = g;
    (*cloud)[*point_iter].b = b;
    cloud_cluster->push_back ((*cloud)[*point_iter]);
}  
    cloud_cluster->width = cloud_cluster->size ();
    cloud_cluster->height = 1;
    cloud_cluster->is_dense = true;
    std::cout << "PointCloud representing the Cluster: " << cloud_cluster->size () << " data points." << std::endl;
    j++;
  }
  std::cout << j <<std::endl;
  cloud_cluster->header.frame_id = cloud->header.frame_id;
  pub_clust.publish(cloud_cluster);
}  



int main (int argc, char** argv)
{
  ros::init (argc,argv,"pcl_clustering_rgb");
  ros::NodeHandle nh;
  ROS_DEBUG("Reached Main");;
  pub_clust = nh.advertise<sensor_msgs::PointCloud2> ("pcl/points/clustered", 1);
  ros::Subscriber sub1 = nh.subscribe<sensor_msgs::PointCloud2> ("pcl/points/gpe", 1, cloud_clustering_rgb);
  ROS_INFO("Obtained PointCloud Data");
  ros::spin ();
  return(0);
}

