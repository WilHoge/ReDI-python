"""
Exercises related to sets
"""

python_hybrid_class = ['foo', 'bar']
ui_ux_class = ['bar', 'baz']

"""UseCase""" 
#Given a list of students in 2 classes, print overall unique students

overall_students = set(python_hybrid_class).union(ui_ux_class)
print(overall_students)

#UseCase: Given a list of students in 2 classes, find students attending both classes
students_attending_all_classes = set(python_hybrid_class).intersection(
    ui_ux_class)
print(students_attending_all_classes)

"""Exercise 1"""

set_1 = {"A", "B", "E", "J", "L", "O", "K", "Y", "N"}
set_2 = {"c", "B", "D", "N", "P", "Y", "A", "J", "M"}

#print common elements in both sets
common_elements = 
print("Common elements are:", )

#print total number of number unique alphabets from both set
unique_alphabets = 
print("The total number of unique alphabets is:", )

#print alphabets that are in set2 but not in set1
set_alphabets = 
print("Alphabets in set2 that are not in set1:", )
