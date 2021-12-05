class Command:
    def __init__(self, direction, amount):
        self.direction = direction
        self.amount = amount

commands = []
with open("inputs/day_02.txt") as stream:
    for line in stream.readlines():
        parts = line.split(" ")
        commands.append(Command(parts[0], int(parts[1])))

# Part 1

position = 0
depth = 0

for command in commands:
    if command.direction == "forward":
        position = command.amount + position
    elif command.direction == "down":
        depth = command.amount + depth
    elif command.direction == "up":
        depth = depth - command.amount

print(position * depth)

# Part 2

position = 0
depth = 0
aim = 0

for command in commands:
    if command.direction == "forward":
        position = command.amount + position
        depth = depth + command.amount * aim
    elif command.direction == "down":
        aim = command.amount + aim
    elif command.direction == "up":
        aim = aim - command.amount

print(position * depth)