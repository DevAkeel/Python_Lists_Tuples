# Lists
a = [10,20,60,52,80] # Integer List Type
b = [10,"Akeel",60,"Reshi",80] # Mixed List 
c = ["Hello","World","Universe"] # String List
d = [] #Empty List
print(a[-1]) # accessing an Element in a List
print(b[1]) # accessing element at position 2 and index 1
print(c[1])
#print(a[7]) #IndexError: list index out of range
# Slicing of Lists
print(a[1:4]) # Slicing of list a (The last index i.e; index 4 will not be printed)
print(b[0:5])
print(a[::-1]) # Reverse printing a List
print(c[::2]) # Prints List by skipping one element
print(a[:3]) # Prints elements before index 3
print(b[3:]) # Prints the element at index 3 and after index 3
a[0] = 100 # Changes the element at index 0 in the list a to 100
print(a) # Prints the new list
c [0:2] = ["Hey", "Akeel"] # Changes list elements from index 0 to index 1 -> (2-1)
print(c) # Prints the New List
# Lists Operations
a.append(4) # Add one element
print(a) # Prints new List a with appended element
b.extend([10,"Vatira.app", "Toflio.com"]) # Extend adds up multiple items 
print(b) # Prints the extended list
c.insert(1,99) # Inserts 99 at index 1
print(c) # Prints the new list c
a.remove(4) # Removes the element 4 from list a
print(a)
a.pop() # removes the last element
a.pop(1) # removes the element at index 1
del a [0] # removes element at index 0
print(a) # new list a will be printed
a.clear() # clears the whole list
print(a) # prints the empty list

# Searching
new_list = [100,"Apple", 50, "Banana","Cherry", 50]
print("Apple" in new_list) # returns the boolean value. True if found else False
print(1000 in new_list)

print(new_list.index("Apple")) # returns the index number of a element
print(new_list.count(50)) # Returns the number of times element repeats

# Iterating a list
for element in new_list: # This loop helps printing the elemnets in the list individually
    print(element)

for i, mixed in enumerate(new_list): #This loop helps printing the elemnets in the list individually with indexes
    print(i, mixed)

# Nested Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
] # Matrix list
print(matrix[2][1]) # Accessing element

#Tuples
t = (1,3,4) # Tuples are immutable 
# just like list have some index features tuples also do but since tuples are immutable we can't perform much operations on tuples
point = (10, 20)

print(point)
print(type(point))


# ------------------------------------------------------------
# Tuple indexing
# ------------------------------------------------------------

print(point[0])
print(point[1])


# ------------------------------------------------------------
# Tuple slicing
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[::-1])