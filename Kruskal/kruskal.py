#doar pe neorientate

def citire(fisier): 
    f=open(fisier) #open(numefisier)
    n,m=[int(x) for x in f.readline().split()]
    lm = []  #lista de muchii

    #doua noduri au aceeasi culoare daca au acelas reprezentant => nu ne pasa muchia cum este scrisa
    #pentru noi [n1,n2,c] == [n2,n1,c]

    for i in range(m):
        m1,m2,c= [int(x) for x in f.readline().split()]
        lm.append([m1,m2,c])
    f.close()
    return n,m,lm

def comp(x):    #pt sortare
    return x[2]

def intializare(i): #varful i formeaza un arbore (o componenta/o multime)
    tata[i] = 0
    h[i] = 0

def reprez(u):    #determin reprezentantul nodului u    
    if tata[u] == 0:
        return u

    # compresie de cale
    tata[u] = reprez(tata[u])   #fac mai usoara determinarea tatalui (ca sa fac arborele mai mic in h => mai usor de parcurs)
    return tata[u]     

# reuniune ponderata
def reuneste(u,v):
    ru=reprez(u)
    rv=reprez(v)
    if h[ru]>h[rv]:
        tata[rv]=ru
    else:
        tata[ru]=rv
        if h[ru] == h[rv]:   #inaltimea se modifica doar daca cei 2 arbori au aceeasi inaltime. de ce? pt ca altfel arborele mai mic devine subarbore arborelui mai mare => nu se modifica h
            h[rv] += 1

#muchii.sort(key=comp)    def comp(x) return x[2]
def kruskal():
    
    lm.sort(key=comp)  
    print (lm)
    
    for i in range(1,n+1): #initializaz tata si h pentru fiecare componenta
        intializare(i)

    cost_minim=0
    nr_muchii = 0 #tin evindenta numarului de muchii selectate pentru ca sa opresc algoritmul cand ajung la (n-1)
    
    for u, v, c in lm: 
        if reprez(u) != reprez(v):  #reprezentantul nu va fi niciodata 0, ci daca este vorba doar de un nod, el va fi reprezentantul sau
            reuneste(u, v)
            print(u, v)
            cost_minim += c
            nr_muchii += 1
            if nr_muchii == n-1:
                #print("Vector de tati: ", tata)
                print("Costul minim este de: ", cost_minim)
                return
        
        
n,m,lm = citire("cost.in")
tata=[0 for i in range(n+1)]
h=[0 for i in range(n+1)]
kruskal()


     












# #doar pe neorientate

# def citire(fisier): #am pus tipul grafului ca parametru, nu ca data in fisier
#     # ar merge trimis ca parametru si numele fisierului, sa nu il fixam ca fiind graf.in:
#     # citire(numefisier,tip)
#     f=open(fisier) #open(numefisier)
#     n,m=[int(x) for x in f.readline().split()]
#     lm = []  #lista de muchii

#     #doua noduri au aceeasi culoare daca au acelas reprezentant => nu ne pasa muchia cum este scrisa
#     #pentru nou, [n1,n2,c] == [n2,n1,c]

#     for i in range(m):
#         m1,m2,c= [int(x) for x in f.readline().split()]
#         lm.append([m1,m2,c])
#     f.close()
#     return n,m,lm


# # def reprez(u):    #determin reprezentantul nodului u
# #     x=u
# #     while tata[x]!=0:
# #         x=tata[x]
# #     return x

# def reprez(u):    #determin reprezentantul nodului u    
#     if tata[u] == 0:
#         return u

#     tata[u] = reprez(tata[u])   #fac mai usoara determinarea tatalui
#     return tata[u]


# def reuneste(u,v):
#     r1=reprez(u)
#     r2=reprez(v)
#     if h[r1]>h[r2]:
#         tata[r2]=r1
#     else:
#         tata[r1]=r2
#         if h[r1] == h[r2]:
#             h[r2] += 1



# n,m,lm = citire("cost.in")
# # for i in lm:
# #     print(i)

# #muchii.sort(key=comp)   def comp(x) return x[2]
# lm.sort(key=lambda tup: tup[2])
# print (lm)

# tata=[0 for i in range(n+1)]
# h=[0 for i in range(n+1)]

# cost_minim=0

# for ind in lm: #reprezentantul nu va fi niciodata 0, ci daca este vorba doar de un nod, el va fi reprezentantul sau
#     if reprez(ind[0]) != reprez(ind[1]):
#         reuneste(ind[0], ind[1])
#         print(ind[0], ind[1])
#         cost_minim += ind[2]
        
# print("Vector de tati: ", tata)
# print("Costul minim este de: ", cost_minim)

     
            
