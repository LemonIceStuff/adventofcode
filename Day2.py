#Part 1
#A == Pierre
#B == Papier
#C == Ciseaux

input = open("puzzle_input.txt", "r")

line = input.readline()
score = 0
trad_score = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3
}
while line!= "":
    # juste pour compter le score du symbole utilisé
    score += ord(line.strip("\n")[-1]) - 87
    score += trad_score[line.strip("\n")]

    line = input.readline()

print(score)


#Part 2
#A == Pierre
#B == Papier
#C == Ciseaux

input = open("puzzle_input.txt", "r")

line = input.readline()
score = 0
trad_signe = {
    "X":0,
    "Y":3,
    "Z":6
}

while line!= "":
    print("la ligne:" + line)
    # juste pour compter le score du symbole utilisé
    score += trad_signe[line.strip("\n")[-1]]
    if line.strip("\n")[-1] == "X":
        print(chr((ord(line.strip("\n")[0]) - 65 - 1) % 3 + 65))
        score += (ord(line.strip("\n")[0]) - 65 - 1) % 3 + 1
    elif line.strip("\n")[-1] == "Y":
        print(ord(line.strip("\n")[0]) - 64)
        score += ord(line.strip("\n")[0]) - 64
    else:
        print(chr((ord(line.strip("\n")[0]) - 65 + 1) % 3 + 65))
        score += (ord(line.strip("\n")[0]) - 65 + 1) % 3 + 1
    line = input.readline()

print(score)
