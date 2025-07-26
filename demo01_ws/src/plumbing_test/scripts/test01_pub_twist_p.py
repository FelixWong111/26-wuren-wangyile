#!/usr/bin/env python3
import rospy

#创建消息类型Twist
from geometry_msgs.msg import Twist

def param_publisher():
    #初始化节点'param_publisher'
    rospy.init_node('param_publisher', anonymous=True)
    #创建发布者pub,向'cmd_vel'话题发布Twist类型消息
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    #每秒发布一次
    rate = rospy.Rate(1)

    rospy.loginfo("等待参数服务器准备...")
    #检查有无两个必须参数，如没有则打印‘等待参数xx’，1s后再循环，直到节点被关闭或是加载到参数
    required_params = ["linear_x_speed", "angular_z_speed"]
    for param in required_params:
        while not rospy.is_shutdown() and not rospy.has_param(param):
            rospy.loginfo(f"等待参数 {param} 加载...")
            rospy.sleep(1)  # 等待1秒后重试
    rospy.loginfo("参数服务器准备就绪")

#循环发布消息
    while not rospy.is_shutdown():
        # 读取参数（带默认值）
        linear_x = rospy.get_param("linear_x_speed", 0.5)
        angular_z = rospy.get_param("angular_z_speed", 0.5)

        # 构造消息（创建类的对象），只要是.linear.x/.angular.z就能够被小乌龟的控制模块识别
        twist_msg = Twist()
        twist_msg.linear.x = linear_x
        twist_msg.angular.z = angular_z

        pub.publish(twist_msg)
        rospy.loginfo(f"发布速度指令: 线速度x={linear_x}, 角速度z={angular_z}")
        rate.sleep()

if __name__ == '__main__':#当运行main函数的时候，运行param_publisher函数
    try:
        param_publisher()
    except rospy.ROSInterruptException:
        rospy.loginfo("发布方节点已停止")