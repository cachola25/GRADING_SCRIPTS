#!/bin/bash
# Simple script to create a grading rubric for each student
# with their name and HW# attached
directories=$(ls -d */ | grep grp | tr -d '/')
for dir in $directories; do
	cd $dir
	files=$(ls | tr ' ' '_')
	for filename in $files; do
		newname=$(echo $filename | cut -d '_' -f1,2)
		concat='_HW4.txt'
		final=$newname$concat
		cp ../rubric.txt ../gradesheets/$final
	done
	cd ..
done