#fisier n-muchii impuse, n randuri cu muchiile si costul, apoi Kruskalul normal

def citire(fisier):   # citire(numefisier)
    f=open(fisier) #open(numefisier)
    imp=int(f.readline())
    muchii_impuse = []

    for i in range(imp):
        m1,m2,c = [int(x) for x in f.readline().split()]
        muchii_impuse.append([m1,m2,c])

    n,m=[int(x) for x in f.readline().split()]
    lm = []  #lista de muchii
    #doua noduri au aceeasi culoare daca au acelas reprezentant => nu ne pasa muchia cum este scrisa
    #pentru noi [n1,n2,c] == [n2,n1,c]

    for i in range(m):
        m1,m2,c= [int(x) for x in f.readline().split()]
        if [m1,m2,c] not in muchii_impuse:
            lm.append([m1,m2,c])
    f.close()
    return n,m,lm,muchii_impuse

def comp(x):
     return x[2]

def reprez(u):    #determin reprezentantul nodului u    
    if tata[u] == 0:
        return u

    tata[u] = reprez(tata[u])   #fac mai usoara determinarea tatalui
    return tata[u]

            
def reuneste(u,v):
    ru=reprez(u)
    rv=reprez(v)
    if h[ru]>h[rv]:
        tata[rv]=ru
    else:
        tata[ru]=rv
        if h[ru] == h[rv]:
            h[rv] += 1


def kruskal_muchii_impuse():
    cost_minim=0
    lm.sort(key=comp)   
    print (lm)
    
    verif = 0

    for x, y, c in muchii_impuse: #reprezentantul nu va fi niciodata 0, ci daca este vorba doar de un nod, el va fi reprezentantul sau
        if reprez(x) != reprez(y):
            reuneste(x, y)
            print(x, y)
            cost_minim += c
            verif += 1
        else:
            # inseamna ca nu se accepta o muchie impusa
            return [], 0


    for x, y, c in lm: #reprezentantul nu va fi niciodata 0, ci daca este vorba doar de un nod, el va fi reprezentantul sau
        if reprez(x) != reprez(y):
            reuneste(x, y)
            print(x, y)
            cost_minim += c
            verif += 1
            if verif == n-1:   #s-a creat un arbore minim
                return tata, cost_minim
                

    # print("Vector de tati: ", tata)
    # print("Costul minim este de: ", cost_minim)
    
    # if verif > n-1:
    #     print("S-a format un ciclu!!")


n,m,lm, muchii_impuse = citire("cost.in")    
tata=[0 for i in range(n+1)]
h=[0 for i in range(n+1)]
tata, ok = kruskal_muchii_impuse()
if ok != 0:
    print(tata)
    print(ok)

     
            
