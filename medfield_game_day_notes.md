# Medfield Game Day Notes

## Jackal Steps
1) Power on Jackal
2) Connect to acl-jackal-2G on Intel Wireless
Jackal:
3) roscore
4) cd phoenix/phoenix-r1 && phxlaunch  dcist_medfield_launch jackal_experiment.xlaunch

6) Monitor: image stream ~ 30Hz, rostopic hz /acl_jackal/forward/color/image_raw/compressed
7) Monitor: IMU stream ~ 200Hz, rostopic hz /acl_jackal/forward/imu
8) Monitor: rostopic echo acl_jackal/barrel_scout/position

9) rviz: roslaunch dcist_medfield_launch rviz.launch
9a) IMPORTANT: rosrun dynamic_reconfigure dynparam set /acl_jackal/forward/aligned_depth_to_color/image_raw/compressedDepth png_level 4
10) Record: rosrun dcist_medfield_launch bag.py --robot acl_jackal --prefix test_medfield --config acl_jackal_topics_medfield.yaml


## Diagnostics & Misc

rostopic hz /acl_jackal/forward/color/image_raw/compressed
rostopic hz /acl_jackal/forward/imu
rostopic echo cl_jackal/barrel_scout/position
rostopic echo /acl_jackal/jackal_velocity_controller/odom
rosrun dynamic_reconfigure dynparam set /acl_jackal/forward/aligned_depth_to_color/image_raw/compressedDepth png_level 4

## Recording
rosrun capstone_launch bag.py --robot acl_jackal --prefix medfield --config acl_jackal_topics_medfield.yaml

## Playback
(on basestation laptop)
rosrun rviz rviz -d /home/swarm/phoenix/phoenix-r1/acl_jackal_medfield_replay.rviz
