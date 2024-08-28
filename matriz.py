listas_anidad =[[1,2,3],
                [4,5,6],
                [7,8,9]]
print (listas_anidad) 
print(f"{listas_anidad[0]},\n{listas_anidad[1]},\n{listas_anidad[2]}")
print(listas_anidad[0][0])
print(listas_anidad[2][2])
for row in listas_anidad:
    print(row)
for row in listas_anidad:
    for element in row:
        print(element)