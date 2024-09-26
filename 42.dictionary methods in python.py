#get():Returns the value for the specified key if it exists, otherwise returns None (or a specified default).
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('a'))                    # Output: 1
print(my_dict.get('c', 'Not Found'))            # Output: Not Found

#items():Returns a view object that displays a list of a dictionary's key-value tuple pairs.
my_dict = {'a': 1, 'b': 2}
print(my_dict.items())                # Output: dict_items([('a', 1), ('b', 2)])

#keys():Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())                 # Output: dict_keys(['a', 'b'])

#values():Returns a view object that displays a list of all the values in the dictionary.
my_dict = {'a': 1, 'b': 2}
print(my_dict.values())               # Output: dict_values([1, 2])

#len():Returns the number of items (key-value pairs) in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
length = len(my_dict)
print(length)                         # Output: 3

#fromkeys():Creates a new dictionary from the given keys and a value.
keys = ('a', 'b', 'c')
new_dict = dict.fromkeys(keys, 0)
print(new_dict)                       # Output: {'a': 0, 'b': 0, 'c': 0}

#clear():Removes all items from the dictionary.
my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)                        # Output: {}

#copy():Returns a shallow copy of the dictionary.
original = {'a': 1, 'b': 2}
copy_dict = original.copy()
print(copy_dict)                      # Output: {'a': 1, 'b': 2}

#pop():Removes the specified key and returns the corresponding value. If the key does not exist, it raises a KeyError.
my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')
print(value)                     # Output: 1
print(my_dict)                       # Output: {'b': 2}

#popitem():Removes and returns the last key-value pair as a tuple. Raises KeyError if the dictionary is empty.
my_dict = {'a': 1, 'b': 2}
item = my_dict.popitem()
print(item)                      # Output: ('b', 2)
print(my_dict)                       # Output: {'a': 1}

#del:Deletes a specified key from the dictionary. If the key does not exist, it raises a KeyError.
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']
print(my_dict)                      # Output: {'a': 1, 'c': 3}

#max():Returns the maximum key from the dictionary. By default, it compares keys, but you can also specify a function for custom comparisons.
my_dict = {'a': 1, 'b': 2, 'c': 3}
max_key = max(my_dict)
print(max_key)                   # Output: 'c'

#min():Returns the minimum key from the dictionary. Similar to max(), you can specify a function for custom comparisons.
my_dict = {'a': 1, 'b': 2, 'c': 3}
min_key = min(my_dict)
print(min_key)                      # Output: 'a'

#sum():Calculates the sum of all values in the dictionary. You can specify a start value (default is 0).
my_dict = {'a': 1, 'b': 2, 'c': 3}
total = sum(my_dict.values())
print(total)                      # Output: 6

#setdefault():Returns the value of a key if it is in the dictionary. If not, it inserts the key with a specified value.
my_dict = {'a': 1}
value = my_dict.setdefault('b', 2)
print(value)                     # Output: 2
print(my_dict)                       # Output: {'a': 1, 'b': 2}

#update():Updates the dictionary with the elements from another dictionary or from an iterable of key-value pairs.
my_dict = {'a': 1}
my_dict.update({'b': 2, 'c': 3})
print(my_dict)                       # Output: {'a': 1, 'b': 2, 'c': 3}

