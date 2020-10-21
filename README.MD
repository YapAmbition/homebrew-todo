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
todo -D [n]             删除一条序号为n的待办,如果不传参数时
-i [n]                  将第n条标记为重要,不传参数时展示所有重要todo
-I [n]                  取消第n条的重要标记,不传参数时展示所有重要todo
-l [n][label] [label]   为第n条添加label标签,当第一个参数为label时第二个参数不用填,表示列出标签为label的所有todo
-L [n][label] [label]   为第n条删除label标签,当第一个参数为label时第二个参数不用填,表示列出标签为label的所有todo
```