#!/bin/bash

# Feature 01: Script Input
clear
echo "Feature 1: Script Input"
echo "Feature 2: FIXME Log"
echo "Feature 3: Checkout Latest Merge"
echo "Feature 4: File Size List"
echo "Feature 5: File Type Count"
echo "Feature 6: Find Tag"
echo "Feature 7: Switch to Executable"
echo ""

num_fea=1
while [ $num_fea -eq 1 ] ; do
    read -p "Enter the feature to be executed (this is Feature 1): " num_fea
done

if [[ $num_fea -eq 6 ]] || [[ $num_fea -eq 7 ]]  ; then
    echo "Sorry, this feature has not been implemented yet :("
fi

# Feature 02: FIXME Log
echo -n > fixme.log
if [[ $num_fea -eq 2 ]] ; then
    for item in $(find . -type f) ; do
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
if [[ $num_fea -eq 4 ]] ; then
    find . -type f | xargs ls -lSh
fi

# Feature 05: File Type Count
if [[ num_fea -eq 5 ]] ; then
    read -p "Enter the extension to find how many files with that extension: " file_ext
    num_file=$(ls -alR | grep ".*\.$file_ext$" | wc -l)
    echo "There are $num_file files with that extension"
fi
