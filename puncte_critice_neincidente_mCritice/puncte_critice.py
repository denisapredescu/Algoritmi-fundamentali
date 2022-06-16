def citire(tip): #am pus tipul grafului ca parametru, nu ca data in fisier
    # ar merge trimis ca parametru si numele fisierului, sa nu il fixam ca fiind graf.in:
    # citire(numefisier,tip)
    f=open("graf.in") #open(numefisier)
    n,m=[int(x) for x in f.readline().split()]
    la = [[] for i in range(n+1)]
    for i in range(m):
        m1,m2= [int(x) for x in f.readline().split()]
        la[m1].append(m2)
        if tip==1: #tip = 1 neorientat; tip = 2 orientat
            la[m2].append(m1)
    f.close()
    return n,m,la

n,m,la = citire(1) #graf neorientat

viz=[0]*(n+1)
niv=[0]*(n+1)
niv_min=[0]*(n+1)
pc=[False]*(n+1)
nr_pc = [0] * (n+1)
tata = [0] *(n+1)

def DFS(i):
    viz[i] = 1
    # nr_pc[i] += 1
    
    niv_min[i] = niv[i]  #initializez nivelul minim
    for j in la[i]:
        
        if viz[j]==0:
            viz[j] = 1
            tata[j] = i
            # print( i, j, nr_pc[i], nr_pc[j])
            # niv[j]=niv[i]+1
            DFS(j)

            #test p c - pentru varfuri diferite de radacina
            # if niv_min[j] == niv[i]:   # (>) inseamna ca daca tai parintele, legatura cu fiul si arborele lui vor cadea (graful nu va mai fi conex). 
            #                            # Daca am (==) inseamna ca daca tai parintele, se va taia tot ciclul (arbore) pe care il tinea parintele => din nou se strica conexitatea  
            #     # print(i," punct critic")
            #     pc[i]=True
                # nr_pc[i] += 1
                
            # niv_min[i]=min(niv_min[i],niv_min[j])
            
        else:
            # if niv[j] < niv[i]-1:   #j = stramos al lui i
            #     niv_min[i] = min(niv_min[i], niv[j])      
            if j!=tata[i]: 
                x=i
                while x!=j:    #afisez ciclul
                    print(x,end=" ")
                    x=tata[x]
                print(j,i)
            nr_pc[j] += 1 

# for i in range(1,n+1):
#     if viz[i]==0:
#         DFS(i)    # este conex... deci doar incep din 1
# print(pc)
DFS(5)
print(nr_pc)
  
# for i in range(1,n+1):
#     if pc[i] == True:
#         print(i, nr_pc[i])


