# 功能介绍

RDK X3 Performance Node，基于Web打造的RDK X3 & RDK X3 Module 性能监测应用，监测CPU, BPU, Memory和Disk。 无论是什么品牌的电脑和手机，同一局域网下只需要在浏览器访问即可体验。

[![desktop_demo](./doc/desktop_demo.jpg)](./doc/desktop_demo.jpg)

[![mult_device](./doc/mult_device.jpg)](./doc/mult_device.jpg)

# 物料清单

| 机器人名称             | 生产厂家 | 参考链接                                       |
| ---------------------- | -------- | ---------------------------------------------- |
| RDK X3（任何内存版本） | 多厂家   | [点击跳转](https://developer.horizon.cc/rdkx3) |

# 使用方法

**安装Flask和psutil**

```
pip install psutil==5.9.6 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

```
pip install flask==3.0.0 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

**启动RDK X3后，通过终端SSH或者VNC连接机器人，复制如下命令在RDK的系统上运行，完成相关Node的安装。**

```
sudo apt update
sudo apt install -y tros-RDKX3PerformanceNode
```

**运行**

```
source /opt/tros/setup.bash
ros2 run performance_node_pkg_py RDKX3PerformanceNode
```

**在同一局域网访问X3的5000端口即可**

```
IP:5000
```

# 接口说明

暂无，未来会基于ROS2话题通讯机制重构。

# 常见问题

见评论区。



觉得还不错就点个赞再走吧~
