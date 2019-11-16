class Dados:
    def __init__(self,nome=None,plano=None,gravidade=None):
        self.nome = nome
        self.plano = plano
        self.gravidade = gravidade


class Node:
    def __init__(self,dado=None):
        self.dado = dado
        self.right = None
        self.left = None
        self.pai = None


class BinaryTree:
    def __init__(self):
        self.Null = Node()
        self.raiz = self.Null

    def inserir(self,valor):
        string = valor.split(" ")
        data = Dados()
        data.nome = string[0]
        data.plano = self.__planos(string[1])
        data.gravidade = int(string[2])
        objeto = Node(data)
        objeto.left = self.Null
        objeto.right = self.Null

        if self.raiz == self.Null:
            self.raiz = objeto
        else:
            n = self.raiz
            y = None
            while n != self.Null:
                y = n
                if objeto.dado.plano == n.dado.plano:
                    if objeto.dado.gravidade > n.dado.gravidade:
                        n = n.right
                    elif objeto.dado.gravidade < n.dado.gravidade:
                        n = n.left
                    elif objeto.dado.nome < n.dado.nome:
                        n = n.right
                    else:
                        n = n.left
                elif objeto.dado.plano > n.dado.plano:
                    n = n.right
                else:
                    n = n.left

            objeto.pai = y
            if y is None:
                self.raiz = objeto
            elif objeto.dado.plano == y.dado.plano:
                if objeto.dado.gravidade > y.dado.gravidade:
                    y.right = objeto
                elif objeto.dado.gravidade < y.dado.gravidade:
                    y.left = objeto
                elif objeto.dado.nome < y.dado.nome:
                    y.right = objeto
                else:
                    y.left = objeto
            elif objeto.dado.plano < y.dado.plano:
                y.left = objeto
            else:
                y.right = objeto

    def __planos(self,plano):
        if plano == "premium":
            return 5
        if plano == "diamante":
            return 4
        if plano == "ouro":
            return 3
        if plano == "prata":
            return 2
        if plano == "bronze":
            return 1
        if plano == "resto":
            return 0
    def printer(self,node):
        if node != self.Null:
            self.printer(node.right)
            print(node.dado.nome)
            self.printer(node.left)

t = BinaryTree()
ent = int(input())
for p in range(ent):
    t.inserir(input())
t.printer(t.raiz)