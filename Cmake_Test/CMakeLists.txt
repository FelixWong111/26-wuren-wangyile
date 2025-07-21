cmake_minimum_required(VERSION 3.10)
project(Test)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)

set(CMAKE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/CMake 1")
#定义变量指代绝对位置（路径）

#添加引用头文件
include_directories(
    "${CMAKE_DIR}/common/kalman/include"
#路径写到头文件的上一目录/（文件夹）
    "${CMAKE_DIR}/common/math/include"
    "${CMAKE_DIR}/modules/A1/include"
    "${CMAKE_DIR}/modules/A2/include"
    "${CMAKE_DIR}/modules/M1/include"
    "${CMAKE_DIR}/modules/M2/include"
    /usr/local/include/opencv4
)

#添加库（.cpp程序）
#尝试过用common和modules两个总库这样来添加总是报错？猜测是这样建立库后，M1的cmakelists文件中引用的“A1库”没有建立库（不是一个库），所以没有链接到
#写给自己的：同理，给M2增加了cmakelists文件，添加了用到的A1、A2两个库，果不其然成功了^v^
add_library(common_kalman INTERFACE)
target_link_directories(common_kalman INTERFACE "${CMAKE_DIR}/common/kalman/include")
#无.cpp文件，只有头文件，使用INTERFACE库类型

add_library(common_Math "${CMAKE_DIR}/common/math/src/Math.cpp")
target_link_directories(common_Math PRIVATE ${OpenCV_LIBS})
#报错说要用OpenCV库，故链接

add_library(A1 
    "${CMAKE_DIR}/modules/A1/src/A11.cpp"
    "${CMAKE_DIR}/modules/A1/src/A12.cpp"
    "${CMAKE_DIR}/modules/A1/src/A13.cpp"
    )

add_library(A2 "${CMAKE_DIR}/modules/A2/src/A2.cpp")
add_library(M1 "${CMAKE_DIR}/modules/M1/src/M1.cpp")
add_library(M2 "${CMAKE_DIR}/modules/M2/src/M2.cpp")
target_link_directories(M2 PRIVATE ${OpenCV_LIBS})

#创建可执行文件
add_executable(test "${CMAKE_DIR}/main.cpp")

#链接库
target_link_libraries(test 
    PRIVATE 
    common_kalman
    common_Math
    M1
    M2
    A1
    A2
#要将依赖高层库放在前面（M1/M2放在A1/A2前）
    ${OpenCV_LIBS}
)