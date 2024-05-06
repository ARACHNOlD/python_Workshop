a = int(input("Enter the value of a"))
b = int(input("Enter the value of a"))
try:
    print(a/b)
except ZeroDivisionError:
    print('b cannot be zero')
except ValueError:
    print('a and b is no of desired type')

finally:
    print('done')
