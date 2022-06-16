# determinarea componentelor tare conexe intr-un graf
# am nevoie de transpusa pentru grafurile orientate

def citire(file, tip): #am pus tipul grafului ca parametru
    # ar merge trimis ca parametru si numele fisierului, sa nu il fixam ca fiind graf.in:
    # citire(numefisier,tip)
    f=open(file) #open(numefisier)
    n,m=[int(x) for x in f.readline().split()]
    la = [[] for i in range(n+1)]
    for i in range(m):
        m1,m2= [int(x) for x in f.readline().split()]
        la[m1].append(m2)
        if tip == 1: #tip = 1 neorientat; tip = 2 orientat
            la[m2].append(m1)
    f.close()
    return n,m,la


def DFS(start,la, tip="G"):
    viz[start] = 1

    for vf in (la[start]):
        if viz[vf] == 0:
            DFS(vf,la,tip)
            
    # am nevoie de tranpusa pentru a depista toate componentele tare conexe (caz graf orientat) => cand ajung la un nod 
    # din care nu mai pot continua, incep afisarile => diferenta fata de vector este ca acum nu voi
    # mai avea toate nodurile la un loc, ci le afisez doar pe cele ce fac parte dintr-o componenta, 
    # apoi se va apela functia dfs si pentru celelalte noduri ce nu fac parte din acea componenta
    
    # de ce se creeaza componentele? pentru ca initial am pastrat doar nodurile in care pot ajunge
    # apoi in transpusa vad daca pot merge in sens invers: de ce? pentru ca in graf orientat (a, b) != (b, a)
    if(tip == "transpus"):   
        print(start, end=" ")
        
    fin.append(start)    
    # det. nodurile in ordinea frunze - parinte (pe modelul DFS ului adica ma duc pana nu mai am 
    # unde in jos, pun valoarea finala in vector, urc un pas in arbore, vad daca mai am alti copii 
    # si in functie de asta ma duc in copil sau salvez valoarea in vector, algoritmul se repeta pana
    # cand nu mai am noduri netrecute in vector)
    
    # cand va intra in dfs ul din transpusa, va continua sa completexe numerele in fin, dar nu este 
    # problema pentru ca oricum trecute ca vizitate pe parcurs si nu va afisa din nou datele


def construieste_transpusa(n, la):
    la_trans = [ [] for i in range(n+1)]
    for x in range(1, n+1):
        for y in la[x]:
            la_trans[y].append(x)
    return la_trans

###############################################################################################3

n,m,la=citire("kosaraju.in", 2)     # 1 = graf neorientat

# for i in range(1,n+1):
#     print(i,":",end=" ")
#     for j in la[i]:
#         print(j,end=" ")
#     print()

fin = []   #pastrez drumul de la frunza pana la radacina
viz = [0 for x in range(len(la)+1)]

for i in range (1,n+1):
    if viz[i] == 0:
        DFS(i,la)

print(fin[::-1])  


la_trans=construieste_transpusa(n,la)
# print(la_trans)
# for i in range(1,n+1):
#     print(i,":",end=" ")
#     for j in la_trans[i]:
#         print(j,end=" ")
#     print()

viz = [0 for x in range(len(la)+1)]
for i in fin[::-1]:    # iau nodurile in ordine inversa a DFS ului, adica radacina sa fie prima
    if viz[i] == 0:
        DFS(i, la_trans, "transpus")
        print()
        
