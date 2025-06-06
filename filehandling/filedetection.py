import os #to work with file we have to import os module
#for file detection we can use relative file path = folder/test.txt
#or absolute= c:/usrs/brocode/destop/test.txt
import os  # To work with files, we import the os module

# You can use a relative path (e.g., "folder/test.txt") or an absolute path (e.g., "C:/users/brocode/desktop/test.txt")
file_path = "C:\\Users\\dibya\\OneDrive\\Desktop\\k.txt"


if os.path.exists(file_path):
    print(f"The location {file_path} exists")
    if os.path.isfile(file_path):
        print("this is a file")
    elif os.path.isdir(file_path):
        print("this is a directory")
else:
    print("Location does not exist")

