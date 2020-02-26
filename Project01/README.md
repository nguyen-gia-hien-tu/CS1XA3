# CS1XA3 Project01 - tun1

## USAGE
1. Use the `cd` command to get into the `CS1XA3` folder
2. Execute the script from the project root (i.e. execute the script when you are in the `CS1XA3` folder) with:
* `chmod +x ./Project01/project_analyze.sh`
* `./Project01/project_analyze.sh`
   
**Note:** 
* You don't need to type in any argument, after executing the script, there will be user prompt asking you to enter which feature you want to execute
* Enter __1__, __2__, __3__, or __4__ corresponding to the feature you want to execute
* You will need to enter the number correctly or the script won't run anything
* You need to run the script again to test another feature

## Feature 1: Script Input
This feature is described in the `USAGE` section above

## Feature 2: FIXME Log
* __Description:__ 
    * This feature finds every file in the repository folder (`CS1XA3` folder) and its sub-folders that has the word `#FIXME` (case sensitive) in the last line and put a list of the file names in `CS1XA3/Project01/fixme.log`
    * The feature will ignore `.git` directory
* __Execution:__ Execute this feature by typing `2` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__ 
    * The idea on how to check if a string contains a specific word is from: https://stackoverflow.com/questions/229551/how-to-check-if-a-string-contains-a-substring-in-bash
    * The idea on how to ignore a directory with `find` command is from: https://stackoverflow.com/questions/2314643/how-can-i-get-find-to-ignore-svn-directories


## Feature 3: Checkout Latest Merge
* __Description:__ 
    * This feature checkouts the latest commit that has the word `merge` (case insensitive) in its commit message
    * __You need to commit all your changes before executing this feature__
* __Execution:__ Execute this feature by typing `3` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__ 
    * The idea on how to list the commits is from the Pro Git book: https://git-scm.com/docs/git-rev-list


## Feature 4: File Size List
* __Description:__ 
    * This feature lists all files in the repo (`CS1XA3` folder and its sub-folders) and their sizes in human readable format sorted from largest to smallest
    * The feature will ignore any files in the `.git` directory
* __Execution:__ Execute this feature by typing `4` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__
    * The idea on how to use `ls` to list in human readable format and sort from largest to smallest is from: https://www.cyberciti.biz/faq/linux-ls-command-sort-by-file-size/
    * The idea on how to ignore a directory with `find` command is from: https://stackoverflow.com/questions/2314643/how-can-i-get-find-to-ignore-svn-directories

## Feature 5: File Type Count
* __Description:__ 
    * This feature asks the user to enter an extension and outputs the number of files in the repo folder and sub-folders with that extension
    * The feature will ignore `.git` directory
* __Execution:__ Execute this feature by typing `5` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__
    * The idea on how to count files by extension is from: https://www.2daygeek.com/how-to-count-files-by-extension-in-linux/

## Feature 6: Find Tag
* __Description:__ This feature:
    * Prompts the user a for a __Tag__ (a single word) using `read` command
    * Creates a log file `CS1XA3/Project01/Tag.log` where `Tag` is the name of the Tag that the user provided (overwrite the file if the file doesn't already exist)
    * Finds all the lines that begin with a comment (#) and iclude the __Tag__ in all python files, then put them in `CS1XA3/Project01/Tag.log` 
* __Execution:__ Execute this feature by typing `6` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): ` 
* __Reference:__
    * The idea on how to get the number of words given as input in a "read" command is from: https://unix.stackexchange.com/questions/309272/how-to-get-the-number-of-words-given-as-input-in-a-read-command

## Feature 8: Backup and Delete / Restore
* __Description:__
    * The feature will not work if there are 2 files with the same name but in different directories
* __Execution:__
* __Reference:__
    * The idea on how to ignore case with if statement is from: https://stackoverflow.com/questions/13848101/case-insensitive-string-comparison-in-bash
    * The idea on getting the file path is from: https://superuser.com/questions/202645/how-to-get-the-full-path-of-a-file-in-bash/202654


## Custom Feature 1: Organize Files
* __Description:__
    * This feature asks the user to choose __Organize__ or __Unorganize__
    * If the user chooses __Organize__:
        * The script will move all non-hidden files with the same extension into the folder `CS1XA3/Project01/Organize_<the extension>` where `the extension` is the extension of those files
        * The script will keep track of the files' original paths by storing them in `CS1XA3/Project01/organize_path.log` 
    * If the user chooses __Unorganize__:
        * All of the files that are stored in the `CS1XA3/Project01/Organized_<the extension>` folders will restored to their original location
* __Execution:__ Execute the feature by typing `CF1` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__
    * The idea on how to get the extension of a file is from: https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash

## Custom Feature 2: Checking Password
* __Desciption:__ 
    * The script will find every file ends with `.txt` and has the word `Password: ` in it
    * It will then check if the word follows the word `Password: ` is a good password or not
    * The script will output to the `CS1XA3/Project01/password.log` file (it will create the `password.log` file if it doesn't exist, overwrite if it does) __the name of the file__ in which the password is not good, __the password__ and __recommend__ what is missing to be a good password
    * If the `.txt` file has multiple passwords, the script will output the recommendation to be a good password corresponding to each password

    * __Notes:__ Please consider a good password is a password that has:
        * A length from 6 to 255 characters
        * At least 1 upper case letter
        * At least 1 lower case letter
        * At least 1 number from 0-9
        * At least 1 special character (i.e. !@#$%^&*()_+)
* __Execution:__ Execute the feature by typing `CF2` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__
    * The idea on how to search for a word after a specific word is from: https://stackoverflow.com/questions/17371197/extract-one-word-after-a-specific-word-on-the-same-line
    * The idea on how to check if a string contains what is from: https://www.golinuxcloud.com/check-if-string-contains-numbers-shell-script/
