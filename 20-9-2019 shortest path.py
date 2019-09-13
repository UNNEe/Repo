def find_path(origin,destination):
   if origin == destination :
        temp = []
        for h in paths:
            if all(elem in path for elem in h):
                return None
        for n in path:
           temp.append(n)
        paths.append(temp)
        print(path)
        return path
   for adjacents in city[origin]:
        if adjacents not in path:
            path.append(adjacents)
            find_path(adjacents,destination)
            path.pop()
def Find_Distance(lista):
    some = 0
    for n in range(len(lista)-1):
        num = city.get(lista[n]).index(lista[n + 1])
        some += value.get(lista[n])[num]
    return some
def min_path(PATH):
    min_path_temp = [1000000000,0]
    for n in PATH:
        temp = Find_Distance(n)
        if temp < min_path_temp[0]:
            min_path_temp[0],min_path_temp[1]= temp,n
    return min_path_temp
paths = []
path = [1]



city = {1:[2,3],
       2:[1,3,4],
       3:[1,2,5],
       4:[2,5,6,7],
       5:[3,4],
       6:[4,7],
       7:[4,6]}
value = {1:[3,1],
       2:[3,4,2],
       3:[1,4,5],
       4:[2,1,3,5],
       5:[5,1],
       6:[3,2],
       7:[5,2]}

find_path(1,7)
print(paths)
print(min_path(paths))