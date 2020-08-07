#!/bin/bash

git clone git@github.com:YapAmbition/homebrew-todo.git
TODO_PATH=`cd homebrew-todo && pwd`
COMMAND="alias todo='perl $TODO_PATH/index.pl'"
echo $COMMAND >> ~/.bashrc
source ~/.bashrc