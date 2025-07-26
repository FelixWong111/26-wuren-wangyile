#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def param_publisher():
    rospy.init_node('param_publisher', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1Hz

    rospy.loginfo("等待参数服务器准备...")
    required_params = ["linear_x_speed", "angular_z_speed"]
    for param in required_params:
        while not rospy.is_shutdown() and not rospy.has_param(param):
            rospy.loginfo(f"等待参数 {param} 加载...")
            rospy.sleep(1)  # 等待1秒后重试
    rospy.loginfo("参数服务器准备就绪")

    while not rospy.is_shutdown():
        # 读取参数（带默认值）
        linear_x = rospy.get_param("linear_x_speed", 0.5)
        angular_z = rospy.get_param("angular_z_speed", 0.5)

        # 构造消息
        twist_msg = Twist()
        twist_msg.linear.x = linear_x
        twist_msg.angular.z = angular_z

        pub.publish(twist_msg)
        rospy.loginfo(f"发布速度指令: 线速度x={linear_x}, 角速度z={angular_z}")
        rate.sleep()

if __name__ == '__main__':
    try:
        param_publisher()
    except rospy.ROSInterruptException:
        rospy.loginfo("发布方节点已停止")