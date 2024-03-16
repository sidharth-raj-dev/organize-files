import os
import json
import shutil  # Import the shutil module for moving files

# Load the config.json file
with open('config.json', 'r') as f:
    config = json.load(f)

# Get the list of file extensions from the config
file_extensions = config.get('file_extensions', [])

# Get the list of items in the current directory
items = os.listdir()

# Create the "no_extension" folder if it doesn't exist
no_extension_folder = "files"
if not os.path.exists(no_extension_folder):
    os.mkdir(no_extension_folder)

for item in items:
    # Check if it's a file
    if os.path.isfile(item):
        # Get the extension of the file
        ext = os.path.splitext(item)[-1].lstrip('.')

        # If the file has no extension, move it to the "no_extension" folder
        if not ext:
            shutil.move(item, os.path.join(no_extension_folder, item))
        else:
            # If this is a new file extension, add it to the list and update the config file
            if ext not in file_extensions:
                file_extensions.append(ext)
                with open('config.json', 'w') as f:
                    json.dump({'file_extensions': file_extensions}, f)

            # Check if the current directory has a folder named after the extension
            if not os.path.exists(ext):
                # If not, make the folder
                os.mkdir(ext)

            # Move the file to that folder (in its respective file type extension)
            # but ignore the script file itself and config.json
            if item != "organize-files.py" and item != "config.json":
                shutil.move(item, os.path.join(ext, item))

    elif os.path.isdir(item) and item != "collection" and item != no_extension_folder:
        # Check if the current directory has a folder named "collection"
        if not os.path.exists("collection"):
            # If not, make the folder
            os.mkdir("collection")

        # Move the directory to the "collection" folder only if its name
        # is not in the list of file extensions
        if item not in file_extensions:
            shutil.move(item, os.path.join("collection", item))