# Light Bot
![图片](https://github.com/user-attachments/assets/7e672f6c-a748-4e71-8862-b763b4ff59f4)

一个模板帮助你快速创建一个QQ机器人
### 关于

由于大多数`协议`机器人(例如GOCQ)处于账户被封禁的边缘，QSign的没落 以及`LiteLoaderQQNT`和`OneBot11标准`流行  
本项目基于 [LLOB(LiteLoader OneBot)](https://github.com/LLOneBot/LLOneBot)  

[!!!!] 不要在QQ官方群内讨论本项目
### Todo 列表
1. 混合协议的bot（http+ws）
2. Http事件上报密钥
## **开始**
##### 一些问题
- 为什么不新建一个分支 ` kotlin`?  
方便构建。当然会在以后新建分支，不过现在没几个开发者用本项目，暂时不考虑。（其实可能新建个项目）
- 如果我只想开发核心的其中一个，能不能把别的删除？  
可以






### LightBot Python Core

- 如何在`Windows`系统上使用?  
在 [releases](https://www.github.com/Undef1nedT1am/LightBot/releases) 上下载可执行文件  
将LightBot放入空文件夹中 然后执行它   
然后，`LightBot`将生成一些`.yml`文件（从网络下载） 
转到`config.yml`并更改配置。（如主机ip、pltype等） 
- 如何将LightBot构建为“.exe”文件或“Linux可执行文件”？
```shell
git clone https://www.github.com/Undef1nedT1am/LightBot.git
```
你可以使用`虚拟环境`

```shell
venv的python路径 -m pip install -r requirements.txt
```
```shell
venv的python路径 -m nuitka --remove-output --lto=yes --output-dir=LightBot-build-out --onefile PythonCore/LightBot.py
```


