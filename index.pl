#!/usr/bin/perl

### 参数解释:
sub paramDesc {
    my $desc = <<"EOF" ;
todo [-aAD] [args...]
-a          打印所有的todo
-A arg      新增一条内通为arg的todo
-D [arg]    不传arg时,删除最后一条;传递arg时删除第arg条
EOF
    print "$desc" ;
}

### 创建目录
# 参数1: 目录名
sub createDir {
    my $dirname = $_[0] ;
    mkdir($dirname);
}

### 创建文件
# 参数1: 文件名
sub createFile {
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
sub getHomePath {
    my $home = `echo \$HOME`;
    return trim($home);
}

### 读取文件后n行
# 参数1: 文件名
# 参数2: n
## 返回: 读取的内容
sub readTail {
    my $filename = $_[0] ;
    open(DATA, "<$filename") ;
    my @lines = <DATA> ;
    my $size = @lines ;
    my $n = $size ;
    $paramSize = @_ ;
    if ($paramSize == 2) {
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
sub addItem {
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
    my $paramSize = @_ ;
    my $n = $paramSize ;
    if ($paramSize > 1) {
        $n = @_[1] ;
    }
    my $content = readTail($filename) ;
    my @items = split('\n', $content) ;
    my $size = @items ;

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

### 初始化
sub init {
    # 检查是否存在~/.todo/todolist文件,如果不存在则创建
    $TODODIR = getHomePath() ;
    $FILENAME = ".todolist" ;
    $TODOFILE = "${TODODIR}/${FILENAME}" ;
    createDir($TODODIR) ;
    createFile($TODOFILE) ;
}

sub main {
    init() ;
    my $paramSize = @_ ;
    if ($paramSize == 0) {
        print readTail($TODOFILE, 3) ;
        exit ;
    }
    my $firstParam = @_[0] ;

    if ($firstParam =~ /^-[a-zA-Z]{1}$/) {
        $firstParam =~ s/-// ;
        if ($firstParam eq "a") {
            print readTail($TODOFILE) ;
            exit ;
        } elsif ($firstParam eq "A") {
            if ($paramSize == 2) {
                my $item = @_[1] ;
                addItem($TODOFILE, $item) ;
                exit ;
            }
        } elsif ($firstParam eq "D") {
            if ($paramSize == 1) {
                del($TODOFILE) ;
                exit ;
            } elsif ($paramSize == 2) {
                my $n = @_[1] ;
                del($TODOFILE, $n) ;
                exit ;
            }
        }
    }
    paramDesc() ;
    exit ;
}

main(@ARGV);