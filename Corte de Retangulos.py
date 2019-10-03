# inp2 = [int(a) for a in input().split()]
# inp = len(inp2)

inp2 = [10, 20, 10, 40, 50]

def separar(tira,corte):
    if tira > corte: return 1
    return 0

def varrer(lista,corte):
    pedacos = []
    for n in lista:
        pedacos.append(separar(n,corte))
    return pedacos

def verificar(conjunto):
    cont = 0
    sequencia = False
    for n in conjunto:
        if n == 1 and not sequencia:
            cont += 1
            sequencia = True
        if n == 0 and sequencia:
            sequencia = False
    return cont
ideal = 0
for p in inp2:
    conj = varrer(inp2, p)
    a = verificar(conj)
    if a > ideal :
        ideal = a
print(ideal+1)