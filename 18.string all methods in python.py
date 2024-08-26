#len(): Returns the length of string
text = "Hello World"
print(len(text))                            #Output: 11

#count(): Counts the number of times a substring occurs
text = "Hello World"
print(text.count("o"))                      #Output: 2

#find(): Find the index of a substring
text = "Hello World"
index = text.find("World")
print(index)                                #Output: 6

#index(): Finds the first occurrence of a substring and returns its index
text = "Hello World"
print(text.index("W"))                      #Output: 6

#isalpha(): Checks if all characters in a string are alphabetic
text = "Hello"
print(text.isalpha())                       #Output: True

#isalnum(): Checks if all characters in a string are alphabetic(a-z,A-Z) or digits(0-9)
text = "Hello123"
print(text.isalpha())                        #Output: False

#isdigit(): Checks if all characters in a string are digits
text = "123"
print(text.isdigit())                        #Output: True

#lower(): Converts all characters to lowercase
text = "Hello World"
print(text.lower())                          #Output: hello world

#upper(): Converts all characters to uppercasePython
text = "Hello World"
print(text.upper())                          #Output: HELLO WORLD

#strip(): Removes leading and trailing whitespace
text = "   Hello World   "
print(text.strip())                          #Output: Hello World

#lstrip(): Removes leading whitespace from the string
text = "   Hello World"
print(text.lstrip())                         #Output: Hello World

#rstrip(): Removes trailing whitespace from the string
text = "Hello World   "
print(text.lstrip())                         #Output: Hello World

#replace(): Replaces a substring with another
text = "Hello World"
print(text.replace("World", "Python"))            #Output: Hello Python

#split(): Splits a string into a list of substrings based on a delimiter
text = "Hello, World"
print(text.split(","))                       #Output: ['Hello','World']

#join(): Joins a list of strings into a single string using a specified delimiter
words = ["Hello", "World"]
print(", ".join(words))                      #Output: Hello, World

#title(): Capitalizes the first letter of each word
text = "hello world"
print(text.title())                          #Output: Hello World

#startswith(): Checks if a string starts with a specific substring
text = "Hello World"
print(text.startswith("Hello"))              #Output: True

#endswith(): Checks if a string ends with a specific substring
text = "Hello World"
print(text.endswith("World"))                #Output: True

#partition(): Splits the string into three parts: the part before the separator, the separator itself, and the part after the separator
text = "Hello, World!"
print(text.partition(","))                   #Output: ('Hello', ',', ' World!')
