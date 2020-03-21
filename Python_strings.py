# Python Strings

"""
A string is a collection of characters closed  within single or double quotes

The lenght of a  string
- the lenght of a string can be found using the len() statement

Indexing 
- In a string, every character is given a numerical index based on its position.
- Index start from 0

Accessing characters
- Each character in a string can be accessed using its index.
- The index must to be closed within square brackets, [], and
  appended to the string.

Reverse indexing
- Negative indices start from the opposite end of the string.
  Hence, the -1 index corresponds to the last  character.
"""

# Create a variable and assign a string to work it

string1 = "m8Competition"
# Grab the number 8 from the string
grab_item1 = string1[1]
print("The item is",grab_item1)
# Grab the last letter from the string
grab_item2 = string1[-1]
print("The item is",grab_item2)
# Check the lenght of the string
check_lenght = len(string1)
print("The lenght of the string is",check_lenght)

"""
String slicing
- Slicing is the process of obtaining a portion (substring) of a string
  by using indices
- syntax : string[start:end]
- the  character at the end index in the string , will not be included
  in the substring obtained through this method.

Slicing with a step
- syntax : string[start:end:step]

Reverse slicing 
- Strings can also be sliced to return a reverse substring.
- In this case,we would neet to switch the order of the start and end indices
- Also , a negative step must to  be provided.

Partial slicing
- One thing to note is stat specifying the start and end indicies is optional.
- If start is not provided , the substring will have all the characters until
  the end index
- If end is not provided , the substring will begin from the start index and
  go all the way to the end.
"""

# Grab all characters from the string
grab_item3 = string1[:]
print("The item is",grab_item3)
# Grab all the letter up to the last t but not included
grab_item4 = string1[:9]
print("The item is",grab_item4)
# Grab everything but in step size of two
grab_item5 = string1[::2]
print("The item is",grab_item5)
# Reverse the string using slicing
reverse_string = string1[::-1]
print("The string is now",reverse_string)