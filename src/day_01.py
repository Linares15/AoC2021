depths = []
with open("inputs/day_01.txt", "r") as file:
    for line in file.readlines():
        depths.append(int(line))

number_increases = 0
for index in range(1, len(depths)):
    if depths[index] > depths[index - 1]:
        number_increases = number_increases + 1

print(number_increases)

windows = []
for index in range(0, len(depths) - 2):
    windows.append(depths[index] + depths[index + 1] + depths[index + 2])

number_increases_2 = 0
for index in range(1, len(windows)):
    if windows[index] > windows[index - 1]:
        number_increases_2 = number_increases_2 + 1

print (number_increases_2)