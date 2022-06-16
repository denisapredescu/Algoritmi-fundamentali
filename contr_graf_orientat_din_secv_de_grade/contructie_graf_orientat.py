# Construcția unui graf orientat cu secvențele de grade de intrare și ieșire date.  Se  citesc din  
# fișierul secvente.in: un  număr  naturaln>2, o  secvență s1 de  n  numere  naturaleși  o secvență s2
# de  n  numere  naturale. Să  se construiască,  dacă  se  poate,  un  graf  cu  secvența gradelor 
# interne s1 și cu secvența gradelor externe s2 (reducând problema la o problemă de flux maxim).În caz 
# afirmativ se vor afișa arcele grafului, altfel se va afișa mesajul NU.O(mn2)(unde m = suma numerelor 
# din s1= numărul de arce ale lui G)
import collections

# problema se rezuma la a determina un graf bipartit de flux maxim
# in cazul acela nu stiam daca este bipartit (verificam daca este) si in caz
# afirmativ determinam reteaua adaugand cont pe muchii si nodurile s si t (vezi implementarea de la bipartit)

# acum ni se dau gradele, deci costul de pe arce (acum nu o sa mai fie mereu 1 capacitatea)
# stim cate varfuri sunt... le dublam ca sa determinam cele doua partitii => adaugam s si t 
# si dupa dam drumul la flux => el determina fluxul maxim. Noi extragem arcele pe care exsta flux

def citire(filename):
    f = open(filename)
    nr_vf = int(f.readline())
    gr_int= [ int(x) for x in f.readline().split()]
    gr_ext= [ int(x) for x in f.readline().split()]
   
    f.close()
    return nr_vf,gr_int,gr_ext


def constructieRetea(file, s, t, gr_int, gr_ext):
    f = open(file, "w")
    #viz = 1 => leg la sursa
    #viz = -1 => leg la destinatie
    
    f.write(f"{t}\n")
    f.write(f"{s} {t}\n")
    f.write(f"{2 * nr_vf + nr_vf * (nr_vf-1)}\n")
    
    for i in range(1, nr_vf+1):
        # stiu cate arce vreau sa intre in fiecare nod
        f.write(f"{s} {i} {gr_ext[i - 1]} {0}\n")
             #capacitate flux   
    for i in range(1, nr_vf + 1):
        #stiu cate vreau sa iasa din fiecare nod
        f.write(f"{i + nr_vf} {t} {gr_int[i - 1]} {0}\n")
    for i in range(1, nr_vf+1):
        for j in range(nr_vf+1, 2*nr_vf+1):
            #nu trebuie sa punem arcele din ambele sensuri
            if i + nr_vf != j:
                f.write(f"{i} {j} {1} {0}\n")
            
    f.close()


# fix aceeasi citire pe care am avut-o in codul flux.py (de fapt am creat fisierul astfel 
# incat acum doar sa apelez/copiez ce am scris la flux)
def citireRetea(nume_fisier):
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


##################################################main############################

nr_vf,gr_int,gr_ext = citire("contructie_graf_orientat.in")
# print(nr_vf,gr_int,gr_ext)

if sum(gr_int) != sum (gr_ext):
    print("Nu se poate construi un astfel de graf")
else:
    constructieRetea("retea.in", 2*nr_vf + 1 , 2*nr_vf + 2, gr_int, gr_ext)  # dupa fisier am spus care sunt nodurile s si t
                
    n,m,la, s,t, intra, iese = citireRetea("retea.in");

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
        while v != s:  # cresc fluxul pe acel drum cu ip
            if tata[v] > 0:
                f[tata[v]][v] =  f[tata[v]][v] + ip
                v = tata[v]
            else:
                f[v][-tata[v]] =  f[v][-tata[v]] - ip  #ne intoarcem pe arc    => arcul (b, a) => f[a][b]
                v = -tata[v]

        ok, tata, viz = BFS(s, t, la, la_int, f, c)  #ok == 0 <=> nu ajunge in destinatie, fluxul este maxim


    for m1 in range(1, n+1):
        
        for m2, capac, flux in la[m1]:
            if  f[m1][m2] == 1 and m1 != s and m2 != t:
                print(m1, m2 - nr_vf)    # eu am in retea 2*n noduri pentru ca a trebuit sa dublez fiecare nod, acum la final vreau sa zic ca nodul x si (x + n) este acelasi
                    
    