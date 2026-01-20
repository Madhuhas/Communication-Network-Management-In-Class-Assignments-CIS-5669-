# Sai Madhuhas Kotini
# 2024.01.20
# operators

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print('a is in list')
else:
    print('a is not in list')

if (b in list):
    print('b is in list')
else:
    print('b is not in list')

a = 20
b = 20

if (a is b):
    print('a and b are same')
else:
    print('a and b are not same')

if (id(a) is id(b)):
    print('a and b are same identity')
else:
    print('a and b are not same identity')
