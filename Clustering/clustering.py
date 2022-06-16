def citire(fisier):
    f = open(fisier)
    lista = []
    n = int(f.readline())
    for i in range(n):
        lista.append(f.readline().replace('\n', ''))
    f.close()
    return n, lista

def creare_lista_de_muchii():  #Kruskal asteapta sa i se dea o lista de liste [[nod1, nod2, distanta]]
    muchii = []
    
    #pentru fiecare 2 cuvinte determin distanta de editare pe care o consider costul de la un cuvant la celalalt
    #graf neorientat
    #am muchie de la a la b si de la b la a
    for i in range(1, n):
        for j in range(i+1, n+1):
            distanta = distanta_de_editare(lista[i-1], lista[j-1])
            muchii.append([i, j, distanta])
            muchii.append([j, i, distanta]) 
    return muchii


def distanta_de_editare(cuv1, cuv2):  # Programare dinamica
    
    c = [[0 for j in range(len(cuv1)+1)] for i in range(len(cuv2)+1)]
    
    for i in range(1, len(cuv1)+1):
        c[0][i] = i
    for i in range(1, len(cuv2)+1):
        c[i][0] = i

    for i in range(1, len(cuv2)+1):
        for j in range(1, len(cuv1)+1):
            # print(i, j, cuv1[j-1], cuv2[i-1])
            if cuv1[j-1] == cuv2[i-1]:
                c[i][j] = c[i-1][j-1]  
                # print(i, j, cuv1[j-1], cuv2[i-1])
            else:
                c[i][j] = 1 + min (c[i-1][j], c[i-1][j-1], c[i][j-1])

    return c[len(cuv2)][len(cuv1)]
        
        
# n-k pasi din alg lui Kruskal
def comp(x):    #pt sortare
    return x[2]

def intializare(i): #varful i formeaza un arbore (o componenta/o multime)
    tata[i] = 0
    h[i] = 0

def reprez(u):    #determin reprezentantul nodului u    
    if tata[u] == 0:
        return u
    # compresie de cale
    tata[u] = reprez(tata[u])   #fac mai usoara determinarea tatalui (ca sa fac arborele mai mic in h => mai usor de parcurs)
    return tata[u]     

# reuniune ponderata
def reuneste(u,v):
    ru=reprez(u)
    rv=reprez(v)
    if h[ru]>h[rv]:
        tata[rv]=ru
    else:
        tata[ru]=rv
        if h[ru] == h[rv]:   #inaltimea se modifica doar daca cei 2 arbori au aceeasi inaltime. de ce? pt ca altfel arborele mai mic devine subarbore arborelui mai mare => nu se modifica h
            h[rv] += 1

#muchii.sort(key=comp)    def comp(x) return x[2]
def kruskal(pasi):   #varianta de Kruskal cu paduri ca sa fie mia eficient
    
    muchii.sort(key=comp)  
    # print (muchii)
    
    for i in range(1,n+1): #initializaz tata si h pentru fiecare componenta
        intializare(i)

    for u, v, c in muchii: 
        if reprez(u) != reprez(v):  #reprezentantul nu va fi niciodata 0, ci daca este vorba doar de un nod, el va fi reprezentantul sau
            reuneste(u, v)  # la varianta de clustering vrem doar sa se creeze o singura componenta din 2
            # print(c, lista[u-1], lista[v-1])

            pasi -= 1   #fac doar (n-k) pasi din algoritmul lui Kruskal (asa zice in teorie)
            if pasi == 0:
                return
 
 
def afisare_clase():
    viz = [0 for i in range(n+1)]  # tin evidenta cuvintelor care au fost afisate deja
    ok = 0  # sa nu mai fac pasi in plus pana la terminarea forurilor in cazul in care am afisat deja toate cuvintele
    for i in range(1, n):
        
        if viz[i] == 0:   # afisez doar daca nu a mia fost afisat deja    
            if ok != 0: # doar ca sa nu puna un spatiu in plus
                print()
                
            print(lista[i-1], end = " ")
            viz[i] = 1   # vizitez ca sa ia doar o singira data fiecare cuvant din lista
              
            for j in range(i+1,n+1):
                if viz[j] == 0 and reprez(i) == reprez(j):
                    print(lista[j-1], end=" ")
                    viz[j] = 1
                    ok += 1
        if ok == n:
            break

n, lista = citire("clustering.in")
muchii = creare_lista_de_muchii()
    
tata=[0 for i in range(n+1)]
h=[0 for i in range(n+1)]

k = 3 # numarul de clase
kruskal(n-k)     
afisare_clase()



            
            
        

    
    
