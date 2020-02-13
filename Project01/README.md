# CS 1XA3 Project01 - tun1

## USAGE
<!--Access to the folder `/home/tun1/private/CS1XA3/Project01` using `cd` command-->

Execute the script from the project root (execute the script when you are at the `CS1XA3` folder) with:
* `chmod +x CS1XA3/Project01/project_analyze.sh`
* `./CS1XA3/Project01/project_analyze.sh`

You need to run the script again to test another feature
   
**Note:** 
* You don't need to type in any argument, after executing the script, there will be user prompt guiding to the next steps
* Enter 1, 2, 3,... corresponding to the feature you want to execute

## Feature 2: FIXME Log
* Description: 
    * This feature finds every file in the repository folder and subfolders and put a list of the file names in CS1XA3/Project01/fixme.log
    * The feature will ignore `.git` directory
* Execution: Execute this feature by typing `2` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* Reference: 
    * The idea on how to find a word in the last line of a file is from: https://unix.stackexchange.com/questions/213610/find-last-line-of-a-file-for-matching-string?rq=1

## Feature 3: Checkout Latest Merge
* Description: This feature finds the latest commit that has the word "merge" in its commit message
* Execution: Execute this feature by typing `3` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* Reference: 
    * The idea on how to list the commits is from the Git Pro book: https://git-scm.com/docs/git-rev-list

## Feature 4: File Size List
* Description: 
    * This feature lists all files in the repo and their sizes in human readable format from largest to smallest
    * The feature will ignore any files in the `.git` directory
* Execution: Execute this feature by typing `4` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* Reference:
    * The idea on how to use `ls` to list in human readable format and sort from largest to smallest is from: https://www.cyberciti.biz/faq/linux-ls-command-sort-by-file-size/
    * The idea on how to ignore a directory (specigically `.git` directory) is from: https://stackoverflow.com/questions/2314643/how-can-i-get-find-to-ignore-svn-directories

## Feature 5:
* Description: This feature asks the user to enter an extension and outputs the number of files in the repo with that extension
* Execution: Execute this feature by typing `5` when you are prompted with the statement `Enter the feature to be executed (this is Feature 1): `
* Reference:
    * The idea on how to count files by extension is from: https://www.2daygeek.com/how-to-count-files-by-extension-in-linux/
