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

        if c==0: #état 0 (mémoire temp vide)
            temp=y
            c+=1 #passage à l'état 1
        elif c==1: #état 1 (mémoire temp: 2 chiffres)
            li+=[temp+y[0]]
            temp=y[1]
            c+=1 #passage à l'état 2
        elif c==2: #état 2 (mémoire temp: 1 chiffre)
            li+=[temp+y]
            temp=""
            c=0 #retour à l'état 0
    if temp!="": #si la mémoire temp n'est pas vide
        li+=[temp] #flush
    return li #renvoie li

def numtoalpha(li,alpha):
    mot="" #mot à renvoyer
    temp="" #mémoire temporaire
    c=True #état
    i=0

    while i<len(li):
        if isinstance(li[i],int): #ajout de "0" pour remplir les blocs (sauf le dernier -> cas de fin de mot)
            li[i]=str(li[i])
            if i!=len(li)-1:
                while len(li[i])<3:
                    li[i]="0"+li[i]

        if len(li[i])==3: #bloc de 3 chiffres
            if c: #état 0 (mémoire temp vide)
                t=0
                while t<2 and int(li[i][t]+li[i][t+1])>=len(alpha): #l'indice calculé est incohérent (trop grand) 
                    mot+=alpha[int(li[i][t])]
                    t+=1
                if t==0: 
                    mot+=alpha[int(li[i][t]+li[i][t+1])]
                    temp+=li[i][t+2]
                    c=False #passage à l'état 1
                elif t==1:
                    mot+=alpha[int(li[i][t]+li[i][t+1])]
                elif t==2:
                    temp+=li[i][t]
                    c=False #passage à l'état 1
                i+=1
            else: #état 1 (mémoire temp: 1 chiffre)
                if int(temp+li[i][0])>=len(alpha): #l'indice calculé est incohérent (trop grand)
                    mot+=alpha[int(temp)]
                    temp="" #vide la mémoire
                    c=True #passage à l'état 0
                    #i n'est pas incrémenté;reste sur le même bloc de 3 chiffres
                else:
                    mot+=alpha[int(temp+li[i][0])]
                    temp="" #vide la mémoire
                    if int(li[i][1]+li[i][2])>=len(alpha):
                        mot+=alpha[int(li[i][1])]
                        temp+=li[i][2]
                        #reste à l'état 1
                    else:
                        mot+=alpha[int(li[i][1]+li[i][2])]
                        c=True #passage à l'état 0
                    i+=1
        elif len(li[i])==2: #bloc de 2 chiffres (cas de fin de mot)
            if c: #état 0 (mémoire temp vide)
                if int(li[i][0]+li[i][1])>=len(alpha): #l'indice calculé est incohérent (trop grand)
                    mot+=alpha[int(li[i][0])]
                    temp+=li[i][1]
                    c=False #passage à l'état 1
                else:
                    mot+=alpha[int(li[i][0]+li[i][1])]
                    #reste à l'état 0
                i+=1
            else: #état 1 (mémoire temp: 1 chiffre)
                if int(temp+li[i][0])>=len(alpha): #l'indice calculé est incohérent (trop grand)
                    mot+=alpha[int(temp)]
                    temp="" #vide la mémoire
                    c=True #passage à l'état 0
                    #i n'est pas incrémenté;reste sur le même bloc de 2 chiffres
                else:
                    mot+=alpha[int(temp+li[i][0])]
                    temp=li[i][1] #vide puis nouvelle valeur
                    #reste à l'état 1
                    i+=1
        elif len(li[i])==1: #bloc d'un seul chiffre (cas de fin de mot)
            if c: #état 0 (mémoire temp vide)
                #l'indice est forcément cohérent 
                mot+=alpha[int(li[i][0])]
            else: #état 1 (mémoire temp: 1 chiffre)
                if int(temp+li[i][0])>=len(alpha): #l'indice calculé est incohérent (trop grand)
                    mot+=alpha[int(temp+"0")] 
                    temp=li[i][0] #vide puis nouvelle valeur
                    #reste à l'état 1
                else:
                    mot+=alpha[int(temp+li[i][0])]
                    temp="" #vide la mémoire
                    c=True #passage à l'état 0
            i+=1
    
    if temp!="": #si la mémoire temp n'est pas vide
        mot+=alpha[int(temp)] #flush
        temp="" #vide la mémoire
    return mot 

def rsa(message,cle,n):
    for i in range(len(message)):
        message[i]=int(message[i])**cle%n

#exo3
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

e=257
n=1073
d=353

conti=True

while conti:
    print("===========MENU============")
    print("1.mot->codeRSA")
    print("2.codeRSA->mot")
    print("q.quitter")
    choix=input("choix?:")

    if choix=="1":
        mot=input("mot à chiffrer:").upper()
        det=input("voir details? (o pour oui):")
        li=alphatonum(mot,alpha)
        if det=="o":
            print(li)
        rsa(li,e,n)
        print("mot crypté:",li)

    
    elif choix=="2":
        li=[]
        nb=int(input("nombre de paquets?:"))
        for i in range(nb):
            print("paquet n°",i+1,sep="",end="")
            li+=[input("?:")]
        print(li)

        det=input("voir details? (o pour oui):")
        rsa(li,d,n)
        if det=="o":
            print("codeRSA décrypté:",li)
        mot=numtoalpha(li,alpha)
        print("mot décrypté:",mot)
    elif choix=="q":
        conti=False
    else:
        print("veuillez rentrer un caractère valide")

"""m1="RSA"
print("!le mot est:",m1)

c1=alphatonum(m1,alpha)
print("!c1:",c1)

rsa(c1,e,n)
print("!c1 crypté:",c1)

rsa(c1,d,n)
print("!c1 décrypté:",c1)

m1=numtoalpha(c1,alpha)
print("!le mot est:",m1)

print(numtoalpha(["553", "813"],alpha))"""