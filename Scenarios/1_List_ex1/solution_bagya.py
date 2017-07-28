"""
Lets say,  we have a list

a = [2,4,5,3,7,5,6,8,0,4,5,7,3,5,8,9,0,6,3,5]

1) Remove all duplicates and print
2) Count how many times each character appeared in the list
3) Create a new list from this list  which contains numbers less than 7
"""
a = [2,4,5,3,7,5,6,8,0,4,5,7,3,5,8,9,0,6,3,5]
print a

b = []

c = []

for i in a:
  if i not in b:
    b.append(i)
    print "occurrence of "+str(i)+" is : "+str(a.count(i))+""
    if i < 7:
      c.append(i)
    #print a.count(i)
  #b.append(i)
print "The final list is "+str(b)+""
print "The final list is "+str(c)+""