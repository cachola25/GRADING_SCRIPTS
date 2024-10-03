cd gradesheets
files=$(ls)

# Adjust the old HW # to the new one
for file in $files
do
    newname=$(echo $file | tr '3' '4')
    mv $file $newname
done