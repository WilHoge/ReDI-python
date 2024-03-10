# Lists are a very useful, ordered collection of distinct objects.
# Lists are created with the square brackets []
groceries = ['milk', 'bread', 'rice', 'tomato', 'potato']

# The command for can access individual items inside the list.
for item in groceries:
  print(item)


print()
print('-' * 40)
print()
# Lists are ordered.
# ingredients contains the same elements/strings like the groceries variable,
# but in a different order. They are therefore considered unequal in Python.
ingredients = ['rice', 'tomato', 'milk', 'potato', 'bread']

if groceries != ingredients:
  print("The elements in ingredients are in a different order than in groceries.")

print()
print('-' * 40)
print()

# List elements can be accessed by index, starting from 0.
# Negative index means counting backward.

print(groceries[0])
print(groceries[2])
print(groceries[-1])

print()
print('-' * 40)
print()

# Uncomment the line below to see the error message, when trying to access
# an element index, which is outside of the range of the list:
print("Raising an IndexError when accessing an index outside of the list's range.")
# print(groceries[5])
# IndexError: list index out of range

print()
print('-' * 40)
print()

# Lists can contain any arbitrary objects.
# A list can contain another list!

notes = ['math', 1, 'german', 1.2, 'python', [1, 2, 1.4] ]
print(notes)

print()
print('-' * 40)
print()

# Lists are dynamic:
# - the size of the list will change as you modify it (use "len(list_object)" 
#   to determine the length of a list)
# - the list will use more or less memory as you create or remove elements from it.

groceries = ['milk', 'bread', 'rice']
print(f"{groceries} has length {len(groceries)}")
pasta_item = 'pasta'
groceries.append(pasta_item)
print(f"Appended {pasta_item!r} to groceries.")
print(f"{groceries} has length {len(groceries)}")
item_to_remove = 'milk'
groceries.remove(item_to_remove)
print(f"Removed {item_to_remove!r} from groceries.")
print(f"{groceries} has length {len(groceries)}")

print()
print('-' * 40)
print()

# Some useful functions for lists.
groceries = ['milk', 'bread', 'rice']

# reverse the order of a list
# The reversal is done in-place. In-place means that the new reversed list
# is stored directly in groceries. 
print("Original groceries: {}".format(groceries))
groceries.reverse()
print("Reversed groceries: {}".format(groceries))
groceries.sort() 
print("Sort the list elements lexicographically: {}".format(groceries))

print()
print('-' * 40)
print()

# Slicing
# Slicing is a method to access only certain elements of a list.
# This is accomplished by adding a colon and additional information 
# on the start, end, and step size in the square brackets:

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# same as:
# numbers = list(range(11))

print(numbers[4])
print(numbers[4:])
print(numbers[1:9:2])
print(numbers[::])
# experiment with specifying a negative start, end or interval value
print(numbers[9:1:-1])
print(numbers[9:1:-2])
print(numbers[::-1])