# toys-and-tools
# Mqtt协议的上传下发控制
## 需要用到的东西：
### micorbit开发板、raspberry 4、本地服务器
## 简介：
### 此次项目采用的是node -red搭建后台及交互界面，，microbit通过蓝牙发送至树莓派上，树莓派通过
### 蓝牙查询，将查询到的数据通过mqtt上传到本地服务器
### 从microbit开始：由于micorbit在设计之初只有12k的ram，所以在运行蓝牙服务之后无法在运行micro python 所以此次编程只有采用图形化编程，图形化编程如图所示
![](https://i.loli.net/2020/08/07/fQHw5O4dszk3yl1.png)
### 设置好microbit之后开始要做的是树莓派和micorbit的配对，首先是设置microbit，microbit需要首先设置任意配对
![](https://i.loli.net/2020/08/07/5r3u2MCdIU9zEyb.png)
### 其次是使用树莓派上的bluetoothctl命令来进行连接，首先是scan on ，然后是pair。pair完成之后quit即可
## 树莓派上的转发采用的是python开发，选择python开发以为python有很方便的mqtt的包，安装方便。
### 用pip install paho-mqtt安装即可
### 关于代码实现，主要的思路就是用多线程实现订阅和收发，再把订阅回来的命令放入函数中，具体可参考附录的python代码
# 服务器端
## 服务器端主要要安装两个软件一个是node-red用于搭建ui及控制逻辑、还有一个
## 是mysql用于存储数据，由于是mysql所以需要一个管理工具，这里我使用的是
## phpmyadmin 以上三个软件用linux自带的apt命令即可安装。
![](https://i.loli.net/2020/08/07/DRZnPQFp1KLM49O.png)
## 以上是node-red最终显示成果，如果需要同样的界面，在node-red选择导入即可
