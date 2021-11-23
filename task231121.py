# for name in ['Amalmalik', 'Zakir']
#     pass

# [] - List (mutable)
# () - Tuple (immutable)
# name = 'Amalmalik'
# name = name.upper()
# print(name.Lower())
# print(name.index('s'))
# print(name[1].isdigit())
# print(name.count('12'))
# name = name.find('J')
# name = name.strip()
# name = name.rstrip()
# name = name.lstrip()


# print(name)
# del name
# print(name)
# name[0] = 'A'

# str = ''
# i = 0

# for i, letter in enumerate('My name is Amalmalik', 2):
#     if i % 2 == 0: str += letter.upper()
#     else: str += letter.lower()
# print(str[::-1])

# str = 'Hello'
# str2 = ''

# for i in range(len(str) - 1, -1, -1):
#         str2 += str[i]

# print(str2)

# print ([elem for elem in range(10) if elem % 2 == 0])

# import random
# print(random.random())

from random import random
from random import randint

# print(int(random() * 255))
print(randint(0, 255))