#!/bin/bash

# Define the target directories
target_directories=("grp1" "grp2" "grp3")

# Loop through each target directory and rename the 
# directories with the students names since spaces
# are messy to work with
for dir in "${target_directories[@]}"; do
    # Check if the directory exists
    if [ -d "$dir" ]; then
        # Copy the source file to the target directory
        IFS=$'\n'
        for subdir in $(ls $dir); do
            unset IFS
            newname=$(echo $subdir | tr ' ' '_')
            mv "$dir/$subdir" $dir/$newname
        done
    else
        echo "Directory $dir does not exist"
    fi
done