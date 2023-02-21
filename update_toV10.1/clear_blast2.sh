#!/bin/bash

path="/home/ubuntu/.sequenceserver/"
timestamp=$(date +%Y%m%d_%H%M%S)    
filename=log_$timestamp.txt    
log=$path$filename
days=7

#START_TIME=$(date +%s)

#find ~/.sequenceserver/ -maxdepth 1 -type d  ! -path "*ncbi*" ! -path "*links.rb" ! -path "*asked_to_join" -mtime +2
#find $path -maxdepth 1 -name "*.txt"  -type f -mtime +$days  -print -delete >> $log

#find $path -type d -exec basename '{}' ';' -print -delete | egrep '^.{20,}$'
dirlen="?????????????????????????????" 
cd $path  # IMPORTANT or will remove $path
if [ $# -eq 0 ]  # NO ARGS
then
    echo
    echo "No arguments supplied"
    echo "Found these directories to delete from '$path':"
    echo
    find . -maxdepth 1 -type d -name $dirlen'*'   # find dirs 
else

    if [[ $1 = "-d" ]]
    then
        echo "Arg[1] = $1"

        find . -maxdepth 1 -type d -name $dirlen'*' -ls -exec rm -rv {} +  # find/
    fi
fi
echo
echo "Add -d to delete the above directories in '$path'"
echo
