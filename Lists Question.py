# ------------------------------------------------------------
# Lists Question
'''
Q1:

Create a Python list containing the numbers:

[10, 20, 30, 40, 50]

Write a program to:

Add 60 to the end of the list.
Remove 30 from the list.
Print the largest number in the list.
Print the final list.

''' 
# ------------------------------------------------------------

List = [10, 20, 30, 40, 50]
List.append(60)
List.remove(30)
print(max(List))
print(List)

'''
Q2:

Given this list:

numbers = [12, 5, 8, 20, 3, 15]

Write a program to:

Add 10 to the list.
Remove 8 from the list.
Sort the list in ascending order.
Print the smallest number.
Print the largest number.
Print the final list.

'''
numbers = [12, 5, 8, 20, 3, 15]

numbers.append(10)
numbers.remove(8)
numbers.sort()
print(min(numbers))
print(max(numbers))
print(numbers)

'''
Q3:

numbers = [4, 7, 2, 9, 7, 3, 7, 1]

Write a program to:

Remove all occurrences of 7.
Add 10 to the list.
Sort the list in descending order.
Print the second-largest number.
Print the final list.

'''
numbers = [4, 7, 2, 9, 7, 3, 7, 1]

target = 7

while target in numbers:
    numbers.remove(target)

numbers.append(10)

numbers.sort(reverse = True)

second_largest = numbers[1] # If accending order then we should use [-2]

print(second_largest)



print(numbers)

'''
Q4:

Given:

numbers = [5, 12, 5, 8, 12, 3, 5, 10]

Write a program to:

Remove duplicate values, keeping only one of each.
Sort the list in ascending order.
Find the second-smallest number.
Find the second-largest number.
Print the final list.

'''
numbers = [5, 12, 5, 8, 12, 3, 5, 10]

unique = list(set(numbers))

unique.sort() 



second_smallest = unique[1]

second_largest = unique[-2]

print(second_smallest)
print(second_largest)

print(unique)
