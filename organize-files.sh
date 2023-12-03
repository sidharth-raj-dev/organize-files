#!/bin/bash

# read files in current directory, ignore the directories / folders
files=(*)

for file in "${files[@]}"; do
    # check if it's a file and not a directory
    if [[ -f $file ]]; then
        # get the extension of file
        # store the extension in a var
        ext="${file##*.}"
        
        # check if the current directory has a folder named (extension-of-current-file)
        if [[ ! -d $ext ]]; then
            # If not, make the folder
            mkdir "$ext"
        fi
        
        # move the file to that folder (in its respective file type extension)
        mv "$file" "$ext/"
    fi
done
