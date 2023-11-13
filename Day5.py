import re
input = open("puzzle_input.txt", "r")
#Matrice hauteur h largeur l
#l = 3
l=9

#For Part 1
def move(num:int,fro:int,to:int,M):
    #M[fro][i] to #[to][i]
    for number in range(num):
        crate = M[fro][-1]
        print("crate is [" + crate + "]")
        M[fro] = M[fro][:len(M[fro]) - 1] #Pop from originating column
        M[to] = M[to] + crate

#For Part2
def move_9001(num:int,fro:int,to:int,M):
    #M[fro][i] to #[to][i]
    crate = M[fro][-num:]
    print("crate is [" + crate + "]")
    M[fro] = M[fro][:len(M[fro]) - num] #Pop from originating column
    M[to] = M[to] + crate


if __name__ == '__main__':

    #Initiate matrix
    M = ["" for i in range(l)]
    line = input.readline()
    line_counter = 0
    #Remplissage de la matrice
    while "[" in line:
        column_counter = 0
        for char in line :
            column_counter += 1
            if re.findall("[A-Z]", char):
                M[column_counter//4] = char + M[column_counter//4] #//4 à cause des espaces, à l'envers pour mettre une colonne ds une liste
        line = input.readline()
        line_counter += 1
    print(M)
    input.readline()#skip de la ligne vide
    line = input.readline()
    while "move" in line :
        num = int(re.findall("move (\d+)", line)[0])
        fro = int(re.findall("from (\d+)", line)[0]) - 1
        to = int(re.findall("to (\d+)", line)[0]) - 1
        move_9001(num, fro, to, M)
        print(M)
        line = input.readline()
    result = ""
    for elem in M:
        result += elem[-1]
    print(result)