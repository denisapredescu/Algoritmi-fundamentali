#doar pe neorientate
# O(m log n)

import heapq

def citire(fisier):
    f=open(fisier) 
    n,m=[int(x) for x in f.readline().split()]
    la = [[] for i in range(n+1)]
    for line in f:
        m1,m2,c= [int(x) for x in line.split()]
        la[m1].append([m2,c])
        la[m2].append([m1,c])
    f.close()
    return n,m,la


def prim(vf):    
    d = [float("inf") for i in range(n+1)]
    tata = [0 for i in range(n+1)]
    viz = [0]*(n+1)
    h = [] # coada de prioritati
    d[vf] = 0    
    
    heapq.heappush(h, [d[vf], vf])  # bag in coada primul nod si costul acestuia = infinit
    
    for i in range(n):   # trebuie sa scot din lista doar n numere (pt ca e arbore)
        
        c, u = heapq.heappop(h) #scot varful de cost minim, dar il caut pe acela care inca nu a fost vizitat
        while viz[u] == 1:
            c, u =  heapq.heappop(h)  
        # se opreste la primul vf nevizitat

        viz[u] = 1  # il trec ca si vizitat
        print(u)
        for nod, cost in la[u]:  # pun si vecinii lui nevizitati in coada
            if viz[nod] == 0 and d[nod] > cost:   # vecinii carora le dau costul minim (verific daca costul curent este mai mic decat costul minim de pana acum)
                d[nod] = cost
                tata[nod] = u
                heapq.heappush(h, [cost, nod])  # exista o muchie cu cost mai mic 
        
    # ok, pana acum am creat arborele deci in vectorul de tati am retinut succesiunea nodurilor
    # acum vreau sa determin costul traseului
    cost_total = 0
    for vf in range(1, n+1):
        if tata[vf] != 0:
            cost_total += d[vf]
            print(vf, tata[vf])
    print("Costul total:", cost_total)
                

n,m,la=citire("prim.in") 
# for i in la:
#     print(i)
    
prim(1)



# #doar pe neorientate
# import heapq

# vf_start = int(input())

# def citire(fisier):
#     f=open(fisier) 
#     n,m=[int(x) for x in f.readline().split()]
#     la = [[] for i in range(n+1)]
#     for i in range(m):
#         m1,m2,c= [int(x) for x in f.readline().split()]
#         la[m1].append([m2,c])
#         la[m2].append([m1,c])
#     f.close()
#     return n,m,la


# n,m,la=citire("prim.in") 
# for i in la:
#     print(i)
    
# d = [100 for i in range(n+1)]
# tata = [0 for i in range(n+1)]
# d[vf_start] = 0
# h = []

# vf = vf_start

# vizitate = [0]*(n+1)
# vizitate[vf] = 1  #pentru ca alg sa functioneze ok, un nod trebuie sa fie vizitat si celalalt nu

# scoase = 0 # cate nr am scos din heap;  la final scoase == n

# while scoase != n:
    
#     print(vf, tata[vf], d[vf])
#     vizitate[vf] = 1
    
#     for nod, cost in la[vf]:
#         if vizitate[nod] == 0 and d[nod] > cost: 
#             d[nod] = cost
#             tata[nod] = vf
#             heapq.heappush(h, [cost, nod])  # exista o muchie cu cost mai mic 
    
#     #cost, vf = heapq.heappop(h)
#     while vizitate[vf] == 1 and len(h) > 0 :
#         cost, vf = heapq.heappop(h)
#     scoase += 1
