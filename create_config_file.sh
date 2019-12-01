#!/usr/bin/env sh

FILENAME=".botkun.toml"

if  [ ! -e ~/$FILENAME ] && 
    [ ! -e ~/.config/$FILENAME ] &&
    [ ! -e ~/.config/botkun/$FILENAME ]
then
    cp ./$FILENAME ~
    echo "config file is created in ~"
else
    echo "config file already exists"
fi
