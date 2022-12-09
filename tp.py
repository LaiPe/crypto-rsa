import math

def erathosthene(n):
    t=[]
    r=[]
    t+=[False]
    t+=[False]
    for i in range(2,n):
        t+=[True]
    for i in range(2,int(math.sqrt(n))):
        j=2*i
        while j<len(t):
            t[j]=False
            j=j+i
    for i in range(2,n):
        if t[i]:
            r+=[i]
    return r
def scan(tab,n):
    for i in range(len(t)):
        for y in range(len(t)):
            if tab[i]*tab[y]==n:
                return [tab[i],tab[y]]
    return False

#exo1
"""e=151
d=7
n=391

print("e=",e,", d=",d,", n=",n,sep="")
print("====================")
t=erathosthene(300)
t=scan(t,n)
print("p=",t[0]," et q=",t[1],sep="")
phi=(t[0]-1)*(t[1]-1)
print("phi(N) =",phi)
print("E*D%phi =",e*d%phi)"""

#exo2
print((112**11)%221)
print((78**35)%221)