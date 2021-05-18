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
todo        打印最近3条todo项
-h          获得帮助
-a          打印所有的todo
-n n        返回最后n条todo
-A arg      新增一条内通为arg的todo
-D n        删除第n条todo
-i [n]      将第n条标记为重要,不传参数时展示所有重要的todo
-I [n]      取消第n条的重要标记,不传参数时展示所有不重要的todo
```