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
echo "Feature CF1: Organize Files"
echo "Feature CF2: Checking Password"
echo ""

num_fea=1
while [ $num_fea = "1" ] ; do
    read -p "Enter the feature to be executed (this is Feature 1): " num_fea
done

# Feature 02: FIXME Log
if [ "$num_fea" = "2" ] ; then
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
if [ "$num_fea" = "3" ] ; then
    git checkout $(git rev-list -i --grep=merge HEAD -1)
fi

# Feature 04: File Size List
if [ "$num_fea" = "4" ] ; then
    find . -type f -not -iwholename "*.git*" | xargs ls -aRlSh
fi

# Feature 05: File Type Count
if [ $num_fea = "5" ] ; then
    read -p "Enter the extension to find how many files with that extension are in the repo: " file_ext
    num_file=$(ls . -alR -I ".git" | grep ".*\.$file_ext$" | wc -l)
    echo "There are $num_file files with that extension"
fi

# Feature 06: Find Tag
if [ $num_fea = "6" ] ; then
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

# Feature 08: Backup and Delete / Restore
if [ $num_fea = "8" ] ; then
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
            echo "ERROR: The 'restore.log' file does not exist"
        fi
    fi
fi

# Custom Feature 1: Organize Files
if [ $num_fea = "CF1" ] ; then
    read -p "Enter \"Organize\" to organize files with the same extension or \"Restore\" to restore those files to their original location: " option

    if [ "${option,,}" == 'organize' ] ; then
        echo -n > ./Project01/organize_path.log
        while [ $(find . -type f -not -path "./Project01/Organize_*" -not -path "./.*" -not -name "project_analyze.sh" -not -name "organize_path.log" -name "*.*" | wc -l) -gt 0 ]
            do
                file=$(find . -type f -not -path "./Project01/Organize_*" -not -path "./.*" -not -name "project_analyze.sh" -not -name "organize_path.log" -name "*.*" | head -n 1)                
                fileExt=${file##*.}
                if ! [ -d ./Project01/Organize_"$fileExt" ] ; then
                    mkdir ./Project01/Organize_"$fileExt"
                else
                    rm -r ./Project01/Organize_"$fileExt"
                    mkdir ./Project01/Organize_"$fileExt"
                fi

                echo "$(find . -type f -not -path "./Project01/Organize_*" -not -path "./.*" -not -name "project_analyze.sh" -not -name "organize_path.log" -name "*.$fileExt" -print0 | xargs -0 readlink -f)" >> ./Project01/organize_path.log 
                find . -type f -not -path "./Project01/Organize_*" -not -path "./.*" -not -name "project_analyze.sh" -not -name "organize_path.log" -name "*.$fileExt" -print0 | xargs -0 -i mv '{}' ./Project01/Organize_$fileExt       
            done

    elif [ "${option,,}" == "restore" ] ; then
        if [ -f ./Project01/organize_path.log ] ; then
            for orgDir in ./Project01/Organize_*/* ; do
                    cp "$file" $(grep $(echo "$file" | rev | cut -d "/" -f 1 | rev) ./Project1/organize_path.log)
            done
        else
                echo "ERROR: The 'organize_path.log' file does not exist"
        fi
    fi
fi

# Custom Feature 2: Checking Password
if [ $num_fea = "CF2" ] ; then
    echo "PASSWORDS NEEDED TO BE IMPROVED" > ./Project01/password.log

    find . -type f -name "*.txt" -print0 | while IFS= read -d '' file
    do
        grep -oP "(?<=Password: )[^ ]+" "$file" | while IFS= read passLine ; do
            if [ ${#passLine} -lt 6 ] || [ ${#passLine} -gt 255 ] || ! [[ "$passLine" =~ [A-Z] ]] || ! [[ "$passLine" =~ [a-z] ]] || ! [[ "$passLine" =~ [0-9] ]] || ! [[ "$passLine" == *['!'@\#\$%^\&*()_+]* ]] ; then
                echo >> ./Project01/password.log
                echo "$file" >> ./Project01/password.log
                echo "Password: $passLine" >> ./Project01/password.log
            fi
            if [ ${#passLine} -lt 6 ] || [ ${#passLine} -gt 255 ] ; then
                echo "The length of the password is not from 6 to 255 characters" >> ./Project01/password.log
            fi
            if ! [[ "$passLine" =~ [A-Z] ]] ; then
                echo "This password needs to have at least 1 upper case letter" >> ./Project01/password.log
            fi
            if ! [[ "$passLine" =~ [a-z] ]] ; then
                echo "This password needs to have at least 1 lower case letter" >> ./Project01/password.log
            fi
            if ! [[ "$passLine" =~ [0-9] ]] ; then
                echo "This password needs to have at least 1 number" >> ./Project01/password.log
            fi
            if ! [[ "$passLine" == *['!'@\#\$%^\&*()_+]* ]] ; then
                echo "This password needs to have at least 1 special character" >> ./Project01/password.log
            fi
        done
    done
fi