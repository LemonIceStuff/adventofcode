input = open("puzzle_input.txt", "r")
start_buffer_size = 4
msg_buffer_size = 14
offset = start_buffer_size
window = ""
line = input.readline()

#Part1

# for i in range(len(line)):
#     if i < start_buffer_size: #initiate window
#         window += line[i]
#     else:
#         print(set(window))
#         if len(set(window)) == start_buffer_size:
#             print(window)
#             print(i)
#             break
#         window = window[1:] + line[i]
#     print(window)

#Part2

for i in range(len(line)):
    if i < msg_buffer_size: #initiate window
        window += line[i]
    else:
        print(set(window))
        if len(set(window)) == msg_buffer_size:
            print(window)
            print(i)
            break
        window = window[1:] + line[i]
    print(window)