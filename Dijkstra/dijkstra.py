#merge pe orice tip de grafuri

import heapq

def citire(fisier, tip):
    f=open(fisier) 
    n,m=[int(x) for x in f.readline().split()]
    la = [[] for i in range(n+1)]
    for i in range(m):
        m1,m2,c= [int(x) for x in f.readline().split()]
        la[m1].append([m2,c])
        if tip == 1 :   #daca este neorientat, pun de doua ori muchia
           la[m2].append([m1,c])
    f.close()
    return n,m,la


    
def dijkstra(sursa):
    
    d = [float('inf') for i in range(n+1)]
    tata = [0 for i in range(n+1)]
    d[sursa] = 0
    h = []
    viz = [0]*(n+1)

    heapq.heappush(h, [d[sursa], sursa])
    
    while len(h) > 0:    
        
        cost, vf = heapq.heappop(h)
        
        if viz[vf] == 0:  #trebuie sa verificam ca nu s-a golit heapul
            viz[vf] = 1
            
            for nod, cost in la[vf]:
                if viz[nod] == 0:
                    if d[nod] > d[vf] + cost:    #aici am suma 
                        d[nod] = cost + d[vf]
                        tata[nod] = vf
                        heapq.heappush(h, [d[nod], nod])  # exista o muchie cu cost mai mic 
    
    return d, tata


n,m,la=citire("dijkstra.in", 1)   #1-neorientat, #2-orientat
# for i in la:
#     print(i)

vf_start = int(input("Sursa: "))


# print("Muchiile din traseu: ", end="")
# for i in range(1, len(tata)):
#     if d[i] != 100:
#         print("(",tata[i],",",i,")", end=" ")

# care este cel mai apropiat punct de control fata de varful de start
p_control=[int(x) for x in input("Puncte de control: ").split()]  # 3 4

d, tata = dijkstra(vf_start)   
print(d)
print(tata)

minim = float('inf')
destinatie = 0

for i in p_control:
    if d[i] < minim:
        minim = d[i]
        destinatie = i
        
drum = []
u = destinatie
drum.append(u)
while u!=vf_start:
    u = tata[u]
    drum.append(u)
drum.reverse()
print(drum)
        


# 6 8
# 2 4 2
# 4 1 12
# 4 5 16
# 1 5 20
# 1 6 10
# 5 6 15
# 5 3 30
# 3 6 1

# 1
# []
# [[4, 12], [5, 20], [6, 10]]
# [[4, 2]]
# [[5, 30], [6, 1]]
# [[2, 2], [1, 12], [5, 16]]
# [[4, 16], [1, 20], [6, 15], [3, 30]]
# [[1, 10], [5, 15], [3, 1]]
# 1 0 0
# 6 1 10
# 3 6 11
# 4 1 12
# 2 4 14
# 5 1 20
# [100, 0, 14, 11, 12, 20, 10]
# [0, 0, 4, 6, 1, 1, 1]
# Muchiile din traseu: ( 0 , 1 ) ( 4 , 2 ) ( 6 , 3 ) ( 1 , 4 ) ( 1 , 5 ) ( 1 , 6 )



# 1
# []
# [[4, 12], [5, 20], [6, 10]]
# [[4, 2]]
# [[5, 30], [6, 1]]
# [[2, 2], [1, 12], [5, 16]]
# [[4, 16], [1, 20], [6, 15], [3, 30]]
# [[1, 10], [5, 15], [3, 1]]
# 1 0 0
# 6 1 10
# 3 6 1
# 4 1 12
# 2 4 2
# 5 6 15