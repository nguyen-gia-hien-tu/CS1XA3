#!/bin/bash

# Feature 01: Script Input
clear
echo "Feature 1: Script Input"
echo "Feature 2: FIXME Log"
echo "Feature 3: Checkout Latest Merge"
echo "Feature 4: File Size List"
echo "Feature 5: File Type Count"
echo ""

num_fea=1
while [ $num_fea -eq 1 ] ; do
    read -p "Enter the feature to be executed (this is Feature 1): " num_fea
done

# Feature 02: FIXME Log
if [[ $num_fea -eq 2 ]] ; then
    echo -n > fixme.log
    for item in $(find . -type f -not -iwholename "*.git*") ; do
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
    find . -type f -not -iwholename "*.git*" | xargs ls -aRlSh
fi

# Feature 05: File Type Count
if [[ num_fea -eq 5 ]] ; then
    read -p "Enter the extension to find how many files with that extension are in the repo: " file_ext
    num_file=$(ls . -alR | grep ".*\.$file_ext$" | wc -l)
    echo "There are $num_file files with that extension"
fi

