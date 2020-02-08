#!/bin/bash

# Script Input
read -p "Enter the feature to be executed: " num_fea

# FIXME Log
if [! -f fixme.log ] ; then
            touch fixme.log
else:
    echo > fixme.log
fi

for item in ./* ; do
    last_line=$(tail -n 1 "$item")
    if [[ $last_line == *"#FIXME"* ]] ; then
        echo "$item" >> fixme.log
    fi
done