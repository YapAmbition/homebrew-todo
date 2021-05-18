#!/bin/bash

SCRIPT_PATH=`dirname "$0"`
TODO_PATH=`cd $SCRIPT_PATH && pwd`
echo $TODO_PATH
osname=`uname`
if [ "X$osname" == "XDarwin" ]; then
    sed -i '' "/alias todo='python3/d" ~/.bashrc
    sed -i '' "1i\\
alias todo='python3 $TODO_PATH/index.py'\\
" ~/.bashrc
else
    sed -i "/alias todo='python3/d" ~/.bashrc
    sed -i "1i alias todo='python3 $TODO_PATH/index.py'" ~/.bashrc
fi