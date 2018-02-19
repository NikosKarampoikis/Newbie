import random

lista=[]
for i in range(30):
    lista.insert(i,random.randint(-30, 30))
p=0
for i in range(30):
    for j in range(30):
        for k in range(30):
            t = lista[i] + lista[j] + lista[k]
            if t==0:
                p+=1
                print lista[i], lista[j], lista[k]
if p==0:
    print "Den iparxei tetoios sindiasmos!"
