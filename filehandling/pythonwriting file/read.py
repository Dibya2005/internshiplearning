# file_path="C:\\Users\\dibya\\OneDrive\\Documents\\py bootcamp\\sss\\sigma\\filehandling\\k.txt"
# try:
#   with open(file_path,"r") as file:
#     content=file.read()
#     print(content)
# except FileNotFoundError:
#   print("file is not found")
# except PermissionError:
#   print("you not have permission to read that file")
# import json

# file_path = "C:\\Users\\dibya\\OneDrive\\Documents\\py bootcamp\\output.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         # print(content)
#         #we can access the json file using key also
#         print(content["name"])
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("You do not have permission to read the file.")
# except json.JSONDecodeError:
#     print("Error decoding JSON. Check if the file contains valid JSON.")
import csv
import json

file_path = "C:\\Users\\dibya\\OneDrive\\Documents\\py bootcamp\\output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        # print(content)
        #we can access the json file using key also
        for i in content:
             print(i)
            #if you need specific column of data from csv file you can use index
            #print(i[0])
        
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You do not have permission to read the file.")
except json.JSONDecodeError:
    print("Error decoding JSON. Check if the file contains valid JSON.")


