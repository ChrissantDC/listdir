# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# list_dir [path] [ouput_filename]
# list_dir d:\downloads my_output.csv
#
# Develop an application with the following requirements:
#
# Take the path of a directory and list the files (recursively)
# Output the files in a CSV (comma separated value) file.
# Here are the columns of the CSV: parent path, filename, filesize, sha1, md5
# Here's what a row should look like: "D:\Downloads","setup.exe",1048576, sha1-here, md5-here
# The output filename should be set by the user using command line arguments
# Commit your code in GitHub under the project listdir. Post the link to the project here

import glob
import hashlib
import pathlib
import os

file_path = []
txt_files = []
files_size = []
sha1 = []
md5 = []


# STEP 1: Get files and store them to array
# STEP 2: Get path of each file from the array
# STEP 3: Get file name
# STEP 4: Get Sha1
# STEP 5: Get md5
# STEP 6: Follow the format and save to csv


def get_file():
    # This function will list down the file names in an array

    for file in glob.glob("*.txt"):
        txt_files.append(file)


# print(txt_files)


def print_path(path):
    # This function will collect the paths of the file
    file_path.append(str(pathlib.Path(path).parent.resolve()))


def hash_file(filename):
    # This function returns the SHA-1 hash
    # of the file passed into it

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as hashfile:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = hashfile.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    sha1.append(h.hexdigest())
    return h.hexdigest()


def file_size(filename):
    file_name = os.path.getsize(filename)
    files_size.append(file_name)
    return file_name


def get_md5():
    with open("A.txt", "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    md5.append(file_hash.hexdigest())  # to get a printable str instead of bytes


get_file()
for file in txt_files:
    print_path(file)
    file_size(file)
    hash_file(file)
    get_md5()

with open(input("Enter Desired File Name: "), "w") as Test_Write:
    first_column = "Parent path \t filename \t filesize \t sha1 \t md5"
    row = ""
    i = 0
    for i in range(len(txt_files)):
        row += file_path[i] + ",\t" + txt_files[i] + ",\t" + str(files_size[i]) + ",\t" + sha1[i] + ",\t" + md5[i] + "\n"
    Test_Write.write(row)

# print(str(txt_files))
# print(file_path)
# print(sha1)
# for files in txt_files:
#     fs = file_size("A.txt")
# print("File Size is :", fs, "bytes")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
