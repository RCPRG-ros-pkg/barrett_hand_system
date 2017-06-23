cmake_minimum_required(VERSION 2.8.6)

project(barrett_hand_cs_ve_msgs)

find_package(catkin REQUIRED
  COMPONENTS common_interfaces message_generation actionlib_msgs velma_core_cs_ve_body_msgs)

add_message_files(FILES
  Command.msg
  Status.msg
)
  

generate_messages(
  DEPENDENCIES
  velma_core_cs_ve_body_msgs
  )


catkin_package(
  CATKIN_DEPENDS message_runtime velma_core_cs_ve_body_msgs)
