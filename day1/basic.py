# printing basic hello world

print("Hello World"+" HI")  # print command
print('hi')
print("""
sadad
fafaf
afaf
""")
a = 4
b = 2
c = 'ram'
if a < b:
    print('5 is less than 2')
else:
    print('5 is greater than 2')

a = '5'
print(type(a))

# variables = snake_case
# Class = camelCase
print(a)

# Type Casting
a = 6
print(float(a))

# list
ab = ['mac', 'soch', 'pn',]
ab[0] = 'gcs'
print(ab[0])
ab.append('wrc')
print(ab[3])
ab.remove(ab[2])
print(ab[2])

# list
# a = ['ram', 'shyam', 'hari']

# tuple type is a constant type of list
# a = ('ram', 'shyam', 'hari')

# set
# a = {'mac', 'ram', 'shyam', 'hari'}

# dict type

ba = {"name": "sita", "address": "nadipur"}
print(ba["address"])

if a == b:
    print(a)

else:
    print('not equal')

# loop
a = range(1, 15, 2)
for n in a:
    print(n)

count = 1
while count < 5:
    print(count)
    count += 1
