import re

f = open('input.txt', 'r')
lines = f.readlines()

sum = 0
line_num = 0
for line in lines:
    for m in re.finditer(r'\d+', line):
        num = int(m.group())
        start = m.start()
        length = m.end() - start

        valid = False
        # check left on current line
        if (start > 0 and re.match(r'[^.\d\s]', line[start - 1])):
            valid = True
        # check right on current line
        elif(start + length < 140 and re.match(r'[^.\d\s]', line[start + length])):
            valid = True
        
        for i in range(-1, length + 1):
            if (start + i >= 0 and start + i < 140):
                # check above and below
                if (line_num > 0 and re.match(r'[^.\d\s]', lines[line_num - 1][start + i])):
                    valid = True
                if(line_num < 139 and re.match(r'[^.\d\s]', lines[line_num + 1][start + i])):
                    valid = True
        
        #print(num, valid)
        if valid:
            sum = sum + num

    line_num = line_num + 1
        

print(sum)