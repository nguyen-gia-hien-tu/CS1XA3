#!/bin/bash

# Feature 01: Script Input
clear
echo "Feature 1: Script Input"
echo "Feature 2: FIXME Log"
echo "Feature 3: Checkout Latest Merge"
echo "Feature 4: File Size List"
echo "Feature 5: File Type Count"
echo "Feature 6: Find Tag"
echo "Feature 8: Backup and Delete / Restore"
echo ""

num_fea=1
while [ $num_fea -eq 1 ] ; do
    read -p "Enter the feature to be executed (this is Feature 1): " num_fea
done

# Feature 02: FIXME Log
if [ "$num_fea" -eq 2 ] ; then
    echo -n > ./Project01/fixme.log
    find . -type f -not -iwholename "*.git*" -print0 | while IFS= read -d '' item 
    do
            last_line=$(tail -n 1 "$item")
            if [[ "$last_line" == *"#FIXME"* ]] ; then
                echo "$item" >> ./Project01/fixme.log
            fi
    done
fi

# Feature 03: Checkout Latest Merge
if [ "$num_fea" -eq 3 ] ; then
    git checkout $(git rev-list -i --grep=merge HEAD -1)
fi

# Feature 04: File Size List
if [ "$num_fea" -eq 4 ] ; then
    find . -type f -not -iwholename "*.git*" | xargs ls -aRlSh
fi

# Feature 05: File Type Count
if [ $num_fea -eq 5 ] ; then
    read -p "Enter the extension to find how many files with that extension are in the repo: " file_ext
    num_file=$(ls . -alR -I ".git" | grep ".*\.$file_ext$" | wc -l)
    echo "There are $num_file files with that extension"
fi

# Feature 06: Find Tag
if [ $num_fea -eq 6 ] ; then
    echo -n "Enter a single word to represent a tag: "
    read -a tag
    while [[ ${#tag[@]} -ne 1 ]] ; do
        echo -n "Enter a single word to represent a tag: "
        read -a tag
    done

    echo -n > ./Project01/"$tag".log
    lines=$(find . -type f -name "*.py" | xargs grep '^#' | grep "$tag")
    echo "$lines" > ./Project01/"$tag".log
fi

# Feature 8: Backup and Delete / Restore
if [ $num_fea -eq 8 ] ; then
    read -p "Enter \"Backup\" to backup .tmp files or \"Restore\" to restore the files to their original location: " option

    if [ "${option,,}" == "backup" ] ; then
        if ! [ -d ./Project01/backup ] ; then
                mkdir ./Project01/backup
        else
                rm -r ./Project01/backup
                mkdir ./Project01/backup
        fi

        countFiles=$(find . -type f -name "*.tmp" | wc -l)
        if [ "$countFiles" -gt 0 ] ; then
                find . -type f -name "*.tmp" -print0 | xargs -0 -i cp '{}' ./Project01/backup
                echo "$(find . -type f -name "*.tmp" -not -path "./Project01/backup/*" -print0 | xargs -0 readlink -f)" > ./Project01/restore.log               
                find . -type f -name "*.tmp" -not -path "./Project01/backup/*" -print0 | xargs -0 rm
        fi

    elif [ "${option,,}" == "restore" ] ; then
        if [ -f ./Project01/restore.log ] ; then
                for f in ./Project01/backup/* ; do
                        cp "$f" $(grep $(echo "$f" | rev | cut -d "/" -f 1 | rev) ./Project01/restore.log)
                done
        else
            "The 'restore.log' file does not exist"
        fi
    fi
fi