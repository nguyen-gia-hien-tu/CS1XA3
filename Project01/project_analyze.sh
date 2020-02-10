#!/bin/bash

# Feature 01: Script Input
read -p "Enter the feature to be executed: " num_fea

# Feature 02: FIXME Log
if [[ $num_fea -eq 2 ]] ; then
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
fi

# Feature 03: Checkout Latest Merge
if [[ $num_fea -eq 3 ]] ; then
    git checkout $(git rev-list --grep=merge HEAD -1)
fi

# Feature 04: File Size List
if [[ $num_fea -eq 4]] ; then
    find . -type f | xargs ls -lSh 
fi

# Feature 05: File Type Count
if [[ num_fea -eq 5 ]] ; then
    read -p "Enter the extension to find how many files with that extension: " file_ext
    ls -lR | grep ".$file_ext" | wc -l
fi