a=[x**2 for x in range(0,11)]
print(a)
b=[i**2 for i in range(11)]
print(b)
c=[x for x in a if x%2==0]
print(c)
words='the quick borwn fox jumps over the lazy dog'.split()
print('the words are',words)
stuff=[[w.upper(),w.lower(),len(w)] for w in words]
for data in stuff:
    print(data)
celsius=[12,456,132,547,23315648,6984]
print(celsius)
f=[((x*(9/5))+32)for x in celsius]
print('fuck this shit',f)
