l=[ (2, 7), (3, 7), (2, 5), (8, 7), (6, 5), (9, 8) ]
l1=sorted(l,key=lambda a: l.count(a),reverse=True)
print(l1)
