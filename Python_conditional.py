# Python Conditional Statement

"""
A conditional statement is a Boolean expression that, if True, executes a piece of code.
Conditional statements control the flow of the code and allow the computer to think.
syntax :
	if conditional stataement is True:
		# execute expression1
		pass
	else:
		# execute expression2
		pass
"""

"""
The if statement
- An if statement runs like this:
	if the condition holds True, execute the code to be executed. Otherwise, skip it and move on.
"""
"""
 Create two variables with two different numbers
 	If the first number is grater than the second , will display the message :
 		The first number is greater than the second .
 	If is not will display:
 		The first number is lower than first
 """

first_number = 25
second_number = 46
if (first_number > second_number):
	print("The first number is greater than the second number")
else:
	print("The first number is lower than the second number")

"""
Conditions with logical operators
"""

difference = (second_number - first_number)
if (first_number > second_number) and (difference == 10):
	print("The first number is greater than second number,\n and their difference is equal to 10")
else:
	print("The first number is lower than the second one,\n and the difference of both numbers is not equal to 10")

"""
Nested if statements
"""

# Example of nested if statements
num = 63
if (num >= 0) and (num <= 100):
	if (num >= 50) and (num <= 75):
		if (num >= 60) and (num <= 70):
			print("The number is in the 60-70 range")

"""
Creating and Editing Values
"""

number3 = 27
if (number3 > 5):
	number3 = 20
	new_number3 = (number3 * 5)
print(number3)
print(new_number3)

"""
The if-elif-else statement
"""
# Example if-elif-else

engine = "stopped"
if engine == "started":
	print("Your engine will start")
elif engine == "stopped":
	print("Your engine is stopped")
else:
	print("There must be a problem with the engine")
