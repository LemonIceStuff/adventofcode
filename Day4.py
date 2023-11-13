import re
input = open("puzzle_input.txt", "r")

def find_ranges(text:str):
    range_1 = re.findall("(\d+)-(\d+),", text)[0]
    range_2 = re.findall(",(\d+)-(\d+)", text)[0]
    return(range_1, range_2)

def is_contained(range_1: tuple, range_2: tuple):
    #range_1 : [a - b]
    #range_2 : [c - d]
    a = int(range_1[0])
    b = int(range_1[1])
    c = int(range_2[0])
    d = int(range_2[1])
    return (a - c )*(d - b) >= 0 #If (a>=c et d>=b) ou (a<=c et d<=b)

def is_overlap(range_1: tuple, range_2: tuple):
    #range_1 : [a - b]
    #range_2 : [c - d]
    a = int(range_1[0])
    b = int(range_1[1])
    c = int(range_2[0])
    d = int(range_2[1])
    return (a <= c <= b) or (a <= d <= b) or (c <= a <= d) or (c <= b <= d)

if __name__ == '__main__':

#Part1
    # line = input.readline()
    # overlap = 0
    # while line != "":
    #     (range_1, range_2) = find_ranges(line)
    #     if is_contained(range_1, range_2):
    #         overlap += 1
    #     line = input.readline()
    # print(overlap)
#Part2
    line = input.readline()
    overlap = 0
    while line != "":
        (range_1, range_2) = find_ranges(line)
        if is_overlap(range_1, range_2):
            print(range_1,range_2)
            overlap += 1
        line = input.readline()
    print(overlap)
