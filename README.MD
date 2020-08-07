* 数据存到~/.todo/todolist中
* 待办本身不带序列号
* 输入todo返回末尾3条todo
* 输入todo -a 输出todolist的所有待办
* 输入todo -A 新增一条待办到最后
* 输入todo -D 删除最后一条待办


```
命令列表
todo                    列出最后3条待办
todo -h                 帮助
todo -a                 列出所有待办
todo -A "something"     新增一条内容为something的待办
todo -D [num]           删除一条序号为num的待办,当不传num的时候删除最后一条
```