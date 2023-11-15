import re

input = open("puzzle_input.txt", "r")

class Directory:
    def __init__(self, parent, name, files):
        self.parent = parent
        self.name = name
        self.files = files


class File:
    def __init__(self, size, parent, name):
        self.parent = parent
        self.name = name
        self.size = size


line = input.readline()
directory = []
files = []

directory.append(Directory("", "/", ""))
cur_dir = directory[0] #We start at root

while line != "":
    if line[0] == "$":
        if "cd" in line :
            cur_dir = re.findall("cd (.+)", line)



    line = input.readline()