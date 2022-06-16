# O(m log n)
# exista circuite

import heapq

def citire(fisier):
    f=open(fisier) 
    n,m=[int(x) for x in f.readline().split()]
    la = [[] for i in range(n+1)]
    for i in range(m):
        m1,m2,c= [int(x) for x in f.readline().split()]
        la[m1].append([m2,c])
           
    b = int(f.readline())
    s = int(f.readline()) 
    f.close()
    return n,m,la, b,s


    
def dijkstra(sursa):
    
    d = [float('inf') for i in range(n+1)]
    tata = [0 for i in range(n+1)]
    d[sursa] = 0
    distanta = [0 for i in range(n+1)]
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
                        distanta[nod] = distanta[vf] + 1
                        tata[nod] = vf
                        heapq.heappush(h, [d[nod], nod])  # exista o muchie cu cost mai mic 
    
    return d, tata, distanta

def dinNouInS():
    cost_max = float("inf")
    nod = 0
    for m1 in range(1, n+1):
        for m2, cost in la[m1]:
            if m2 == s:
                if cost_max > d[m1] + cost:    #aici am suma 
                    if b >= d[m1] + cost:
                        cost_max = cost + d[m1]
                        nod = m1
                        # print("se ajunge in s: ", m1, m2, cost, cost_max, nod)
                        
    return nod
            
    
n,m,la, b, s=citire("an2021.in")   #1-neorientat, #2-orientat

d, tata, distanta = dijkstra(s)
nod_dorit = 0
distanta_nod = 0
cost_nod = 0
for i in range(1, n+1):
    if d[i] <= b and d[i] > cost_nod and distanta[i] > distanta_nod:
        cost_nod = d[i]
        distanta_nod = distanta[i] 
        nod_dorit = i
# print(d)
# print(tata)
# print(distanta)
# print(cost_nod, distanta_nod)
print(f"v={distanta_nod}")
drum = []
while tata[nod_dorit] != 0:
    drum.append(nod_dorit)
    nod_dorit =  tata[nod_dorit]
drum.append(nod_dorit)
drum.reverse()
print(drum)

nod = dinNouInS()
circuit = [s, nod]
# print(s, nod, end = " ")
while nod != s:
    nod = tata[nod]
    circuit.append(nod)
    # print(nod, end = " ")
circuit.reverse()
print(circuit)