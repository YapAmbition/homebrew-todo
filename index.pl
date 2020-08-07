#!/usr/bin/perl


use Getopt::Std;

### 参数解释:
sub help {
    my $desc = <<"EOF" ;
todo [-haAD] [args...] 打印最近3条todo项
-h          获得帮助
-a          打印所有的todo
-A arg      新增一条内通为arg的todo
-D [n]      不传n时,删除最后一条,否则删除第n条todo
EOF
    return "$desc" ;
}

### 创建目录
# 参数1: 目录名
sub create_dir {
    my $dirname = $_[0] ;
    mkdir($dirname);
}

### 创建文件
# 参数1: 文件名
sub create_file {
    my $filename = $_[0] ;
    open(DATA, ">>$filename");
    close(DATA);
}

### 去除首尾空格
# 参数1: 待去除空格的字符串
sub trim {
    my $ss = $_[0] ;
    $ss =~ s/(^\s+|\s+$)//g ;
    return $ss ;
}

### 获得当前用户的home目录
sub get_home_path {
    my $home = `echo \$HOME`;
    return trim($home);
}

### 读取文件后n行
# 参数1: 文件名
# 参数2: n
## 返回: 读取的内容
sub read_tail {
    my $filename = $_[0] ;
    open(DATA, "<$filename") ;
    my @lines = <DATA> ;
    my $size = @lines ;
    my $n = $size ;
    $param_size = @_ ;
    if ($param_size == 2) {
        $n = $_[1] ;
    }
    $content = "";
    for ($i = 1 ; $i <= $size ; $i = $i + 1) {
        if ($i > $size - $n) {
            $content = "${content}${i}.@lines[$i-1]";
        }
    }
    close(DATA) ;
    return $content;
}

### 在文件里添加一条消息
# 参数1: 文件名
# 参数2: 加入的字符串
sub add_item {
    my $filename = @_[0] ;
    my $item = @_[1] ;
    $item = trim($item) ;
    $item = "$item\n" ;
    open(DATA, ">>$filename");
    print DATA $item ;
    close(DATA) ;
    return $item ;
}

### 删除第n条
# 参数1: 文件名
# 参数2: n,如果不传则删除最后一条
sub del {
    $filename = @_[0] ;
    my $param_size = @_ ;
    my $content = read_tail($filename) ;
    my @items = split('\n', $content) ;
    my $size = @items ;
    my $n = $size ;
    if ($param_size > 1) {
        $n = @_[1] ;
    }

    open(DATA2, ">$filename") ;
    for ($i = 1 ; $i <= $size ; $i = $i + 1) {
        if ($i != $n) {
            my $item = @items[$i - 1] ;
            $item =~ s/^([0-9]+\.)// ;
            print DATA2 "$item\n" ;
        }
    }
    close(DATA2) ;
}

### 文件&全局变量初始化
sub init {
    my $file_name = "todolist" ; # todo列表文件名
    my $home_path = get_home_path() ; # 用户家目录绝对路径
    my $todo_work_dir = "${home_path}/.todo" ; # 工作目录绝对路径
    $TODO_FILE = "${todo_work_dir}/${file_name}" ; # todo文件绝对路径

    create_dir($todo_work_dir) ;
    create_file($TODO_FILE) ;
}

sub main {
    init() ;

    my %opts = () ;
    $ret = getopts('haA:D:', \%opts) ;

    ### 帮助
    if ($opts{'h'}) {
        print help() ;
        exit ;
    }

    ### 展示所有todo
    if ($opts{'a'}) {
        print read_tail($TODO_FILE) ;
        exit ;
    }

    ### 新增一条todo
    if ($opts{'A'}) {
        add_item($TODO_FILE, $opts{'A'}) ;
        exit ;
    }

    ### 删除一条todo
    if (exists($opts{'D'})) {
        $opts{'D'} ? del($TODO_FILE, $opts{'D'}) : del($TODO_FILE) ;
        exit ;
    }

    ### 输入错误,放在最后是因为当传入参数D时如果后面不接参数也应该能正确响应,而此时$ret却是0,所以只有所有条件都不满足时才会打印
    if (!$ret) {
        print help () ;
        exit ;
    }

    print read_tail($TODO_FILE, 3) ;
    exit ;
}

main(@ARGV);