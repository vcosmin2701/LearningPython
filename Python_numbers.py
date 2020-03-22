# Python Numbers
"""
Main types of numbers in Python:
- Integers , Floating-point number, Complex Numbers

Integers :
- The integer data type is comprised of all the positive and negative whole numbers.
- The amount of memory an integer occupies depends on  its value.
  0 ---- 24 bytes
  1 ---- 28 bytes

Floating Point Numbers
- Floating Point Numbers or flaots, refers o positive and negative decimal numbers.
- Python allows us to create decimals up to a very high decimals place .
- This ensures accurate computation for precise values.
- A float occupies 24 bytes of memeory.

Complex numbers
- numbers made up of a real and an imaginary part.
- complex() statement is used to create complex numbers
- syntax: complex(real, imaginary)
- a complex number usually takes up 32 bytes of memory
"""

# Create a variable to store a int
number1 = int(27)
print("The integer is",number1)
# Create a variable to store a floating point number
number2 = 45.100
print("The floating point number is",number2)
# Create a variable to store a complex number
number3 = complex(4, 13)
print("The complex number is",number3)

# Python Booleans
"""
- The Boolean(bool) data types allows us to choose between two values :
  true / false
- A Boolean is used to determine whether the logic of an expression
  or a comparison is correct 
- True / False
"""
# Example 
condition = True
print("The condition is", condition)
