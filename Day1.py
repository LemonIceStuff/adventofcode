#Part 1

input = open("puzzle_input.txt", "r")

line = input.readline()
max_calories = 0
calories = 0
while line != "":
    if len(line)>1:
        calories += int(line)
    else:
        if calories > max_calories:
            max_calories = calories
        calories = 0
    line = input.readline()

print(max_calories)
input.close()

#Part 2

input = open("puzzle_input.txt", "r")

line = input.readline()
max_calories = [0,0,0]
calories = 0
while line != "":
    if len(line)>1:
        calories += int(line)
    else:
        max_calories.sort()
        if calories > max_calories[0]:
            max_calories[0] = calories
        calories = 0
    line = input.readline()

print(sum(max_calories))
input.close()