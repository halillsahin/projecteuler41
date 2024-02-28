import sympy
a=set()
c=0
for i in range(2,10000000):
    if sympy.isprime(i):
        for b in range(1,len(str(i))+1):
            a.add(str(b))
            if a==set(str(i)):
                c=i
        a=set()
print(c)

        

        