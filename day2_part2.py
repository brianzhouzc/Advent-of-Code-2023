f = open('input.txt', 'r')
lines = f.readlines()
sum = 0

for line in lines:
    split_list = line.split(': ')
    game_num = int(split_list[0].split(' ')[1])

    sets = split_list[1].split('; ')

    colors = {
        'red': 0 ,
        'green': 0,
        'blue': 0
    }
    for set in sets:
        subsets = set.split(', ')

        invalid = False
        for subset in subsets:
            num = int(subset.split(' ')[0])
            color = subset.split(' ')[1].strip()
            if (num > colors[color]):
                colors[color] = num

    sum = sum + (colors['red'] * colors['green'] * colors['blue'])

print(sum)