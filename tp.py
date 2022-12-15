import math

def erathosthene(n):
    t=[] # liste booléenne de taille n
    r=[] # liste des entiers premiers dans l'intervalle [0,n[
    t+=[False] #0 n'est pas premier
    t+=[False] #1 n'est pas premier
    for i in range(2,n): #2 <= i < n
        t+=[True] #initialisation des n-2 autres entiers (2,3,4,...,n-1)
    
    for i in range(2,int(math.sqrt(n))): #2<= i < sqrt(n)
        j=2*i #j appartient à l'ensemble des multiples de i de 0 à n-1
        while j<len(t):
            t[j]=False # j n'est pas premier
            j=j+i # prochain multiple de i

    for i in range(2,n): #2 <= i < n
        if t[i]: #si i est premier
            r+=[i] #i appartient à r
    return r #renvoie r

def scan(n):
    tab=erathosthene(n) #import des nombres premiers compris entre 0 et n exclu
    s=len(tab)
    pyr=0
    for i in range(s): # 0 <= i < len(tab)
        for y in range(pyr,s): # pyr <= y < len(tab)
            if tab[i]*tab[y]==n: # si le produit des deux nombres entiers d'indices i et y est égal à n
                return [tab[i],tab[y]] # renvoie p et q
        pyr+=1
    return False

def euclideEtt(a,b):
    r1=b
    r2=a
    u1=0
    v1=1
    u2=1
    v2=0
    while r2!=0:
        q=r1//r2
        
        r3=r1
        u3=u1
        v3=v1

        r1=r2
        u1=u2
        v1=v2

        r2=r3-q*r2
        u2=u3-q*u2
        v2=v3-q*v2
    return [r1,u1,v1] # retourne l'identité de bézout


#exo1
"""e=151
d=7
n=391

print("e=",e,", d=",d,", n=",n,sep="")
print("====================")
t=scan(n)
print("p=",t[0]," et q=",t[1],sep="")
phi=(t[0]-1)*(t[1]-1)
print("phi(N) =",phi)
verif=euclideEtt(phi,e)
print(phi,"*",verif[1],"+",e,"*",verif[2],"=",verif[0],"(identité de bézout)")"""

#exo2

"""print((112**11)%221)
print((78**35)%221)

phi=3640
e=307
verif=euclideEtt(phi,e)
print(phi,"*",verif[1],"+",e,"*",verif[2],"=",verif[0],"(identité de bézout)")
print(3640*-7+307*83)"""

#exo3
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

e=257
n=1073
d=353


print("=========TABLE FONCTION==========")

for x in range(34):
    y=math.ceil(2*x/3)
    print("x=",x,"; y=",y,sep="")
print("=============================")

m1="AJOUTERA"
print("!le mot est:",m1)
print("!taille du mot:",len(m1))

c1=alphatonum(m1,alpha)
print("!c1:",c1)

rsa(c1,e,n)
print("!c1 crypté:",c1)

rsa(c1,d,n)
print("!c1 décrypté:",c1)

m1=numtoalpha(c1,alpha)
print("!le mot est:",m1)
