### 简单地在命令行中记录你的TodoList

如何安装: 
```
git clone git@github.com:YapAmbition/homebrew-todo.git
cd homebrew-todo
chmod +x install.sh
./install.sh
source ~/.bashrc
```

使用帮助:
```
命令列表
todo                    列出最后3条待办
todo -h                 帮助
todo -a                 列出所有待办
todo -A "something"     新增一条内容为something的待办
todo -D [num]           删除一条序号为num的待办,如果不传参数时,删除最后一条
-i [n]                  将第n条标记为重要,不传参数时展示所有重要todo
-I [n]                  取消第n条的重要标记,不传参数时展示所有重要todo
```

额外功能:
```
标签功能:
    功能目标:
        1. 允许用户给每一条todo添加标签,标签名遵循[a-zA-Z_]+[a-zA-Z,._-]*
        2. 允许用户在查询时使用-l后接标签,查询所以该标签的todo
    功能实现:
        1. 在.todo文件夹中新建文件: decorator
        2. 见decorator.py源码
```