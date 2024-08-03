# Light Bot
An example bot to help you make a QQBot quickly.
### About
Because most of `protocol bot` (such as ___Go-CQ___) are in great danger of banned  
And `LiteLoader QQNT` and `OneBot11`gets popular.  
This Project is based-on [LLOB(LiteLoader OneBot)](https://github.com/LLOneBot/LLOneBot).  Thanks their supports.  

[!!!!] Don't share this project on QQ Online Groups.

## **Start**
##### Some questions
- Why don't we new a branch ` kotlin`?  
It's easy to build. But we may new branch later. Now there's few developers that use the project. 
- If I only want to develop one of cores, can I delete another one?  
Sure.You can edit `buildconfig.yml`




### LightBot Python Core
##### For windows executable files(.exe)  
###### For Linux, you can use `SourceCode` to use LightBot
- How can I use it on `Windows`?  
Download the executable file in [releases](https://www.github.com/Undef1nedT1am/LightBot/releases)  
Put LightBot  in any empty folders and execute it  
Then `LightBot` will generate some `.yml` files  (Download from network)  
Go `config.yml` and change configs. (Such as host-ip, pltype etc.)
- How can I build it to `.exe` file or `Linux Executable` file?  
```shell
git clone https://www.github.com/Undef1nedT1am/LightBot.git
```
You can use `venv` python  
```shell
python path of VENV -m pip install -r requirements.txt
```
```shell
python path of VENV -m nuitka --remove-output --lto=yes --output-dir=LightBot-build-out --onefile PythonCore/LightBot.py
```


