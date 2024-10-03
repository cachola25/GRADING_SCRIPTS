#!/bin/bash

# Grading system doesn't allow extra credit to be entered,
# use this to log students that achieved extra credit
# and send the info to the professor
cd ../gradesheets
files=$(ls)
for file in $files; do
    if [ $file == "find_extra_credit.sh" ]; then
        continue
    fi
    grep 'Extra Credit:' $file > /dev/null
    if [ $? -ne 1 ]; then
        output=$(grep 'Extra Credit:' $file)
        name=$(echo $file | cut -d '_' -f1,2 | tr '_' ' ')
        printf "%-30s %s\n" "$name" "$output"
    fi
done