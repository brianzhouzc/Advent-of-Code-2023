import re

f = open('input.txt', 'r')
lines = f.readlines()

symbol_map = [ [0]*140 for i in range(142)]

line_num = 1
for line in lines:
    for m in re.finditer(r'[^.\d\s]', line):
        symbol_map[line_num][m.start()] = 1
    line_num = line_num + 1

sum = 0
line_num = 1
for line in lines:
    for m in re.finditer(r'\d+', line):
        num = int(m.group())
        start = m.start()
        length = m.end() - start

        valid = False
        # check left on current line
        if (start > 0 and symbol_map[line_num][start - 1] == 1):
            valid = True
        # check right on current line
        elif(start + length < 140 and symbol_map[line_num][start + length] == 1):
            valid = True
        
        for i in range(-1, length + 1):
            if (start + i >= 0 and start + i < 140):
                # check above and below
                if(symbol_map[line_num - 1][start + i] == 1 or symbol_map[line_num + 1][start + i] == 1):
                    valid = True
        
        #print(num, valid)
        if valid:
            sum = sum + num

    line_num = line_num + 1
        

print(sum)