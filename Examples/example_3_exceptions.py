class CustomException(Exception):
    pass


try:
    int('five')
    print('Success!')
except ValueError as e:
    print("Fail!")
    print(e)

print('Got here')

int('1.5')  # Run fails with exit code 1
print("Didn't get here")

num = int(input("Enter Number : "))
try:
    inverse = 1 / num
except ZeroDivisionError as e:
    print("Fail")
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print()
