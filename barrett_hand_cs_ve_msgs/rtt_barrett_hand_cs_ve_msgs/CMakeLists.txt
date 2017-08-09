cmake_minimum_required(VERSION 2.8.3)
project(rtt_barrett_hand_cs_ve_msgs)

find_package(catkin REQUIRED COMPONENTS rtt_roscomm common_interfaces barrett_hand_cs_ve_msgs rtt_velma_core_cs_ve_body_msgs rtt_barrett_hand_msgs)

ros_generate_rtt_typekit(barrett_hand_cs_ve_msgs)

orocos_generate_package(
  DEPENDS barrett_hand_cs_ve_msgs
  DEPENDS_TARGETS rtt_roscomm
)
