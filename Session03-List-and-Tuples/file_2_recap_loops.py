###########
## LOOPS ##
###########

# Take the following piece of code.
print("Printing number... 1")
print("Printing number... 2")
print("Printing number... 3")
print("Printing number... 4")
print("Printing number... 5")
print("Printing number... 6")
print("Printing number... 7")
print("Printing number... 8")
print("Printing number... 9")
print("Printing number... 10")

# This code is very redundant... We basically want to print the same string, except for the number appearing at the end. Is there a more elegant/more compact way to do this?
# Indeed there is! We can use a while loop! Try to run the following code.
current_number = 1
max_printed_number = 10
while current_number <= max_printed_number:
  print("Printing number...", current_number)
  current_number += 1   # This is just a shorthand for current_number = current_number + 1

"""
INSIGHT

What is happening here? After the keyword "while" we have a condition (current_number <= 10). And after the colon, similarly to an if statement, we find a piece of code (lines 22 and 23).

When we run the code, what happens is that
(1) the program checks whether the condition (current_number <= 10) is true, and if this is the case
(2) it runs the piece of code in lines 22 and 23, and then
(3) the programs start start again from point (1)
And what if the condition is false in point (1)? Then the program does not run the code and stops checking the condition.

In a nutshell: the program keeps running lines 22 and 23 while the condition holds true.
"""

# EXERCISE 2.1.: Try to change the initial values of current_number and max_printed_number in the code above and see what happens!

print()
print(('-' * 13) + ' Exercise 2.1 ' + ('-' * 13))
print()

# TODO: add your code for exercise 1 here

print()
print('-' * 40)
print()

# If you played around enough with the values in the previous exercise, you probably noticed two things:
# -> Sometimes the program does not run the code in the while statement. This happens when the condition is not true to start with. Check the following code!
while False:
  print("Too bad, this text will never see the light of day!")
# -> Sometimes the program does not terminate. This happens when the condition holds true indefeinitely. Check the following two examples, and be sure to stop the execution of the code manually! (Big Stop button)

# while True:
#   print("This text will be printed until the end of time!")

# negative_number = -5
# while negative_number < 0:
#   print("negative_number is still negative...")
#   negative_number -= 1    # Shorthand for negative_number = negative_number - 1


# Notice that we might not be able to tell how many times the code in the while statement will be executed. For example, in the following piece of code, the user decides how many times the text is printed!
user_input = input("How many lines should be printed?: ")
lines_to_print = int(user_input)  # input provides a string, so we need to turn it into an int
lines_printed = 0
while lines_printed < lines_to_print:
  print("This is a line!")
  lines_printed += 1

print()
print('-' * 40)
print()

# One last remark: the while statement is *one* way to loop code in python. But there are more ways to do that!
# For example the following code, using the for statement, is another way to eliminate the redundancy in the initial example
for current_number in range(1,11):
  print("Printing number...", current_number)

# How does this work? After the keyword "for" we provide a variable (in this case current_number). Then the code in line 71 is run several times, every time with a different value of current_number.
# And how is the value of current_number determined at every iteration of the code? To answer this question we need to know more about range(1,11)... But this is material for the next lecture! :)

# EXERCISE 2.2.: Create and print the following number sequences using range():
# 1. all numbers from 3 to (including) 15 (e.g.: 3, 4, 5, ... , 15)
# 2. all number divisible by 5 from 0 to (including) 100 (e.g.: 5, 10, 15, ... , 100)
# 3. all numbers from 10 counting down to (including) 1 (e.g.: 10, 9 , ... , 1)

print()
print(('-' * 13) + ' Exercise 2.2 ' + ('-' * 13))
print()

# TODO: add your code for exercise 2 here
sequence = range(0)
print(list(sequence))

print()
print('-' * 40)
print()
