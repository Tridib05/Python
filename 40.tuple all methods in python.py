#count():Returns the number of occurrences of a specified value.
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))                 # Output: 3

#index():Returns the index of the first occurrence of the specified value. Raises ValueError if the value is not found.
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.index(3))                 # Output: 2

#join():Joins all elements of a tuple (of strings) into a single string with a specified separator.
tuple_of_strings = ('apple', 'banana', 'cherry')
result = ', '.join(tuple_of_strings)
print(result)                      # Output: "apple, banana, cherry"

#len():Returns the number of elements in the tuple.
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))                     # Output: 5

#max():Returns the maximum element in the tuple.
my_tuple = (10, 20, 30, 5, 15)
print(max(my_tuple))                     # Output: 30

#min():Returns the minimum element in the tuple.
my_tuple = (10, 20, 30, 5, 15)
print(min(my_tuple))                     # Output: 5
