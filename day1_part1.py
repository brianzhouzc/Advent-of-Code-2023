import re

f = open('code.txt', 'r')
lines = f.readlines()

sum = 0
for line in lines:
	digits = re.findall('\d', line)
	sum = sum + int(digits[0]) * 10 + int(digits[-1])

print(sum)