#  # https://olimpiada.ic.unicamp.br/pratique/pj/2017/f3/onibus/

def Find_Distance(lista):
    some = 0
    for n in range(int(len(lista)-1)):
        num = city_[0].get(lista[n]).index(lista[n + 1])
        some += city_[1].get(lista[n])[num]
    return some

def create_tree(num):
   city = {}
   value = {}
   for NODE in range(1,num + 1):
       city[NODE] = []
       value[NODE] = []
   for n in range(num-1):
       inpu = input().split()
       city[int(inpu[0])].append(int(inpu[1]))
       value[int(inpu[0])].append(int(inpu[2]))
       city[int(inpu[1])].append(int(inpu[0]))
       value[int(inpu[1])].append(int(inpu[2]))

   return city,value


def deepness_scan(start, destination, hold= None):
   if destination == start:
      return start
   for PATH in city_[0][start]:
       if PATH != hold:
           hold = start
           do_scan = deepness_scan(PATH, destination, hold)
           if do_scan :
               lista.append(do_scan)
               return hold
           else :
               del city_[0][PATH]

lista = []
inp = input().split(" ")


city_ = create_tree(int(inp[0]))


lista.append(deepness_scan(int(inp[1]), int(inp[2])))

print(lista)
print(Find_Distance(lista))
