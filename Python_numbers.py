# Python Data Types and Variables

"""
- The data types of an item defines the type and range
  of values that item can have.
- Python provides three main data type : nunbers , strings, booleans.

Variables :
- A variable is simply a name to which a value can be assigned (like a box)
- Variables are mutable . Hence, the value of a variable can always be updated
  and replaced 

Naming convention:
- the name can start with an upper or lower case alphabet.
- a number can appear in the name , but not at the beginning.
- underscore (_) can appear anywhere in the name.
- spaces are not allowed.
- the variable name should be something meaningful that describes
  the value it holds

"""

"""
Grouping values
- In Python, we can store multiple values together in a single variable.
- While there are many ways of doing , so the most popular is the list.
"""

# Crate a list with some motorcycle brands
motorcycle_brands = ["Kawasaki", "Honda", "BMW"]
print("The brands are",motorcycle_brands)
# Use len() statement to count how many items are in  the list.
num_items = len(motorcycle_brands)
print("Items in the list:",num_items)

# Quiz 
# The output of mystring[-2:-6:-2]
mystring = "0123456789"
print(mystring[-2:-6:-2])
