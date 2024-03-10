################
## CONDITIONS ##
################

# Often we want to run a piece of code only if certain conditions are met.
# Python allows to do that using the "if" statement. Uncomment file_1_recpa_if_else.py in the main.py file.
if True:
  print("This code prints something!")

if False:
  print("This code does not print anything!")

# The object between the keyword "if" and the ":" is called a condition, and can also be a variable or an expression. The statement is evaluated using the same rules as bool()
x = 10
if x == 10:
  print("The content of x is 10!")

y = 1
if y:
  print("The integer y is evaluated as True, so it means that the value stored is not 0.")
  

# In the code above, we run a single line of code in each if statement. But we can also run multiple lines of code, as the following example shows
if True:
  print("First line")
  print("Second line")
  x = 3 + 3 - 4
  print("Third line... and content of the variable x:",x)

# But how does Python know how many lines of code should be executed if the condition is met? Try to run the following lines of code throught the main.py file! Do you see the difference compared to the previous code?
if False:
  print("First line")
  print("Second line")
x = 3 + 3 - 4
print("Third line... and content of the variable x:",x)


"""
INSIGHT

Python uses indentation to group together different lines of code!

Since the indentation on lines 22 and 23 is the same, they form a group of code; and since their indentation is bigger than that of the if statement (line 21), they are under the scope of the if statement.
Lines 24 and 25 have the same indentation of the if statement (line 21), so they are not affected by the if statement.

We will see that the same rules for grouping lines of code apply also for other constructs and statements.
"""


# EXERCISE 1.1.: Write a program that asks the user to give a string as input and:
# Case 1) if the string contains more than 3 characters, prints the number 1
# Case 2) otherwise, prints the number 0

print()
print(('-' * 13) + ' Exercise 1.1 ' + ('-' * 13))
print()

# TODO: add your code for exercise 1 here

print()
print('-' * 40)
print()

"""
INSIGHT

With only the "if" statements introduced above, the previous exercise requires two "if" statements, one for case 1 and one for case 2. But there is a much more compact way to solve the exercise: using if..else statements!
"""

# An if..else statement, similarly to the if statement, checks a condition and:
# Case 1) if the statement is true, then runs a certain piece of code;
# Case 2) if the statement is false, then runs a different piece of code.
# Try to change the value of the variable "test" in the following example and see what happens!
test = True
if test:
  print("The value of test is True.")
else:
  print("The value of test is False.")

print()
print(('-' * 13) + ' Exercise 1.2 ' + ('-' * 13))
print()

# EXERCISE 1.2.: Solve EXERCISE 1 using an if..else statement. Much more elegant and compact solution, uh?

# TODO: add your code for exercise 2 here

print()
print('-' * 40)
print()

# To deal with more complicated conditions we can *nest* several if statements one into the other, as the following piece of code shows. Trie to change the value of first_test and second_test!
first_test  = True
second_test = True
if first_test:
  print("first_test is True.")
else:
  if second_test:
    print("first_test is False and second_test is True.")
  else:
    print("first_test and second_test are both False.")

# Once again, there is a more clean way to write the previous code, that is, using the if..elif..else statement. The previous code does the same as the following. Test it out!
first_test  = True
second_test = True
if first_test:
  print("first_test is True.")
elif second_test:
  print("first_test is False and second_test is True.")
else:
  print("first_test and second_test are both False.")

# The if..elif..else tests the conditions after the "if" and "elif" keywords one at a time, and runs the piece of code corresponding to the first true condition found.
# And if none of the conditions are true, then it runs the code corresponding to the "else" keyword.
# You can have as many "elif" as you want. Test it with the following!
warehouse_capacity = 1000
warehouse_content  = 300
if warehouse_content <= warehouse_capacity * 0.25:
  print("Space in the warehouse: more than 75%")
elif warehouse_content <= warehouse_capacity * 0.5:
  print("Space in the warehouse: more than 50%")
elif warehouse_content <= warehouse_capacity * 0.75:
  print("Space in the warehouse: more than 25%")
elif warehouse_content <= warehouse_capacity:
  print("Attention! Less than 25% space in the warehouse!")
else:
  print("Warehouse capacity exceeded!")
