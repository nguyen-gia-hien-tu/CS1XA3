# CS 1XA3 Project01 - tun1

## USAGE
Execute the script from the project root (i.e. execute the script when you are at the `CS1XA3` folder) with:
* `chmod +x ./Project01/project_analyze.sh`
* `./Project01/project_analyze.sh`

You need to run the script again to test another feature
   
**Note:** 
* You don't need to type in any argument, after executing the script, there will be user prompt guiding to the next steps
* Enter __1__, __2__, __3__, or __4__ corresponding to the feature you want to execute
* You will need to enter the number correctly or the script won't run anything feature

## Feature 2: FIXME Log
* __Description:__ 
    * This feature finds every file in the repository folder (`CS1XA3` folder) and its sub-folders that has the word `#FIXME` in the last line and put a list of the file names in `CS1XA3/Project01/fixme.log`
    * The feature will ignore `.git` directory
* __Execution:__ Execute this feature by typing __2__ when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__ 
    * The idea on how to find a word in the last line of a file is from: https://unix.stackexchange.com/questions/213610/find-last-line-of-a-file-for-matching-string?rq=1
    * The idea on how to ignore a directory with `find` command is from: https://stackoverflow.com/questions/2314643/how-can-i-get-find-to-ignore-svn-directories


## Feature 3: Checkout Latest Merge
* __Description:__ 
    * This feature checkouts the latest commit that has the word `merge` (case insensitive) in its commit message
    * __You need to commit all your changes before executing this feature__
* __Execution:__ Execute this feature by typing __3__ when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__ 
    * The idea on how to list the commits is from the Git Pro book: https://git-scm.com/docs/git-rev-list


## Feature 4: File Size List
* __Description:__ 
    * This feature lists all files in the repo (`CS1XA3` folder and its sub-folders) and their sizes in human readable format sorted from largest to smallest
    * The feature will ignore any files in the `.git` directory
* __Execution:__ Execute this feature by typing __4__ when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* __Reference:__
    * The idea on how to use `ls` to list in human readable format and sort from largest to smallest is from: https://www.cyberciti.biz/faq/linux-ls-command-sort-by-file-size/
    * The idea on how to ignore a directory (specigically `.git` directory) is from: https://stackoverflow.com/questions/2314643/how-can-i-get-find-to-ignore-svn-directories

<!--
## Feature 5:
* Description: This feature asks the user to enter an extension and outputs the number of files in the repo with that extension
* Execution: Execute this feature by typing `5` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* Reference:
    * The idea on how to count files by extension is from: https://www.2daygeek.com/how-to-count-files-by-extension-in-linux/
-->

## Custom Feature 1: Organize Files
* __Description:__
    * This feature asks the user to choose __Organize__ or __Unorganize__
    * If the user chooses __Organize__:
        * The script will move all non-hidden files with the same extension into the folder `CS1XA3/Project01/Organize_<the extension>` where `the extension` is the extension of those files
        * The script will keep track of the files' original paths by storing them in `CS1XA3/Project01/organize_path.log` 
    * If the user chooses __Unorganize__:
        * All of the files that are stored in the `CS1XA3/Project01/Organized_<the extension>` folders will restored to their original location
* __Execution:__ Execute the feature by typing `CF1` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `

## Custom Feature 2: Checking Password
* __Desciption:__ 
    * The script will find every file ends with `.txt` and has the word `Password: ` in it
    * It will then check if the word follows the word `Password: ` is a good password or not
    * The script will output to the `CS1XA3/Project01/password.log` file (it will create the `password.log` file if it doesn't exist, overwrite if it does) the name of the __file__ in which the password is not good, the password and recommend what is missing to be a good password
    * If the `.txt` file has multiple passwords, the script will output the recommendation to be a good password corresponding to each password

    * __Notes:__ Please consider a good password is a password that has:
        * A length from 6 to 255 characters
        * At least 1 upper case letter
        * At least 1 lower case letter
        * At least 1 number from 0-9
* __Execution:__ Execute the feature by typing `CF2` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `

    