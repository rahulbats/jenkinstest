#!/bin/bash
    
SAVEIFS=$IFS   # Save current IFS (Internal Field Separator)
IFS=$'\n'      # Change IFS to newline char
names=($gitdiff)      # split the `names` string into an array by the same name
IFS=$SAVEIFS   # Restore original IFS
echo "this is inside script"+${names}

for name in "${names[@]}"
do
    echo name
    IFS=$'\t'
    callVar=(${name})
    echo "file"+${callVar[0]}+"-"+${callVar[1]}
done
