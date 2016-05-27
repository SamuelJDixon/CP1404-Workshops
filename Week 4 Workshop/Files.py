__author__ = "Samuel Dixon"

name = input("Enter your name: ")
file = open('name.txt', 'w')
print(name, file=file)
file.close()