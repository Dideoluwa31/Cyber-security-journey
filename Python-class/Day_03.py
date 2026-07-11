#Iterable objects --> these are objects that holds multiple values and we access these values either using keys or indexes.
# Tuple --> ()
# List --> []
# Dictionary --> {}


# Tuple
#Tuples are created using the normal bracket
# They cannot be changed after creation
# The tuple is accessed using an index

my_first_object = ('Caleb', 20.34, 20, True, False, 45, 22.1, 'Fire')
type(my_first_object)

# forward index
print(my_first_object[0])
print(my_first_object[1])
print(my_first_object[2])

# Backward index
print(my_first_object[-1])
print(my_first_object[-2])
print(my_first_object[-3])


# Forward range index
print(my_first_object[0:3]) # [start:stop]
print(my_first_object[1:3]) # [start:stop]

print('Caleb' in my_first_object)

my_tuple = (1, 2, 3, 4, 5, 6)
#Forward range index
print(my_tuple[0:3]) # [start:stop]
print(my_tuple[2:3]) # [start:stop]
print(my_tuple[3:3]) # [start:stop]

print(my_tuple[::1]) # [start:stop:step]
print(my_tuple[1:5:2]) # [start:stop:step]

# Backward range index
print(my_tuple[::-1]) #[start: stop: step]
print(my_tuple[:-5:-1]) # #[start: stop: step]
# start --> not given defaults to the beginning
# stop = - converts the positive index(1) value 2 [boundary marker, never comes out as a result. ]
# step = --> takes one backward step

print(my_tuple[:-3])
print(my_tuple[0:])
#List 
#Lists are created usingSquare brackets
# they can be changed after creation
# they are called using indexes

countries = ["Nigeria", "Argentina", "Uganda", "Togo", "Chad", "Niger", "Japan"]
type(countries)

#forward index
print(countries[2])

#Backward index
print(countries[-6])

# Forward range index
print(countries[::2])


#backward range index 
print(countries[::-3])

#Adding a value to a list
countries.append("Mexico")
print(countries)
# Adding a list to a list

countries.extend(["Morocco", "India", "China", "Spain" ])
# Create a list of 5 students. print the first student, the last student and the total number number of students
# 1. Create a list of students
# 2. print the first name in the list
# 3. Print the last name in the list
# 4. Print how many names are in the list

#firstname: student1
students = ["Ofure", "Ore", "Juliet", "Onyiye", "Praiz"]

print(f"Firstname: {students[0]}")
print(f"Lastname: {students[-1]}")
print(f"Total Students: {str(len(students))}")

print(len(students))
print(len(countries))
print(len("Ore"))
for i in students:
    print(i)

name = "Ore"
for i in name:
    print(i)
