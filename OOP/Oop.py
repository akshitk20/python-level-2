# OOP bootcamp
s = 'abc'
print(type(s))

companies = [['NatWest', 'Bank', 10000], ['Microsoft', 'Software', 20000], ['Google', 'Software', 250000]]
c1 = ('BigCo', 'Money', 1000)
print(type(c1))


def describe_company(company):
    return f'{company[0]}  in  {company[1]}'


print(describe_company(c1))


def my_fun(companies):
    s = ''
    for company in companies:
        s = s + company[0] + ' in ' + company[1] + '\n'

    return s


print(my_fun(companies))
print(type(companies))


class Person:
    def __init__(self, first, last, shoe_size):
        self.first = first
        self.last = last
        self.shoe_size = shoe_size

    def fullname(self):
        return f'{self.first} {self.last}'

    def has_big_feet(self):
        return self.shoe_size > 44

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_shoe_size(self):
        return self.shoe_size

    def set_first(self, first):
        self.first = first


p = Person('Akshit', 'Khatri', 43)
print(type(p))
print(p.first)
print(p.fullname())
print(p.get_shoe_size())
print(p.has_big_feet())


class Company:
    def __init__(self, name, domain, employees):
        self.name = name
        self.domain = domain
        self.employees = employees


c1 = Company('BigCo', 'Money', 1000)
c2 = Company('NatWest', 'Bank', 10000)
print(c1.name)
print()


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop of {self.flavor}'


vanilla = Scoop('vanilla')
chocolate = Scoop('chocolate')
strawberry = Scoop('strawberry')
print(vanilla)


#scoops = [vanilla, chocolate, strawberry]
#for scoop in [vanilla, chocolate, strawberry]:
#    print(scoop.flavor)

class Bowl:
    MAX_SCOOPS = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            if (len(self.scoops)) >= Bowl.MAX_SCOOPS:
                break
            self.scoops.append(scoop)

    def flavors(self):
        my_list = []
        for scoop in self.scoops:
            my_list.append(scoop.flavor)
        return my_list

    def __repr__(self):
        return f'Bowl of {self.flavors()}'

    def __len__(self):
        return len(self.scoops)


b = Bowl()
b.add_scoops(vanilla)
b.add_scoops(chocolate)
b.add_scoops(strawberry, chocolate, vanilla)
print(b.flavors())
print(f'length is {len(b)}')
print(b)


class Cellphone:
    def __init__(self, number, model):
        self.number = number
        self.model = model

    def call(self):
        return f'Calling....{self.number}'

    def __len__(self):
        return len(self.number)

    def __repr__(self):
        return f'{self.number} {self.model}'


c = Cellphone('8851916194', 'One plus')
print(c.call())
print(c)
print(len(c))


class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1  # class level variables

    def __len__(self):  # dunder method to calculate length
        return len(self.name)

    def __str__(self):
        return f'Person name {self.name}'

    def __getitem__(self, index):
        return self.name[index]


print(f'Before population = {Person.population}')
p = Person('Akshit')
p1 = Person('Xyz')
print(f'After population = {Person.population}')
print(len(p))
print(p)
print(p[::3])  # skip 3 from beginning A h
print(p[3::])  # skip till index and print everything else hit
print(p[3:])  # same as above


class Employee(Person):  # inheritance
    def __init__(self, name, id_number):
        super().__init__(name)
        self.id_number = id_number