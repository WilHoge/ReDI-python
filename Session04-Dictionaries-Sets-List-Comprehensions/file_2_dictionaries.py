"""
Dictionaries are data structure used to store key: value pairs, also known by hashmaps in some languages
"""

sample_dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(sample_dict)

# Have unique keys, if multiple keys with same content is added the value will be overwritten
multiple_keys = {'brand': 'value1', 'brand': 'value2'}
print(multiple_keys)  # {'brand': 'value2'}

"""Accessing items"""
# items can be access by referring to key name
print(sample_dict['brand'])

#However if the item does not exist the following line would return an error
#print(sample_dict['price'])

# items can also be accessed by using the get method, this would not throw an error if the key does not exists, instead will return None
print(sample_dict.get('price'))  # None

#Getting list of keys
print(sample_dict.keys())

#Getting list of values
print(sample_dict.values())

# items() method: this would return each item in dictionary as tuples in list
print(sample_dict.items())
# sample_dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# check if key exists in dict
print('brand' in sample_dict)

"""Update values in dict"""

sample_dict[
    'year'] = 2018  # this is usually useful when only 1 value needs to be updated in a dict
sample_dict.update({
    'year': 2018,
    'brand': 'bmw'
})  # this is useful when multiple values need to be updated

"""Adding items in dict"""
sample_dict['color'] = 'red'  #similar to above useful for adding 1 item

sample_dict.update({'color': 'red'})  # useful for adding multiple items
"""Removing items in dict"""

sample_dict.pop("color")

"""Delete Dict"""
sample_dict.clear()

"""Looping through Dict"""
# print all keys in dict
for x in sample_dict:
  print(x)

#print all values in dictionary
for x in sample_dict:
  print(sample_dict[x])

#printing key and value in dict
for key, value in sample_dict.items():
  print(key, ":", value)

"""Indexing"""
# Its not possible to get dictionary value by index, for eg in list we do list[1], but implementing dict[1] will likely cause an error if the key "1" does not exist.

"""Key by value"""
# There is no easy way to find a key by looking up a value, dictionaries are meant to be usually used other way around. Also because multiple keys could have the same values, the only possible way then is to loop through the dictionary.

reverse_dict = {'key1': 'value1', 'key2': 'value1', 'key3': 'value3'}
key_for_value1 = None
for k, v in reverse_dict.items():
  if v == 'value1':
    key_for_value1 = k

print(key_for_value1)
