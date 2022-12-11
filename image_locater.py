import os
 
# Get the list of all files and directories
path = "downsized"
dir_list = os.listdir(path)
with open("images.txt", "w") as outfile:
    for images in dir_list:
        if ".jpg" in images:
            outfile.write(f"{images}\n")