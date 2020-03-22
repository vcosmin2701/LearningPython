# Python operator
"""
- Operators are used to perform aithmetic and logical operation on data.
- They enable us to manipulate and interpret data to produce useful outputs.
- In general , Python's operators follow the in-fix or prefix notation.

In-fix operator appear between two operands and hence , are usually known as binary operators.
A prefix operator usually works on one operand and appears before it.

"""

"""
Arithmetic operators
- order of operation : 
1) parentheses ()
2) ** exponent
3) %,*,/,// - modulo, multiplication, division, floor division
4) +,- addition,substraction

- floor divison: the result of opeation is floored to the nearest smaller integer.(integer division)
  unlike normal division,floor division between two int result in an int
"""
# Create two variables and store two different number
number1 = 45
number2 = 76
# Use all the operation from the course.
statement1 = (number1 + number2)
print("Operation 1 =", statement1)
statement2 = (number2 - number1)
print("Operation 2=",statement2)
statement3 = (number2 * number1)
print("Operation 3=",statement3)
statement4 = (number1 ** number2)
print("Operation4=",statement4)

# Comparasion opertors
"""
- > : greater than
- < : less than
- >= : greater than or equal to
- <= : less than or equal to
- == equal to 
- is : equal to
- is not : not equal to

- The result of a comparasion is always a bool.
"""

# Assignment operators
# This is a category of operators which is used to assign values to a variable.
"""
- = : assign
- += : add and assign
- -= : substract and assign
- *= : multiply and assign
- /= : divide and assign
- //= : divide, floor and assing
- **= : raise power and assign
- %= : take modulo and assign
- |= , &=, ^= : OR, AND, XOR and assign
- >>= : right-shift and assign
- <<= : left-shift and assign

note : Variables are mutable.
"""

# Logical operators
"""
Logical operators are used to manipulate the logic of Boolean expressions.

and ------ AND
or  ------ OR
not ------ NOT

Bit Value

True is equal to 1
False is  equal to 0

note: In Python compiler can automatically convert the bool to its numerical form when needed.
"""

# Bitwise operator
"""
Bitwise operators allow us to perform bit-related operations on values.

- & : bitwise AND
- | : bitwise OR
- ^ : bitwise XOR
- ~ : bitwise NOT
- << : shift bits left 
- >> : shift bits right
"""
number1 = 10 # Binary value = 01010
number2 = 20 # Binary value = 10100

print("Operation 5",number1 & number2)