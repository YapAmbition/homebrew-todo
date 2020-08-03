#!/usr/bin/perl


# 创建目录
# 参数1: 目录名
sub createDir {
    my $dirname = $_[0] ;
    mkdir($dirname);
}

# 创建文件
# 参数1: 文件名
sub createFile {
    my $filename = $_[0] ;
    open(DATA, ">>$filename");
    close(DATA);
}

### 读取文件后n行
# 参数1: 文件名
# 参数2: n
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
    if ($size < $n) {
        $n = $size ;
    }
    for ($i = 1 ; $i <= $n ; $i = $i + 1) {
        print  + "$i.@lines[$size - $n + $i - 1]" ;
    }
    close(DATA) ;
}

### 去除首尾空格
# 参数1: 待去除空格的字符串
sub trim {
    my $ss = $_[0] ;
    $ss =~ s/(^\s+|\s+$)//g ;
    return $ss ;
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
    print "it is $item";
    print DATA $item ;
    close(DATA) ;
}

### 删除第n条
# 参数1: 文件名
# 参数2: n,如果不传则删除最后一条
sub del {
    $filename = @_[0] ;
    my $n = 0 ;
    my $size = @_ ;
    if ($size > 1) {
        $n = @_[1] ;
    }
    open(DATA, "<$filename");
    my @lines = <DATA> ;
    my $lineCount = @lines ;
    if ($size == 1) {
        $n = $lineCount ;
    }
    if ($n < 0 || $n > $lineCount) {
        return ;
    }
    $content = "" ;
    for ($i = 1 ; $i <= $lineCount ; $i = $i + 1) {
        if ($i != $n) {
            $content = "${content}@lines[$i - 1]" ;
        }
    }
    close(DATA) ;

    open(DATA2, ">$filename") ;
    print DATA2 $content ;
    close(DATA2) ;
}

### todo工作目录
$tododir = "/usr/local/Cellar/todo/1.0" ;

### todo文件地址
$todofile = "${tododir}/todolist";

createDir($tododir);
createFile($todofile);
readTail($todofile, 2);
# addItem($todofile, $item) or print $! ;
del($todofile);
readTail($todofile) ;