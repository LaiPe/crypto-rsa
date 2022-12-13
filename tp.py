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

def alphatonum(mot,alpha):
    li=[] #liste de chiffres par bloc de 3
    temp="" #mémoire temporaire
    c=0 #état
    for i in range(len(mot)): #0 <= i < len(mot)
        y=0 #position de la i-ème lettre du mot dans alpha (alphabet)
        while mot[i]!=alpha[y]: #tant que la i-ème lettre ne correspond pas à une lettre de l'alphabet
            y+=1 #y est incrémenté

        y=str(y)
        if len(y)==1: # si y est un chiffre (0,1,2,...,9)
            y="0"+y
        print(y)
   
        if c==0: #état 0 (mémoire temp vide)
            print("c0:",temp)
            temp=y
            c+=1 #passage à l'état 1
            print("c0:",temp)
        elif c==1: #état 1 (mémoire temp: 2 chiffres)
            print("c1:",temp)
            li+=[temp+y[0]]
            temp=y[1]
            c+=1 #passage à l'état 2
            print("c1:",temp)
        elif c==2: #état 2 (mémoire temp: 1 chiffre)
            print("c2:",temp)
            li+=[temp+y]
            temp=""
            c=0 #retour à l'état 0
            print("c2:",temp)
    if temp!="": #si la mémoire temp n'est pas vide
        li+=[temp] #flush
    return li #renvoie li

def numtoalpha(li,alpha):
    mot="" #mot à renvoyer
    temp="" #mémoire temporaire
    c=True #état
    for e in li: #e corrspond à une chaine de car d'au plus 3 chiffres. e prends à chaque passage de boucle la valeur suivante dans li. 
        print(e)
        if len(e)==3: #si e est composé d'exactement 3 chiffres    
            if c: #état 0 (mémoire temp vide)
                print("a1:",temp)
                mot+=alpha[int(e[0]+e[1])]
                temp+=e[2]
                c=False #passage à l'état 1
                print("a1:",temp)
            else: #état 1 (mémoire temp: 1 chiffre)
                print("a2:",temp)
                mot+=alpha[int(temp+e[0])]
                temp=""
                mot+=alpha[int((e[1]+e[2]))]
                c=True #retour à l'état 0
                print("a2:",temp)
        else: #si e est composé de 2 ou 1 chiffres (fin de liste)
            print("b:",temp)
            mot+=alpha[int(temp+e)] #flush
    return mot #renvoie mot

        




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

m1="ALPHA"
c1=alphatonum(m1,alpha)
print(c1)
print(numtoalpha(c1,alpha))
