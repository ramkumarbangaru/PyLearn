"""Lets take 2 lists


  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

1) create new list with elements which is available only in list "a" and not in "b" and print (difference)
2) create new list with elements which is common to both lists (intersection) and print
3) create new list with elements from both list (union) and print
4) create new list with elements which is available either in a or b but not on both."""

"""a = set("New Program")
print a
print type(a)

b = set (['list1','list2','list3','list3'])
print b

c = set (('tuple1','tuple2','tuple3','tuple3'))
print b"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = set (a)
print c

d = set(b)
print d


diff = list(c.difference(d))
#list(diff)
print "difference: "+str(diff)+""

intr = list(c.intersection(d))
print "intersection: "+str(intr)+""


uni = list(c.union(d))
print "union: "+str(uni)+""

diff1 = (c.difference(d))
diff2 = (d.difference(c))
anyof = list(diff1.union(diff2))
print "any of the list: "+str(anyof)+""

