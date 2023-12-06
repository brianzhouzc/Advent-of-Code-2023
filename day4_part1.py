import re

f = open('input.txt', 'r')
lines = f.readlines()

sum = 0
for line in lines:
    card = line.strip().split(': ')[1].split(' | ')
    winning_nums = [0] * 100
    for wnum in re.findall(r'\d+', card[0]):
        winning_nums[int(wnum)] = 1

    matches = -1
    for pnum in re.findall(r'\d+', card[1]):
        if (winning_nums[int(pnum)] == 1):
            matches = matches + 1
    
    if (matches > -1):
        sum = sum + pow(2, matches)

print(sum)