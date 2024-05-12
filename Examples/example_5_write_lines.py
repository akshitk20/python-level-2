
with open('data/output.txt', 'w') as file:
    lines = ['a', 'b', 'c', 'd']
    file.writelines(lines)  # write all lines in once like list without spaces
    file.write('\n')
    for line in lines:
        file.write(line + '\n')  # write each line using single line character