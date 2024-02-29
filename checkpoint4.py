from decimal import Decimal
import math

# Exercise 1
# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (6, 7, 8, 9, 10)

# Float
my_float = 3.14

# Integer
my_integer = 42

# Decimal

my_decimal = Decimal('3.14159')

# Dictionary
my_dictionary = {'bikes': 3, 'cars': 5, 'trucks': 2}


# Exercise 2
my_float = 3.14

print(math.ceil(my_float))


# Exercise 3
my_float = 3.14

square_root = math.sqrt(my_float)
print(math.sqrt(square_root))


# Exercise 4
my_dictionary = {'apple': 3, 'banana': 5, 'orange': 2}

first_key = list(my_dictionary.keys())[0]
first_value = my_dictionary[first_key]

print(first_key, first_value)


# Exercise 5
my_tuple = (6, 7, 8, 9, 10)

second_element = my_tuple[1]

print(second_element)


# Exercise 6
my_list = [1, 2, 3, 4, 5]

my_list.append(6)

print(my_list)


# Exercise 7
my_list = [1, 2, 3, 4, 5]

my_list[0] = 8

print(my_list)


# Exercise 8
my_list = ['xiaomi', 'samsung', 'apple', 'huawei']

my_list.sort()

print(my_list)


# Exercise 9
my_tuple = (1, 2, 3, 4, 5)

new_element = 6

my_tuple_new = my_tuple + (new_element,)

print(my_tuple_new)
