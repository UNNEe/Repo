def maximo(n):
    p = 0
    for v in n:
        if v > p: p = v
    return p

def create_matiz(l1):
    matrix = [[0 for c in range(l1[0])]
            for l in range(l1[0])]
    return matrix


def organize_matriz(l1):
    matriz = create_matiz(l1)
    for p in range(l1[1]):
        inp = [int(p) for p in input().split()]
        matriz[inp[0]][inp[1]] = inp[2]
        matriz[inp[1]][inp[0]] = inp[2]
    return matriz


def minimum(distances,visited):
    low = (float("inf"),float("inf"))
    for v in range(ent1[0]):
        if not visited[v] and low[0] > distances[v]:
            low = distances[v],v
    return int(low[1])
def dijkstra_shortest(matrix,origin):
    visi = [False] * ent1[0]
    dist = [float("inf")] * ent1[0]
    dist[origin] = 0

    for count in range(ent1[0]):
        u = minimum(dist,visi)
        visi[u] = True

        for v in range(ent1[0]):
            if matrix[u][v] > 0 and not visi[v] and dist[v] > dist[u] + matrix[u][v]:
                dist[v] = dist[u] + matrix[u][v]

    return maximo(dist)


ent1 = [int(l) for l in input().split()]
matriz = organize_matriz(ent1)
menor = float("inf")
for j in range(ent1[0]):
    maior_minimo = dijkstra_shortest(matriz,j)
    print(maior_minimo)
    if maior_minimo < menor:
        menor = maior_minimo
print(menor)

