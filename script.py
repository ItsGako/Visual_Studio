def recherche_occ(t,x):
    for el in t:
        if el == x:
            return True
    return False

# print(recherche_occ([1,2,3,4],3))

def recherche_occ_indice(t,x):
    for i in range(len(t)):
        if t[i] == x:
            return i
    return -1

# print(recherche_occ_indice([1,2,3,4],1))

def moyenne(t):
    s=0
    for el in t:
        s=s+el
    return s/len(t)

# print(moyenne([1,2,3,4,5]))

def minimum(t):
    mini=t[0]
    for el in t:
        if el<mini:
            mini=el
    return mini

# print(minimum([1,2,3]))

def maximum(t):
    maxi=t[0]
    for el in t:
        if el>maxi:
            maxi=el
    return maxi

# print(maximum([1,2,3]))

def binaire(n):
    q=n//2
    r=n%2
    n_bin=str(r)
    while q!=0:
        n=q
        q=n//2
        r=n%2
        n_bin=str(r)+n_bin
    return n_bin

# print(binaire(122))

def dichotomie(t,valeur):
    debut=0
    fin=len(t)-1
    while debut!=fin:
        milieu=(debut+fin)//2
        if t[milieu]==valeur:
            return True
        elif t[milieu]>valeur:
            fin=milieu-1
        else:
            debut=milieu+1
    if t[debut]==valeur:
        return True
    return False

# print(dichotomie([1,2,3,4,5,6,7],3))

def tri_insertion(t):
    n=len(t)
    for i in range(1,n):
        j=i
        while j>0 and t[j]<t[j-1]:
            t[j],t[j-1]=t[j-1],t[j]
            j=j-1
    return t

# print(tri_insertion([4,2,3,1]))

def tri_selection(t):
    n=len(t)
    for j in range(n-1):
        indice=minimum(t,j)
        if indice!=j:
            t[indice],t[j]=t[j],t[indice]
    return t

def minimum(t,j):
    indice,mini=j,t[j]
    n=len(t)
    for i in range(j+1,n):
        if t[i]<mini:
            indice,mini=i,t[i]
    return indice

# print(tri_selection([1,2,-1,3,-9]))