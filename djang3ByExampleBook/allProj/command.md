venv\Scripts\activate.bat


dev env config 
- pip镜像设置命令
    
        pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
        pip config set install.trusted-host mirrors.aliyun.com
        
- upgrade pip

    - python -m pip install –upgrade pip
   
   
        ``` resolve AttributeError: 'NoneType' object has no attribute 'bytes'```
    - python -m pip install -U --force-reinstall pip  
    
- quickly activate venv
        
        venv\Scripts\activate.bat  