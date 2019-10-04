#!/bin/bash

#FileName="res.txt"
#echo "%CPU\t%MEM" > $FileName
for (( i = 0; i < 10; i++ )) do
    output=`top -n 1 -pid 71202 > usage.txt`
    res=`gawk '{if (NR == 8) { printf "%d\t%d", $10, $11 } }' usage.txt`
    echo "$res" >> $FileName
    sleep 60
done
