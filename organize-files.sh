#!/bin/bash

# read files and directories in current directory
items=(*)

for item in "${items[@]}"; do
    # check if it's a file
    if [[ -f $item ]]; then
        # get the extension of file
        ext="${item##*.}"
        
        # check if the current directory has a folder named (extension-of-current-file)
        if [[ ! -d $ext ]]; then
            # If not, make the folder
            mkdir "$ext"
        fi
        
        # move the file to that folder (in its respective file type extension)
        # but ignore the script file itself
        if [[ $item != "organize-files.sh" ]]; then
            mv "$item" "$ext/"
        fi
    elif [[ -d $item ]]; then
        # check if the current directory has a folder named "collection"
        if [[ ! -d "collection" ]]; then
            # If not, make the folder
            mkdir "collection"
        fi

        # move the directory to the "collection" folder
        mv "$item" "collection/"
    fi
done
