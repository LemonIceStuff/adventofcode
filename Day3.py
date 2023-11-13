#Ascii OFFSET : 71

#Deux offsets car les majs sont avant les mins dans la table ASCII
offset_min = 96
offset_maj = 64 - 26
input = open("puzzle_input.txt", "r")
line = input.readline()
diff = 0

#Part1

# def find_doublon(pocket_1: str, pocket_2: str):
#     set_1 = set(pocket_1)
#     set_2 = set(pocket_2)
#     return set_1.intersection(set_2).pop() #return value, not set
#
# if __name__ == '__main__':
# doublons = []
#
#     while line != "":
#         pocket_1 = line[:len(line) // 2]
#         pocket_2 = line[len(line) // 2:]
#         doublons.append(find_doublon(pocket_1,pocket_2))
#         line = input.readline()
#     print(doublons)
#     for doublon in doublons:
#         value = ord(doublon) - offset_min
#         if value < 0:
#             value = ord(doublon) - offset_maj
#         print(doublon + ": " + str(value))
#         diff += value
#     print(diff)

#Part 2 :

def find_badge(sack_1: str, sack_2: str, sack_3: str):
    set_1 = set(sack_1)
    set_2 = set(sack_2)
    set_3 = set(sack_3)
    return (set_1 & set_2 & set_3).pop()


if __name__ == '__main__':
    badges = []
    while line != "":
        sack_1 = line.strip()
        sack_2 = input.readline().strip()
        sack_3 = input.readline().strip()
        badges.append(find_badge(sack_1, sack_2, sack_3))
        line = input.readline()
        print('plop')
    print(badges)
    for badge in badges:
        value = ord(badge) - offset_min
        if value < 0:
            value = ord(badge) - offset_maj
        print(badge + ": " + str(value))
        diff += value
    print(diff)
