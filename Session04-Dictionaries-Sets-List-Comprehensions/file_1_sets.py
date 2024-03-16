'''
Sets is a data structure that holds unordered & unique value
'''

#A set can be created similar to lists, surrounded by curly braces
sample_set = {'apple', 'banana'}
print(type(sample_set))

#Data types in set: A set can include any type of data including integer, string, boolean
sample_set = {'abc', 12, True}

#To convert list to set, we can use the set constructor
sample_list = ['foo', 'bar']
print(set(sample_list))

#To check if item exists in set
print('foo' in sample_list)

#Add items in set
sample_set.add('baz')
print(sample_set)

#remove items in set
sample_set.remove('baz')
print(sample_set)

"""
Set Operations
"""

set1 = {1, 2, 3}
set2 = {1, 2}

#Subset: Test whether every element of set 1 is in set 2
result = set1.issubset(set2)
print(result)

#Union: Constuct new set with elements both from set 1 and 2
result = set1.union(set2)
print(result)

#Intersection: Set with items common in set 1 and set 2
result = set1.intersection(set2)
print(result)

#Difference: Set with elements in set1 but not in set 2
result = set1.difference(set2)
print(result)

#Symmetric Difference: Set with elements in set 1 or 2 but not both
result = set1.symmetric_difference(set2)
print(result)

## Operator vs Method
'''
Set operations can be performed by either using methods as above, or using operators such as '-' for finding the difference, the key difference being while using operators both operands / data structures should be set.
'''

set1 = [1, 2, 3]
set2 = [1, 2]

#example 1: using operator when both operand are set
difference_by_operator = set(set1) - set(set2)
print(difference_by_operator)

#example 2: using operator when 1 operand is set
#difference_by_operator = set(1) - set2
#This would fail to execute

#example 3: using method when 1 operand is set
#note that we convert the first list to set, but not the second
difference_by_method = set(set1).difference(set2)
print(difference_by_method)
