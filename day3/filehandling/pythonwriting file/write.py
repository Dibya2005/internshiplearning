#writing file (.txt,.json,.csv)
# txt_data="i like pizza "
# file_path="output.txt"
# with open(file=file_path,mode="w") as file:
#   file.write(txt_data)
#   print(f"file path {file_path} was created")
  #if we use mode="x" it will create a file if it is not
  #with will close the file automaticalky after execution
# txt_data="i like pizza "
# file_path="output.txt"
# try:
#   with open(file=file_path,mode="x") as file:
#     file.write(txt_data)
#     print(f"file path {file_path} was created")
# except FileExistsError:
#   print("thatfile already exist")

# import os

# txt_data = "i like pizza "
# file_path = "C:\\Users\\dibya\\OneDrive\\Documents\\py bootcamp\\output.txt"

# # for appending data
# try:
#     with open(file=file_path, mode="a") as file:
#         file.write(txt_data)
#         print(f"File path {file_path} was written to.")
# except FileExistsError:
#     print("That file already exists.")
# import os

# txt_data = ["eugame","squidgame","sponbob"]
# file_path = "C:\\Users\\dibya\\OneDrive\\Documents\\py bootcamp\\output.txt"

# # for appending data
# try:
#     with open(file=file_path, mode="a") as file:
#         for i in txt_data:
#             file.write(i+" ")
#         print(f"File path {file_path} was written to.")
# except FileExistsError:
#     print("That file already exists.")
#json file are some sort of key value file so we need a dictionartyt to impliment it
# import json
# emp={
#     "name":"spongbob",
#     "age":30,
#     "job":"cook"
# }
# file_path = "C:\\Users\\dibya\\OneDrive\\Documents\\py bootcamp\\output.json"

# # for appending data
# try:
#     with open(file=file_path, mode="a") as file:
#         json.dump(emp,file,indent=4) #it convert dictionary to json
#         #for each key value pair how many spaces we want to inmtemnt each
       
#         print(f"File path {file_path} was written to.")
# except FileExistsError:
#     print("That file already exists.")
#csv rfrile = is rally common like a straight sheet of data
import json
import csv

txt_data = [["name","age","job"],
            ["dibya",20,"developer"],
            ["patrick",37,"unemployed"]]

file_path = "C:\\Users\\dibya\\OneDrive\\Documents\\py bootcamp\\output.csv"

# for appending data
try:
    # with open(file=file_path, mode="w") as file: writer method
    #gives uus a new line after every method to prevent that
    with open(file=file_path, mode="w",newline="") as file:
        writer=csv.writer(file) #create an object it provides method to writing sdta in a csv file
        for i in txt_data:
            writer.writerow(i)
        print(f"csv{file_path} was created.")
except FileExistsError:
    print("That file already exists.")


