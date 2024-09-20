#append(): Adds an item to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)                                   # Output: [1, 2, 3, 4]

#extend(): Adds all elements of an iterable (e.g., list, tuple) to the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)                                   # Output: [1, 2, 3, 4, 5]

#insert(): Inserts an item at a specific index.
my_list = [1, 2, 3]
my_list.insert(1, 'a')                           # Insert 'a' at index 1
print(my_list)                                   # Output: [1, 2, 'a', 3]

#remove(): Removes the first occurrence of a specific item.
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)                                    # Output: [1, 3, 2]

#pop(): Removes and returns an item at a given index (or the last item if index is not specified).
my_list = [1, 2, 3]
popped_item = my_list.pop()
print(popped_item)                                # Output: 3
print(my_list)                                    # Output: [1, 2]

# With index
popped_item = my_list.pop(0)
print(popped_item)                                # Output: 1
print(my_list)                                    # Output: [2]

#clear(): Removes all items from the list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)                                    # Output: []

#index(): Returns the index of the first occurrence of a specific item.
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)                                      # Output: 1

#count(): Returns the number of occurrences of a specific item.
my_list = [1, 2, 3, 2, 2]
count = my_list.count(2)
print(count)                                      # Output: 3

#sort(): Sorts the list in ascending (default) or specified order.
my_list = [3, 1, 2]
my_list.sort()
print(my_list)                                    # Output: [1, 2, 3]

# Sort in descending order
my_list.sort(reverse=True)
print(my_list)                                    # Output: [3, 2, 1]

#reverse(): Reverses the order of the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)                                    # Output: [3, 2, 1]

#copy(): Returns a shallow copy of the list.
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)                                   # Output: [1, 2, 3]

#sort() with key: Sorts using a custom key function.
my_list = ["apple", "banana", "cherry"]
my_list.sort(key=len)                             # Sort by length of the string
print(my_list)                                    # Output: ['apple', 'cherry', 'banana']
