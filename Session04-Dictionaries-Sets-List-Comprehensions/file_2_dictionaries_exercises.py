fruits = ['mango', 'apple', 'mango', 'mango', 'apple', 'kiwi']

# Use Case: Given list of fruits count the frequency of fruits
fruit_frequency = {}
for fruit in fruits:
  if fruit not in fruit_frequency:
    fruit_frequency[fruit] = 0
  fruit_frequency[fruit] += 1

print(fruit_frequency)  #{'mango': 3, 'apple': 2, 'kiwi': 1}
"""Exercise 2"""
# Accept name and age from user and update in dict
new_dict = {"name": "xyz", "age": 0}



"""Exercise 3"""

# people / phone number
people_phone_dict = {
    'name1': 'phone1',
    'name2': 'phone2',
    'name3': 'phone3',
    'name4': 'phone4',
    'name5': 'phone5'
}

# Write a program to print all values in given format:
# "the phone number of {key} is {value}"


# Write a program to ask a name to the user if exists output the phone number if not output "user does not exists"

