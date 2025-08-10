import os

# Specify the path to the directory
directory_path = '/'

# List all files and directories in spacified path
contents = os.listdir(directory_path)

# print each file and directory name 
for item in contents: 
    print(item)



