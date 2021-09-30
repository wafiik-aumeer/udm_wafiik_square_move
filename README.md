
cd catkin_ws/src

git clone https://github.com/Goohuram/udm_square_move.git

cd ..

catkin_make

roslaunch turtlebot3_gazebo turtlebot3_world.launch

roslaunch udm_square_move turtlebot3_navigation.launch map_file:=$HOME/map.yaml

rosrun udm_square_move movebase_square.py

