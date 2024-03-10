# Tuples are defined with parenthesis ()
print("Tuples")

print()
print('-' * 40)
print()

fixed_groceries = ('milk', 'bread', 'rice', 'tomato', 'potato')
for item in fixed_groceries:
   print(item)

print()
print('-' * 40)
print()

# The elements are accessed with square brackets []
# like for lists.
print(fixed_groceries[2])

print()
print('-' * 40)
print()

# Tuples are immutable.
# Immutable means, that once defined, the entries 
# of a tuple cannot be changed.
print("A TypeError is raised when trying to re-assign an element of a tuple")
# Uncomment the line below to see the TypeError.
# fixed_groceries[1] = 'butter'

print()
print('-' * 40)
print()

# Values can be grouped to form a single tuple.
# This is called 'Tuple Packing'.
soup = 'Onion Soup'
appetizer = 'Garlic Bread'
salad = 'Cesar Salad'
main_course = 'Chicken'
dessert = 'Chocolate Cake'
coffee = 'Espresso'

full_course_meal = (soup, appetizer, salad, main_course, dessert, coffee)
print(full_course_meal)

# The reverse operation of assigning individual elements
# of a tuple to variables is valid and is called
# 'Tuple Unpacking'

meal_1, meal_2, meal_3, meal_4, meal_5, meal_6 = full_course_meal
print(meal_1, meal_2, meal_3, meal_4, meal_5, meal_6)

print()
print('-' * 40)
print()


