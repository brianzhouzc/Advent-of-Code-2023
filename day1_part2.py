import re

f = open('code.txt', 'r')
lines = f.readlines()
lookup_table = {
    '1': 1 ,
    '2': 2 ,
    '3': 3 ,
    '4': 4 ,
    '5': 5 ,
    '6': 6 ,
    '7': 7 ,
    '8': 8 ,
    '9': 9 ,
    'one': 1 ,
    'two': 2 ,
    'three': 3 ,
    'four': 4 ,
    'five': 5 ,
    'six': 6 ,
    'seven': 7 ,
    'eight': 8 ,
    'nine': 9
}

sum = 0
for line in lines:
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    sum = sum + lookup_table[digits[0]] * 10 + lookup_table[digits[-1]]
    print(digits)

print(sum)