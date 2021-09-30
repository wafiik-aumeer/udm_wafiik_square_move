#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client(x_pos, y_pos):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x_pos
    goal.target_pose.pose.position.y = y_pos
    goal.target_pose.pose.orientation.w = 1

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_square')
        corner1 = movebase_client(-0.5,-0.5)
        if corner1:
            rospy.loginfo("Corner 1 reached, proceding to next corner.")
        corner2 = movebase_client(-0.5,0.5)
        if corner2:
            rospy.loginfo("Corner 2 reached, proceding to next corner.")
        corner3 = movebase_client(-2,0.5)
        if corner3:
            rospy.loginfo("Corner 3 reached, proceding to next corner.")
        corner4 = movebase_client(-2,-0.5)
        if corner4:
            rospy.loginfo("Final corner reached")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
    rospy.spin()


             
