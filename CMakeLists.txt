cmake_minimum_required(VERSION 3.8)
project(challenge_10)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/GetHistory.srv"
  "srv/GetEchoStats.srv"
)

install(PROGRAMS
  scripts/cmd_parser.py
  scripts/secure_nav_client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
