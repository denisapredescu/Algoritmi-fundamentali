# determin daca exista circuite / cicluri si le afisez

def citire(filename, tip): 
    
    f = open(filename) 
    n,m = [int(x) for x in f.readline().split()]
    la = [[] for i in range(n+1)]
    for i in range(m):
        m1,m2 = [int(x) for x in f.readline().split()]
        la[m1].append(m2)
        if tip==1: #tip = 1 neorientat; tip = 2 orientat
            la[m2].append(m1)
    f.close()
    return n,m,la,tip


# diferenta intre orientat si neorientat este ca in cazul unui graf orientat daca am arcele (x, y) so (y, x) inseamna ca am un circuit
# deci nu mai trebuie sa fac verificarea ca nodul vecin sa nu fie tatal nodului curent

def DFS(x):
    viz[x] = 1
    
    for vf in la[x]:
        if viz[vf] == 0:
            tata[vf] = x
            DFS(vf)         #mai buna var cu niv :)
        else:
            global ok
            if tip == 1:  #neorientat
                if  tata[x] != vf and viz[vf] == 1:   #daca exista o legatura cu un nod ce se afla mai sus ca el in arbore, exista ciclu
                    print("Ciclu inchis de arcul de intoarcere", x , vf)
                    print("Ciclul: (", x, end=" ")
                    vf_ciclu = x
                    while vf_ciclu != vf:
                        print(tata[vf_ciclu], end=" ")
                        vf_ciclu = tata[vf_ciclu]
                    print(x, ")")
                    ok = 1
            elif tip == 2:  #orientat
                if viz[vf] == 1:   #inseamna ca exista un arc intre nodul curent si un stramos al lui => circuit
                    vf_circuit = x   
                    print("Circuit inchis de arcul de intoarcere", x , vf)
                    print("Circuit (", vf_circuit,  end=" ")
                    while vf_circuit != vf:
                        print(tata[vf_circuit], end=" ")
                        vf_circuit = tata[vf_circuit]
                    print(x,")")
                    ok = 1
    viz[x] = 2   #am terminat complet cu varful x # ??????????????


n,m,la,tip=citire("circuite.in", 1) #graf neorientat
for i in range(1,n+1):
    print(i,":",end=" ")
    for j in la[i]:
        print(j,end=" ")
    print()
    

tata = [0 for x in range(len(la)+1)] #ca sa stiu care este tatal fiecarui nod
viz = [0 for x in range(len(la)+1)]
 
ok = 0

for i in range(1, n+1):
    if viz[i] == 0:
        DFS(i)
        
if ok == 0:
    print("Nu exista cicluri in graful dat")


# pentru orientat
# 6 10
# 1 2
# 2 1
# 2 4
# 1 3
# 3 5
# 3 6
# 6 1
# 6 3
# 6 5
# 6 4

# pentru neorientat
# 8 11
# 1 2
# 1 8
# 1 3
# 2 8
# 2 3
# 3 7
# 5 3
# 5 7
# 5 6
# 6 4
# 4 7