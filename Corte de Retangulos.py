# questao e entradas:
# https://olimpiada.ic.unicamp.br/pratique/pu/2017/f2/papel/


# inp2 = [int(a) for a in input().split()]
# inp = len(inp2)

inp2 = [10, 20, 10, 40, 50]


def separar(tira,corte):       # faz um 'corte' no retangulo, separando a parte superior da parte inferior
    if tira > corte: return 1  # se o retangulo atual ficar acima da area de corte retorna 1 [maior]
    return 0                   # retorna 0 [menor]


def varrer(lista,corte):
    pedacos = []               # uma matriz N x 1 que diz quais retangulos estao acima do corte [1]
    for n in lista:            # e quais estao abaixo [0]
        pedacos.append(separar(n,corte))
    return pedacos


def verificar(conjunto):       # faz uma aglutinaçao no conjunto de pedaços
    cont = 0                   # transformando uma lista = [1 ,1 ,1 ,0 ,0 ,1]
    sequencia = False          # em uma variavel = 2
    for n in conjunto:
        if n == 1 and not sequencia:
            cont += 1
            sequencia = True
        if n == 0 and sequencia:
            sequencia = False
    return cont


ideal = 0
for p in inp2:                 # a area de corte é definida apartir da propria entrada
    conj = varrer(inp2, p)
    a = verificar(conj)
    if a > ideal:
        ideal = a
print(ideal+1)
