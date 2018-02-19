n=input("Parakalw Dwste to plithws twn psifiwn: ")
s=input("Parakalw dwste kai to athroisma twn psifiwn: ")
pin=[]
a=0
pint=[]
for i in range(n):
    pin.insert(i,9)
    a= a +(10**(i-9+pin[i]))
    pint.insert(i,1)
b=10**(len(pint)-1)
megar=a*9
t=0
for b in range(b,megar+1):
    alist=[int(i) for i in str(b)]
    p=0
    k=1
    for j in range(n-1):
        if alist[j]>alist[j+1]:
            k=k+1
        if k==n:
            for i in range(len(alist)):
                p=p+alist[i]
    if p==s:
        t=t+1
print  t

