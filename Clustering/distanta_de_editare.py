cuv1 = "examen"
cuv2 = "restanta"
print(len(cuv1))
c = [[0 for j in range(len(cuv1)+1)] for i in range(len(cuv2)+1)]

for i in range(1, len(cuv1)+1):
    c[0][i] = i
    
for i in range(1, len(cuv2)+1):
    c[i][0] = i
  
print(c)
  
for i in range(1, len(cuv2)+1):
    for j in range(1, len(cuv1)+1):
        # print(i, j, cuv1[j-1], cuv2[i-1])
        if cuv1[j-1] == cuv2[i-1]:
            c[i][j] = c[i-1][j-1]  
            # print(i, j, cuv1[j-1], cuv2[i-1])
        else:
            c[i][j] = 1 + min (c[i-1][j], c[i-1][j-1], c[i][j-1])
                   
print(c[len(cuv2)][len(cuv1)])