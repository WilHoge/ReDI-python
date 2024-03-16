"""List comprehension: shorter syntax to create lists"""

fruits = ['apple', 'banana', 'cherry', 'mango']
fruit_list = [x for x in fruits]
print(fruit_list)

"""Useful for adding simple filters on list"""
fruit_mango_list = [x for x in fruits if x == 'mango']
print(fruit_mango_list)
