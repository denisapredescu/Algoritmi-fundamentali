#graf orientat

def citire(nume_fisier):
    f = open(nume_fisier)
    n, m = [int(x) for x in f.readline().split()]
    lista_arce = []
    for linie in f:
        lista_arce.append([int(x) for x in linie.split()])
        
    print(lista_arce)
    
    return n, lista_arce

#are nevoie de vectorul de tati si de lista de adiacenta
def b_ford(n, lista_arce, start):
    d = [float("inf") for i in range(n+1)]  #infinit
    tata = [0 for i in range(n+1)]
    d[start] = 0
    
    for i in range (n-1):  #trebuie sa mearga de (n-1) ori
        for u,v,cost in lista_arce:
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                tata[v] = u
                
    are_circuit_negativ = False
    for u,v,cost in lista_arce:
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                tata[v] = u
                are_circuit_negativ = True
                vf_modificat = v    #retin varful care s-a actualizat
        
    return d, tata, are_circuit_negativ, vf_modificat


def afisare_circuit_neg(v, tata, n):
    x = v           # nu stim sigur ca apartine circuitului
    for i in range(n):
        x = tata[x]   # se duce n pasi inapoi
    
    circuit = [x]
    y = tata[x]
    while y != x:    #am mers din tata in tata pana am dat din nou de x
        circuit.append(y)
        y=tata[y]
        
    circuit.append(x)
    circuit.reverse()
    
    return circuit
    
    
    
n, lista_arce = citire("bford.in")

sursa = 1
d, tata, are_circuit_negativ, v = b_ford(n, lista_arce, sursa)
                
if are_circuit_negativ == True:
    print("are circuit negativ!")
    circuit =  afisare_circuit_neg(v,tata,n)
    print(circuit)
else:
    print(d)

              
