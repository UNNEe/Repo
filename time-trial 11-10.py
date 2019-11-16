from copy import deepcopy
def create_tree(num):
   city = {}
   value = {}
   for NODE in range(1,num + 1):
       city[NODE] = []
       value[NODE] = []
   for n in range(num-1):
       inpu = input().split()
       city[int(inpu[0])].append(int(inpu[1]))
       city[int(inpu[1])].append(int(inpu[0]))

   return city


def corte_imperio(c1,c2):
    imperio_cortado = deepcopy(list)

    imperio_cortado[c1].remove(c2)
    imperio_cortado[c2].remove(c1)

    return imperio_cortado


def adentrar_aos_reinos(origem,imp):
    soma = 0
    for node in imp[origem]:
        if node not in path:
            soma += 1
            adentrar_aos_reinos(node,imp)
            path.append(node)
    return soma


def corte(c1,c2,imp):
    a1 = adentrar_aos_reinos(c1,imp)
    a2 = adentrar_aos_reinos(c2,imp)

    return a1-a2


path = []
list = create_tree(int(input()))

for vertice in list:
    for adjacents in list[vertice]:
        new_rome = corte_imperio(vertice,adjacents)
        diferenca = corte(vertice, adjacents,new_rome)
        print(diferenca)



# transformar o imperio em um dicionario,
# "cortar" o imperio em duas partes usando o corte imperio
# contar a diferença de nodos/adjacentes usando o corte
# contar quantas cidades tem em cada parte com um algoritmo de busca em profundidade
# adentrar aos reinos

print(list)
