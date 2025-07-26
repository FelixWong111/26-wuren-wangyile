#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

// 全局发布者，用于在回调函数中发布消息到/turtle1/cmd_vel
ros::Publisher cmd_vel_pub;

// 回调函数：接收cmd_vel消息并转发到/turtle1/cmd_vel
void twistCallback(const geometry_msgs::Twist::ConstPtr& msg)
{
    // 打印接收到的速度指令（用于调试）
    ROS_INFO("接收到速度指令: 线速度x=%.2f, 角速度z=%.2f",
             msg->linear.x, msg->angular.z);
             
    // 将接收到的消息转发到/turtle1/cmd_vel，主函数中指定了发布的话题
    cmd_vel_pub.publish(*msg);
}

int main(int argc, char **argv)
{
    // 初始化节点
    ros::init(argc, argv, "turtle_subscriber");
    
    // 创建节点句柄
    ros::NodeHandle nh;

    // 创建订阅者，订阅cmd_vel话题
    ros::Subscriber sub = nh.subscribe("cmd_vel", 10, twistCallback);

    // 初始化全局发布者，发布到turtlesim的控制话题
    cmd_vel_pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);

    ROS_INFO("订阅方已启动，等待速度指令...");

    // 消息循环（持续处理回调函数）
    ros::spin();

    return 0;
}
    