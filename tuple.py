Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Tuples
>>> t=(1,2,3)
>>> t=(1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> t=(1,2,3,[5,6,7,8,9])
>>> t[0]
1
>>> t[0]=3
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t[0]=3
TypeError: 'tuple' object does not support item assignment
>>> t[3][0]=4
>>> t[3]
[4, 6, 7, 8, 9]
>>> # + is used for concatination * is used repetation
>>> #build in methods
>>> # count()
>>> t=[1,2,3,4,1]
>>> t.count(1)
2
>>> # index()
>>> t.index(4)
3
>>> # max() min() and sum()
>>> max(t)
4
>>> min(t)
1
>>> sum(t)\
KeyboardInterrupt
>>> sum(t)
11
>>> t(3,2,1,4,5)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t(3,2,1,4,5)
TypeError: 'list' object is not callable
>>> t=(3,2,1,4,5)
>>> sorted(t)
[1, 2, 3, 4, 5]
>>> t
(3, 2, 1, 4, 5)
>>> #enumurate
>>> q=('a','b','c','d')
>>> for i,val in enumerate(q):
	print(i,val)

	
0 a
1 b
2 c
3 d
>>> 3 d
SyntaxError: invalid syntax
>>> L=[('mati',20),("karan",30)('shubha',60)]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    L=[('mati',20),("karan",30)('shubha',60)]
TypeError: 'tuple' object is not callable
>>> L=[('mati',20),("karan",30),('shubha',60)]
>>> for i,val in enumerate(L):
	name=val[0]
	age=val[1]
	print("index is ",i)
	print("name is ",name)
	print("age is",age)

index is  0
name is  mati
age is 20
index is  1
name is  karan
age is 30
index is  2
name is  shubha
age is 60
>>> #any() it will return true and false
>>> x=()
>>> any(x)
False
>>> x=(1,2,3)
>>> any(x)
True
>>> x=(1)
>>> any(x)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    any(x)
TypeError: 'int' object is not iterable
>>> x=(1,)
>>> any(x)
True
>>> # call()
>>> # all()
>>> x=(1,2,3)
>>> all(x)
True
>>> x=(0,1,2,3)
>>> all(x)
False
>>> # Connect a list into a tuple
>>> # convert a lsit into a tuple
>>> x=[1,2,3,4,5]
>>> z=tuple(x)
>>> z
(1, 2, 3, 4, 5)
>>> # convert a tuple into a list
>>> y=list(x)
>>> y
[1, 2, 3, 4, 5]
>>> y=list(z)
>>> y
[1, 2, 3, 4, 5]
>>> t=(1,2,3,[5,6,7,8,9])
>>> t[3][0:2]=1,2,3
>>> t[3]
[1, 2, 3, 7, 8, 9]
>>> t[3][0]=9
>>> t[3]
[9, 2, 3, 7, 8, 9]
>>> 
============ RESTART: D:/22mmcb09/list-comprehensioon/q1_even.py ============
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> 
============ RESTART: D:/22mmcb09/list-comprehensioon/q1_even.py ============
[2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> 
============ RESTART: D:/22mmcb09/list-comprehensioon/q2_divby.py ============
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> 
============= RESTART: D:/22mmcb09/list-comprehensioon/q3_odd.py =============
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
>>> 
============ RESTART: D:/22mmcb09/list-comprehensioon/q5_cube.py ============
[125, 216, 343, 512, 729]
>>> 
============ RESTART: D:\22mmcb09\list-comprehensioon\q5_cube.py ============
[216, 512]
>>> 
=========== RESTART: D:/22mmcb09/list-comprehensioon/q4_concat.py ===========
['HiJohn', 'HiAllen']
>>> 
=========== RESTART: D:/22mmcb09/list-comprehensioon/q4_concat.py ===========
['HiJohn', 'HiAllen', 'Good MorningKelly']
>>> 
=========== RESTART: D:/22mmcb09/list-comprehensioon/q4_concat.py ===========
Traceback (most recent call last):
  File "D:/22mmcb09/list-comprehensioon/q4_concat.py", line 3, in <module>
    l1=[ List1[i]+List2[j]  for i in range(3) for j in range(2)]
  File "D:/22mmcb09/list-comprehensioon/q4_concat.py", line 3, in <listcomp>
    l1=[ List1[i]+List2[j]  for i in range(3) for j in range(2)]
IndexError: list index out of range
>>> 
=========== RESTART: D:/22mmcb09/list-comprehensioon/q4_concat.py ===========
['HiJohn', 'HiAllen', 'HiKelly', 'Good MorningJohn', 'Good MorningAllen', 'Good MorningKelly']
>>> 
============= RESTART: D:\22mmcb09\list-comprehensioon\q3_odd.py =============
['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
>>> 
============= RESTART: D:\22mmcb09\list-comprehensioon\q3_odd.py =============
[(0, 'even'), (1, 'odd'), (2, 'even'), (3, 'odd'), (4, 'even'), (5, 'odd'), (6, 'even'), (7, 'odd'), (8, 'even'), (9, 'odd'), (10, 'even'), (11, 'odd'), (12, 'even'), (13, 'odd'), (14, 'even'), (15, 'odd'), (16, 'even'), (17, 'odd'), (18, 'even'), (19, 'odd'), (20, 'even'), (21, 'odd'), (22, 'even'), (23, 'odd'), (24, 'even'), (25, 'odd'), (26, 'even'), (27, 'odd'), (28, 'even'), (29, 'odd')]
>>> 
=========== RESTART: D:\22mmcb09\list-comprehensioon\q4_concat.py ===========
['HiJohn', 'HiAllen', 'HiKelly', 'Good MorningJohn', 'Good MorningAllen', 'Good MorningKelly']
>>> 
