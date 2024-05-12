"""
Read a file with a number on each line. Print the sum of those numbers.
"""

file = open('data/input.txt')  # opening the file
contents = file.read()
print(contents)
file.close()
# file.read() will read the entire file so second time it will not print anything since cursor at last
# to reset the cursor use file.seek(0) this will set cursor to begining
sum = 0
with open("data/input.txt") as file:  # automatically closes the file
    for line in file.readlines():
        sum += int(line)
print(f"Sum is {sum}")
