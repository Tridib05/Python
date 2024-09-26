#creating dictionary
dict = {
    'name': 'Tridib',
    'age': 25,
    'city': 'Haldia'
}

#accessing dictionary
print(dict['name'])                     # Output: Tridib
print(dict['age'])                      # Output: 25


#nested dictionary
students = {
    'student1': {
        'name': 'Alice',
        'age': 25,
        'courses': ['Math', 'Physics']
    },
    'student2': {
        'name': 'Bob',
        'age': 22,
        'courses': ['Biology', 'Chemistry', 'Computer', 'Math']
    }
}
print(students['student1']['name'])                    # Output: Alice
print(students['student2']['courses'])                 # Output: ['Biology', 'Chemistry']
print(students['student2']['courses'][3])              #Output: Math
