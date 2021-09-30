##udm_wafiik_square_move est un package utilisant un noeud qui appel le service move_base/goal et envoie des positions au turtulebot pour faire un carré

cd catkin_ws/src

git clone https://github.com/wafiik-aumeer/udm_wafiik_square_move.git

cd ..

catkin_make

roslaunch turtlebot3_gazebo turtlebot3_world.launch

roslaunch udm_square_move turtlebot3_navigation.launch map_file:=$HOME/map.yaml

rosrun udm_square_move movebase_square.py

