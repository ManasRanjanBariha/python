Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=['physics','chemistry',1997]
>>> list1[2]
1997
>>> list[1:2]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list[1:2]
TypeError: 'type' object is not subscriptable
>>> list1[1:2}
SyntaxError: invalid syntax
>>> list1[1:2]
['chemistry']
>>> list1[0:2]
['physics', 'chemistry']
>>> list1[2]='Bio'
>>> list1
['physics', 'chemistry', 'Bio']
>>> list1[-1]
'Bio'
>>> 
>>> #traversing a list
>>> list1=['apple','banana','chery']
>>> 
====================== RESTART: D:/22mmcb09/list/tut.py ======================
apple
banana
chery
>>> list1=[1,2,3]
>>> for x in range(len(list1)):
	list1[x]*=2

>>> for x in range(len(list1)):
	list1[x]*=2
	print(list1[x])

4
8
12
>>> #list operators
>>> #+ is used to concatinate two list
>>> list2=[4,5,6]
>>> list3=list1+list2
>>> print(list3)
[4, 8, 12, 4, 5, 6]
>>> #* used for repeation
>>> print(list3*2)
[4, 8, 12, 4, 5, 6, 4, 8, 12, 4, 5, 6]
>>> # check membership in a list
>>> list1=[1,2,3]
>>> 1 in list1
True
>>> # list slicing
>>> t=['a','b','c','d','e','f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[1:]
['b', 'c', 'd', 'e', 'f']
>>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']
>>> # list methods
>>> # 1.append()
>>> # append element at the end of the existing list
>>> t=['a','b','c']
>>> t.append('d')
>>> t
['a', 'b', 'c', 'd']
>>> # 2 clear
>>> t.clear()
>>> t
[]
>>> # clear all element of the list
>>> # 3 copy()
>>> l1=[1,2,3,4]
>>> l2=l1.copy()
>>> l2
[1, 2, 3, 4]
>>> l1[2]=5
>>> l2
[1, 2, 3, 4]
>>> l3=l1
>>> l3
[1, 2, 5, 4]
>>> l1[2]=2
>>> l3
[1, 2, 2, 4]
>>> t=[1,2,4,6,1,2,5,6]
>>> t.count(2)
2
>>> # 5 extend()
>>> t=['a','b','c']
>>> t2=['d','e']
>>> t.extend(t2)
>>> t1
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t1
NameError: name 't1' is not defined
>>> t
['a', 'b', 'c', 'd', 'e']
>>> t2
['d', 'e']
>>> t2.extend(t)
>>> t2
['d', 'e', 'a', 'b', 'c', 'd', 'e']
>>> # 6 index()
>>> t.index(2)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    t.index(2)
ValueError: 2 is not in list
>>> t.index('e')
4
>>> t2.index('e')
1
>>> # 7 insert()
>>> l1=[1,2,3,4]
>>> l1.insert(3,'a')
>>> l1
[1, 2, 3, 'a', 4]
>>> l1.insert(6,7)
>>> l1
[1, 2, 3, 'a', 4, 7]
>>> l1.insert(10,5)
>>> l1
[1, 2, 3, 'a', 4, 7, 5]
>>> l1.insert(-1,80)
>>> l1
[1, 2, 3, 'a', 4, 7, 80, 5]
>>> # 8  pop()
>>> l1.pop(2)
3
>>> l1
[1, 2, 'a', 4, 7, 80, 5]
>>> #9 remove()
>>> l1.remove()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l1.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> l1.remove(1)
>>> l1
[2, 'a', 4, 7, 80, 5]
>>> print(l1.remove(80))
None
>>> # 10 reverse()
>>> l1.reverse()
>>> l1
[5, 7, 4, 'a', 2]
>>> # reverse the order of element of the lsit
>>> l1.sort()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    l1.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> l1=[1,2,3]
>>> l1.sort()
>>> l1
[1, 2, 3]
>>> l1.reverse()
>>> l1
[3, 2, 1]
>>> l1.sort()
>>> l1
[1, 2, 3]
>>> max(l1)
3
>>> min(l1)
1
>>> t=['a','b','c','d','e','f']
>>> del t[1:5]
>>> t
['a', 'f']
>>> item=[1,2,3,4,5]
>>> square=[]
>>> for i in items:
	square.append(i**2)

Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    for i in items:
NameError: name 'items' is not defined
>>> for i in item:
	square.append(i**2)

	
>>> square
[1, 4, 9, 16, 25]
>>> sum(t)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    sum(t)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum(item)
15
>>> sum(square)
55
>>> b1=[]
>>> for i in "banana":
	b1.append(i)

>>> print(b1)
['b', 'a', 'n', 'a', 'n', 'a']
>>> l1=[i for i in 'banana']
>>> l1
['b', 'a', 'n', 'a', 'n', 'a']
>>> 
