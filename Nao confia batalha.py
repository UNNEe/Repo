def create_bf(n,m):
    return tiros(reorganize_bf([[[] for x in range(n)]
            for p in range(m)],m))


def reorganize_bf(bf,m):
    for p in range(m):
        bf[p]= list(input())
    return bf


def tiros(bf):
    s = int(input())
    locais = []
    for p in range(s):
        inp = [int(x) for x in input().split()]
        print(bf[inp[0]-1][inp[1]-1])
        if bf[inp[0]-1][inp[1]-1] == "#":
            bf[inp[0]-1][inp[1]-1] = "x"
            locais.append((inp[0]-1,inp[1]-1))
    return bf,locais


def busca(n, m):
    if ent1[0]-1 >= n >= 0 and ent1[1]-1 >= m >= 0:
        if battlefield[n][m] == ".":
            return True
        if battlefield[n][m] == "#":
            return False
        if battlefield[n][m] == "x":
            battlefield[n][m] = "."
        try:
            a = busca(n-1, m)
            b = busca(n+1, m)
            c = busca(n, m-1)
            d = busca(n, m+1)
            return a and b and c and d
        except:
            return False
    return True


ent1 = [int(x) for x in input().split()]
battlefield,locais = create_bf(ent1[0],ent1[1])
print(battlefield,locais)
soma = 0
for t in locais:
    if battlefield[t[0]][t[1]] == "x":
        if busca(t[0],t[1]):
            soma += 1
print(soma)