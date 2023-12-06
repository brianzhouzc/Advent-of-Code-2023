# Took a shortcut. This will not work if a gear can be adjacent to more than 2 numbers.
# Luckly the input doesn't contain any gears that's adjacent to more than 2 numbers.

import re

f = open('input.txt', 'r')
lines = f.readlines()

symbol_map = [[0]*140 for i in range(140)]

sum = 0
line_num = 0
for line in lines:
    for m in re.finditer(r'\d+', line):
        num = int(m.group())
        start = m.start()
        length = m.end() - start

        valid = False
        # check left on current line
        if (start > 0 and line[start - 1] == '*'):
            if (symbol_map[line_num][start - 1] > 0):
                sum = sum + symbol_map[line_num][start - 1] * num
            else:
                symbol_map[line_num][start - 1] = num
        # check right on current line
        elif(start + length < 140 and line[start + length] == '*'):
            if (symbol_map[line_num][start + length] > 0):
                sum = sum + symbol_map[line_num][start + length] * num
            else:
                symbol_map[line_num][start + length] = num
        
        for i in range(-1, length + 1):
            if (start + i >= 0 and start + i < 140):
                # check above and below
                if (line_num > 0 and lines[line_num - 1][start + i] == '*'):
                    if (symbol_map[line_num - 1][start + i] > 0):
                        sum = sum + symbol_map[line_num - 1][start + i] * num
                    else:
                        symbol_map[line_num - 1][start + i] = num
                if(line_num < 139 and lines[line_num + 1][start + i] == '*'):
                    if (symbol_map[line_num + 1][start + i] > 0):
                        sum = sum + symbol_map[line_num + 1][start + i] * num
                    else:
                        symbol_map[line_num + 1][start + i] = num
    line_num = line_num + 1

    

print(symbol_map)
print(sum)