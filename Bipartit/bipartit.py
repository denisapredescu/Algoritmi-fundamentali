def citire(filename):
    f = open(filename)
    n, m = [ int(x) for x in f.readline().split()]
    la = [[] for x in range(n+3)]  # +2 pentru s si t
    for i in range(m):
        m1, m2 = [ int(x) for x in f.readline().split()]
        la[m1].append((m2));
        la[m2].append((m1));

    f.close()
    return n,m,la


#pas 1: colorare / oprire daca nu se poate colora
#pas 2: cream un fisier in care punem datele pentru a putea fi preluate de flux

def dfs(x):  
    
    for y in la[x]:
        if viz[y] == 0:
            tata[y] = x
            viz[y] = -viz[x]   #culoare opusa fata de tata
            dfs(y)
        else:      #test daca au aceeasi culoare
            if viz[x] == viz[y]:
                print("Graful nu este bipartit")
                nodCurent = x     #cel deja vizitat
                while nodCurent != y:  
                    print(nodCurent, end=" ")
                    nodCurent = tata[nodCurent]
                print(y, x)
                exit()
   
   
# 6    numarul de noduri
# 1 6
# 8
# 1 3 6 3
# 1 5 8 2 
# 3 2 5 0 
# 3 4 3 3 
# 5 4 4 2 
# 2 6 7 0 
# 4 6 5 5 
# 3 5 1 0

def constructieRetea(file, s, t):
    f = open(file, "w")
    #viz = 1 => leg la sursa
    #viz = -1 => leg la destinatie
    
    f.write(f"{t}\n")
    f.write(f"{s} {t}\n")
    f.write(f"{n+m}\n")
    
    for i in range(1, n+1):
        if viz[i] == 1:
            f.write(f"{s} {i} {1} {0}\n")
             #capacitate flux
            
            for j in la[i]:    #arcele din reteaua initiala
                f.write(f"{i} {j} {1} {0}\n")       
        else:
            #nu trebuie sa punem arcele din ambele sensuri
            f.write(f"{i} {t} {1} {0}\n")
            
    f.close()
    
    
n, m , la = citire("bipartit.in")
#print(n,la)
viz = [0 for x in range(len(la))]
tata = [0 for x in range(len(la))]
viz[1] = 1 
dfs(1)

constructieRetea("retea.in", n+1, n+2)


import collections

def citire(nume_fisier):
    g = open(nume_fisier)
    n= int(g.readline())
    s,t = [int(x) for x in g.readline().split()]
    m = int(g.readline())
    intra = [0 for i in range(n+1)]
    iese =  [0 for i in range(n+1)]
    la = [[] for i in range(n+1)]
    for i in range(m):
        m1,m2,c,f= [int(x) for x in g.readline().split()]
        la[m1].append([m2,c,f])
        intra[m2] = intra[m2] + f
        iese[m1] = iese[m1] + f
    g.close()
    return n,m,la, s, t, intra, iese


def BFS(s, t, la, la_int, f, c):
     
    q = collections.deque()
    q.append(s)
    
    viz = [0 for i in range(n+1)]
    viz[s] = 1
    tata = [0 for i in range(n+1)]
    
    while len(q) > 0:
        x = q.popleft()
        
        for y,capac,flux in la[x]:
            if viz[y] == 0 and f[x][y] < c[x][y]:    #doar daca mai se poate pune flux
                viz[y] = 1
                tata[y] = x
                q.append(y)
                if y == t:
                    return 1, tata, viz
        
        for y in la_int[x]:
            if viz[y] == 0 and f[y][x] > 0:    # flux > 0, daca am ce lua inapoi
                viz[y] = 1
                tata[y] = -x   #este arc invers
                q.append(y)
    
    return 0, tata, viz
                
                
n,m,la, s,t, intra, iese = citire("retea.in");

f = [[0 for j in range(n+1)] for i in range(n+1)]  #matrice de flux
c = [[0 for j in range(n+1)] for i in range(n+1)]  #matrice de capacitati
la_int = [[] for i in range(n+1)]
for m1 in range(1,n+1):
    for m2,capac,flux in la[m1]:
        f[m1][m2]=flux
        c[m1][m2]=capac
        la_int[m2].append(m1)   #lista de adiacenta pt vf care intra 

ok, tata, viz = BFS(s, t, la, la_int, f, c)
while ok == 1:
    ip = float('inf')
    
    v = t
    while v != s:
        if tata[v] > 0:
            a = c[tata[v]][v] - f[tata[v]][v]
            v = tata[v]
        else:
            a = f[v][-tata[v]]   #ne intoarcem pe arc
            v = -tata[v]   #stiu ca este arc invers
        ip = min(ip, a)
    
    v = t
    while v != s:
        if tata[v] > 0:
            f[tata[v]][v] =  f[tata[v]][v] + ip
            v = tata[v]
        else:
            f[v][-tata[v]] =  f[v][-tata[v]] - ip  #ne intoarcem pe arc
            v = -tata[v]

    ok, tata, viz = BFS(s, t, la, la_int, f, c)  #ok == 0 <=> nu ajunge in destinatie, fluxul este maxim

val_flux = 0
for m2, capac, flux in la[s]:
    val_flux += f[s][m2]
print(val_flux)

#fluxul pe fiecare arc
for m1 in range(1, n+1):
    
    for m2, capac, flux in la[m1]:
        if  f[m1][m2] == 1 and m1 != s and m2 != t:
            print( m1, m2)
                