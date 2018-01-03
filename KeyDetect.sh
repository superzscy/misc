#!/bin/bash

cnt=0
function walk()
{
    for file in `ls $1`
    do
    local path=$1"/"$file
    if [ -d $path ];then
    #   echo "DIR $path"
        walk $path $2
    else
        if [ $file != "$2".lua ];then
            local matchCnt=`grep $2 "$path" | grep -v "$2".lua | wc -l`
            if [ "$matchCnt" -gt 0 ];then
                ((cnt++))
            fi
        fi
    fi
    done
}

if [ $# -lt 2 ];then
    echo "Count each key referenced in all files under folder"
    echo "Usage: ./KeyDetect.sh folder key1 key2 ..."
    exit
fi

echo -- searching in "$1"

for var in "$@"
do
    if [ "$1" != "$var" ];then
        cnt=0
        walk "$1" "$var"
        echo -- searching for "$var" : "$cnt"
    fi
done