t=[ ('Ram', '89.20'), ('Siva', '76.45'), ('Pooja', '84.40'), ('Tara', '68.43'), ('Jeeva', '91.40') ]
t.sort(key = lambda x: float(x[1]), reverse = True) 
print(t)
