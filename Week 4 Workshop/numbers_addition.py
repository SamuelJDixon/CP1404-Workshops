__author__ = "Samuel Dixon"

file = open('numbers.txt', 'r')
total = 0

for line in file:
    total = total + int(line)

print(total)