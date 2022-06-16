# calculeaza matricea de distante
# O(n^3)
# determina daca exista un circuit negativ

# algoritm pentru grafuri orientate

# d va fi matricea distantelor minime
# p matricea tatilor ca sa determinam traseul drumului minim

def citire(fisier):
    f=open(fisier) 
    n,m=[int(x) for x in f.readline().split()]
    
    # initializez matricile
    d = [[float('inf') for i in range(n+1)] for j in range(n+1)]
    p = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        d[i][i] = 0
    
    for i in range(m):
        m1,m2,c= [int(x) for x in f.readline().split()]
        d[m1][m2] = c
        p[m1][m2] = m1
        
    f.close()
    return n, d, p

def floyd(n,d,p):
    for k in range (1, n+1):  # varfurile intermediare
        for i in range (1, n+1):
            for j in range (1, n+1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = p[k][j]
                    
                    if i == j and d[i][j] < 0:
                         return 0, d, p
                    
    # for i in range(1, n+1):
    #     if d[i][i] < 0:
    #         return 0, d, p
    return 1, d, p

       
def drum(i, j):
    if i != j:
        drum(i, p[i][j])
    print(j, end = " ")
               
n, d, p = citire("floydWarshall.in")
ok, d, p = floyd(n, d, p)

if ok == 1:
    print("Matricea de distante minime: ")
    for i in d[1::]:
        print(i[1::])
    print("Matricea de trasee: ")
    for i in p[1::]:
        print(i[1::])
    
    s = 3
    t = 2
    print(f"Drumul de la {s} la {t}: ", end = "")
    drum(s,t)
else: 
    print("A fost detectat un circuit negativ!")
    
    


        

