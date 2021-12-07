lines = None
with open('day07/input.txt') as f:
    lines = f.readlines()

line = lines[0]
arr = list(map(lambda s: int(s), line.split(",")))

min = 99999999999999
for pos in range(1500):
    sum = 0
    for x in arr:
        sum += abs(x - pos)

    if sum < min: min = sum

print(min)
