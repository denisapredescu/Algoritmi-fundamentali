import collections

def citire(nume_fisier):
    g = open(nume_fisier)
    n = int(g.readline())
    s, t = [int(x) for x in g.readline().split()]
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
    
    return n, m, la, s, t, intra, iese


def BFS(s, t, la, la_int, f, c):
     
    q = collections.deque()  #coada
    q.append(s)    # adaug la sfarsit
    
    viz = [0 for i in range(n+1)]
    viz[s] = 1
    tata = [0 for i in range(n+1)]
    
    while len(q) > 0:
        x = q.popleft()  # scot un element din coada
        
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
                
                
n, m, la, s, t, intra, iese = citire("retea.in");

# Conditiile pentru a fi flux coerct: marginirea si suma gradelor de intrare == suma gradelor de iesire
ok = 1
for i in range(1,n+1):
    if i != s and i != t:
        if intra[i] != iese[i]:
            print("Nu intra cat iese")
            ok = 0
            break
for linie in la:
    for m2, c, f in linie:
        if f > c:
            print("Capacitatea este mai mare")
            ok = 0
            break
        
if ok == 1:
    print("DA")
    
    f = [[0 for j in range(n+1)] for i in range(n+1)]  #matrice de flux
    c = [[0 for j in range(n+1)] for i in range(n+1)]  #matrice de capacitati
    
    # am impartit vecinii in 2: cei care sunt pe arce normale (ei se gasesc in la) si cei pe arcele de intoarcere
    # cei cu arce de intoarce trebuie retinuti diferit pentru ca fluxul disponibil se calculeaza altfel
    
    # ceva gen => ma uit in lista sa vad daca am arc normal intre a si b => daca da, atunci pentru a calcula fluxul care
    # mai poate fi introdus fac c[a][b] - f[a][b]; intru si in matricea de arce inverse si ma uit daca nu am vreun arc care 
    # intra in vf a => daca gasesc arcul (b, a) inseamna ca fluxul ce poate fi trimis inapoi este de f[b][a]
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
        while v != s:  # determin cu cat pot sa cresc fluxul pe acel drum
            if tata[v] > 0:
                a = c[tata[v]][v] - f[tata[v]][v]
                v = tata[v]
            else:
                a = f[v][-tata[v]]   #ne intoarcem pe arc    => arcul (b, a) => f[a][b]
                v = -tata[v]   #stiu ca este arc invers  
            ip = min(ip, a)
        
        v = t
        while v != s:   # cresc fluxul pe acel drum cu ip
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
            print( m1, m2, f[m1][m2])
            
    print(val_flux)    #val flux == val taieturii
    for m1 in range(1, n+1):
        for m2, capac, flux in la[m1]:   # arc: m1-viz si m2-neviz  ==> taietura (flux == capacitate)
            if viz[m1] == 1 and viz[m2] == 0:
                print(m1, m2)
                
            
            
        
    
        
        
            
                
                
                
        


        
    
    
            
    
           
        
    

    
