"""
A program that takes a letter and outputs a text file of
all of the countries that start with that letter
"""
# used both list and dictionaries
# Todo: Read data/countries.txt and save all countries
#my_list = []
#with open("data/countries.txt") as file:
#    for line in file.readlines():
#        my_list.append(line.strip())  # remove new line
#print(my_list)
my_list = {}
with open("data/countries.txt") as file:
    for line in file.readlines():
        letter = line[0].upper()
        if letter not in my_list:
            my_list[letter] = []
        my_list[letter].append(line.strip())
# Get user to provide a letter
letter = input('Number of countries that start with letter: ').upper()
number = 0
#countries = []
countries = my_list.get(letter, [])
#for country in my_list:
#    if country[0] == letter:
#        countries.append(country)
# Todo: Print the number of countries that start with the letter
print(f"No of countries {len(countries)}")
print(f"Countries are {countries}")
# Todo: Create text file that lists the countries starting with the letter
with open(f"data/{letter}_countries.txt", 'w') as file:
    for country in countries:
        file.write(country + "\n")