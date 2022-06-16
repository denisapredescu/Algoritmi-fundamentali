#Sortare topologica
#graf orientat

def citire(filename):
    f = open(filename)
    n, m = [ int(x) for x in f.readline().split()]
    la = [[] for x in range(n+1)] 
    g_int = [0]*(n+1)  #gradul intern al fiecarui nod
    for i in range(m):
        m1, m2 = [ int(x) for x in f.readline().split()]
        la[m1].append(m2);
        g_int[m2] += 1
    f.close()
    
    return n,m,la,g_int

#pun in lista nodurile cu gradul intern 0, apoi parcurg pe rand nodurile 
#respective, adaugand la ele pe acelea care, dupa eliminare (scaderea gradului), au gradul intern 0
   
def SortareTopologica():
    sTop=[]
    poz=0
    for x in range(1, len(g_int)):
        if g_int[x] == 0:
            sTop.append(x)
            
    while len(sTop) != n :
        for i in la[sTop[poz]]:
            g_int[i] -= 1
            if g_int[i] == 0:
                sTop.append(i)
        poz += 1
    return sTop

n,m,la, g_int = citire("sortare.in")
sTop = SortareTopologica()
print(sTop)





# def eliminare(start):
#     for i in la[start]:
#         g_int[i] -= 1
        
#     la[start].clear()

#varianta mai putin eficienta!!!!!!!!
# sTop = []
# poz = 0
# while len(sTop) != n:
#     for x in range(1, len(g_int)):
#         if g_int[x] == 0:
#             sTop.append(x)
#             g_int[x] = -1
#     eliminare(sTop[poz])
#     poz += 1 