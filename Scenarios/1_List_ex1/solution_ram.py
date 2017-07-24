"""
Lets say,  we have a list

a = [2,4,5,3,7,5,6,8,0,4,5,7,3,5,8,9,0,6,3,5]

1) Remove all duplicates and print
2) Count how many times each character appeared in the list
3) Create a new list from this list  which contains numbers less than 7
"""
from collections import Counter

a = [2,4,5,3,7,5,6,8,0,4,5,7,3,5,8,9,0,6,3,5]

print "Unique List :"
print list(set(a))
print "Counter for each unique element : "
print Counter(a)
print "List with numbers which is less than 7 : "
print [i for i in a if i < 7]