import re

max_size = 100000
input = open("puzzle_input.txt", "r")

"""

class Directory:
    def __init__(self, parent, name, files, total_size=0):
        self.parent = parent #List of Directories
        self.name = name
        self.files = files #List of Files
        self.total_size = total_size


class File:
    def __init__(self, size, name):
        self.name = name
        self.size = size


line = input.readline()
directories = []
files = []

directories.append(Directory([], "/", []))
cur_dir = directories[0]  # We start at root

#maping de tous les fichiers et dossiers:

while line != "":
    print('Current line is: ' + line.strip() + ", current dir list is " + str(len(directories)))
    if line[0] == "$":
        # Cas "cd"
        if "cd" in line:
            dir_name = re.findall('cd (.+)', line)[0]
            if dir_name == "..":
                cur_dir = cur_dir.parent[0]
                print("We are in dir: " + cur_dir.name)
            else:
                known_dir = False
                for dir in directories:
                    if dir.name == dir_name:
                        if cur_dir.name == "/":
                            cur_dir = dir
                            known_dir = True
                        elif dir.parent[0].name == cur_dir:
                            cur_dir = dir
                            known_dir = True
                # Si on a jamais vu ce directory :
                if not known_dir:
                    directories.append(Directory([cur_dir], dir_name, []))
                    cur_dir = directories[-1]
                    print("We are in dir: " + cur_dir.name)
                if cur_dir.name != "/":
                    parent_dir = cur_dir.parent[0]
                    while parent_dir.name != "/":
                        print("My parent directory is : " + parent_dir.name)
                        parent_dir = parent_dir.parent[0]
                    print("My parent directory is : " + parent_dir.name)
            line = input.readline()
        #Cas "ls"
        elif "ls" in line:
            # on scan l'input jusqu'à la prochaine commande
            line = input.readline()
            while "$" not in line and line != "":
                if "dir" in line:
                    known_dir = False
                    dir_name = re.findall('dir (.+)', line)[0]
                    for dir in directories:
                        if dir.name == dir_name:
                            known_dir = True
                    # Si on a jamais vu ce directory :
                    if not known_dir:
                        print("We discovered directory :" + dir_name)
                        directories.append(Directory([cur_dir], dir_name, []))
                else:
                    known_file = False
                    print("Current line is: " + line)
                    print(re.findall("\d+ (.+)", line)[0])
                    file_name = re.findall("\d+ (.+)", line)[0]
                    file_size = re.findall("(\d+) .+", line)[0]
                    for file in files:
                        if file.name == file_name:
                            known_file = True
                    if not known_file:
                        cur_file = File(int(file_size), file_name)
                        files.append(cur_file)
                        cur_dir.files.append(cur_file)
                line = input.readline()

# Maping des tailles de directory

for dir in directories:
    for file in dir.files:
        dir.total_size += file.size


all_size = 0
for dir in directories :
    if dir.total_size <= max_size:
        print ("Le dossier " + dir.name + " a une taille de " + str(dir.total_size))
        all_size+=dir.total_size

print("La taille totale de ces dossiers est de: " + str(all_size))
#Answer too low, we'll see next time
# get info on defauldict from collections and accumulate from itertools
#
"""
