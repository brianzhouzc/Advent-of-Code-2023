import re

f = open('input.txt', 'r')
lines = f.readlines()
lookup_table = {
    'red': 12 ,
    'green': 13,
    'blue': 14
}
sum = 0

for line in lines:
    split_list = line.split(': ')
    game_num = int(split_list[0].split(' ')[1])

    sets = split_list[1].split('; ')
    invalid = False

    for set in sets:
        subsets = set.split(', ')

        invalid = False
        for subset in subsets:
            num = int(subset.split(' ')[0])
            color = subset.split(' ')[1].strip()
            
            if (num > lookup_table[color]):
                invalid = True
                break
        
        if invalid:
            break

    if not invalid:
        sum = sum + game_num

print(sum)