#palindrome = "race Car"
import pickle
import time


# list comprehension
def is_palindrome(s):
    reverse = [c.lower() for c in s if c.isalpha()]
    print(reverse)
    print(reverse == reverse[::-1])  # reverse[::-1] reversing the string


is_palindrome('race Car')
is_palindrome('hello')


# set comprehension
def get_primes(n):
    big_set = set(range(2, n))
    comp_set = {j for i in range(2, n)
                for j in range(i * i, n, i)}
    return big_set - comp_set


print(get_primes(1000))

# formatting text
x, y, z = 10, 20, 30
print('x = %d , y = %d and z = %d' % (x, y, z))  # %d = integer
x, y, z = 100, 200, 300
print('x = %d , y = %d and z = %d.' % (x, y, z))

for x in [-5, 0.2, 125.7, 3.141592, -12.007, ]:  # %f = float
    print('  %8.3f' % x)

n = 100000033
print(format(n, ','))  # thousand place separate
print(format(3141.5926, '9,.2f'))

for x in [-5, 0.2, 125.7, 3.141592, -12.007, ]:  # format method
    print('  {:8.3f}'.format(x))

# multidimensional list
mat = [[1, 2, 4], [1, 5, 6], [7, 8, 9]]
print(mat)

mat1 = [[0] * 20] * 10  # 10 references to one row not correct way
print(mat1)
mat1[0][3] = 100
print(mat1[1][3])
print(mat1[5][3])

mat2 = []
for i in range(10):  # 10X20 with initial value 0
    mat2.append([0] * 20)
print(mat2)

mat3 = [[0] * 20 for i in range(10)]
print(mat3)

mat4 = [[1, 2, 3] * 5 for _ in range(10)]  # _ can be used for i
print(mat4)

mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(mult_table)

for i in range(5):
    for j in range(5):
        print('%3d' % mult_table[i][j], end='')
    print('\n')

# dictionaries
magic_dict = {}
magic_dict['pi'] = 3.141592
magic_dict['phi'] = 1.6180
print(magic_dict)

# count no of words in string
w_dict = {}
s = "Hello my name is Hello my name"
for word in s.split():
    if w_dict.get(word):
        w_dict[word] += 1
    else:
        w_dict[word] = 1
print(w_dict)


def make_dict(s):
    w_dict = {}
    word_list = s.split()
    for word in word_list:
        w_dict[word] = w_dict.get(word, 0) + 1
    return w_dict


print(make_dict("Hello my name is Hello my name"))

dc = make_dict("Hello my name is Hello my name")
a_list = [(v, k) for k, v in dc.items()]
a_list.sort(reverse=True)
print(a_list)
for i in a_list:
    print(i[1], '\t', i[0])
words = ""
with open('example.txt') as file:
    words = file.read()
print(make_dict(words))


#def generator():
#    yield 1
#    yield 2
#    yield 3


#print(generator().send(1))


def print_msg():
    print('Hi, my name is Brian O')
    print('I live in 123 Main street')
    print('Bellevue WA')


def my_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        rv = func(*args, **kwargs)
        t2 = time.time()
        print('Args are', args)
        print('KW args are:', kwargs)
        print('Function took', t2 - t1, 'mss.')
        return rv

    return wrapper


#dec = my_decorator(print_msg())
@my_decorator
def do_stuff(a=1, b=10, c=100):
    print('a = %s, b = %s, c = %s' % (a, b, c))
    return a + b + c


do_stuff(1, 2, c=3000)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        s = '(' + str(self.x) + ','
        s += str(self.y) + ')'
        return s

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5


pt1 = Point(1, 2)
pt2 = Point(75, 0)
print('Distance between %s and %s is %s ' % (pt1, pt2, pt1.dist(pt2)))
print(pt1.dist(pt2))


class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def __str__(self):
        return ('(' + self.name + ',' + self.job
                + ',' + str(self.salary) + ')')


emp1 = Employee('Bill G', 'CEO', 11)
emp2 = Employee('CR', 'Writer', 7)
emp3 = Employee('Steve Balmer', 'President', 10)
print(emp1)
print(emp2)
print(emp3)


def create_list():
    rec_list = []
    while True:
        name_s = input('Enter name: ')
        if not name_s:
            return rec_list
        job_s = input('Enter job title: ')
        salary = int(input('Salary level: '))
        emp_rec = Employee(name_s, job_s, salary)
        rec_list.append(emp_rec)


a_list = create_list()
for i in a_list:
    print(i)


def load_data(fname):
    with open(fname, 'rb') as f:
        a_list = pickle.load(f)
    for i in a_list:
        print(i)


def save_data(fname):
    with open(fname, 'wb') as f:
        pickle.dump(a_list, f)


save_data('junk.bin')
load_data('junk.bin')