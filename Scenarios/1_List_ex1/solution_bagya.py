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