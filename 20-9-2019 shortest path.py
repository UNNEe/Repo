import copy

def create_tree():
    graph = {}
    print("0 - cancel")

    while True:
        node = int(input("Insert node: "))
        if node == 0 :
            return graph
        graph[node] = []
        while True:
            try:
                adjacentes,peso = [int(n) for n in input("Node %s [adjacents/weight]:"%node).split(" ")]
                graph[node].append([adjacentes,peso])
                if adjacentes == 0:
                    break
            except :
                break

def shortest(n,soma):
    if soma+n[1] < path_s[1]: # # verify if current path is shorter than the 'ideal' path aka path_s
        return True
    return False

def min_path(origin,destination):
    global some
    if origin == destination:  # # verify if the algorithm reached the destination
        path_s[0] = copy.deepcopy(path)
        path_s[1] = copy.deepcopy(some)
    else:
        for n in city[origin]:
            if n[0] not in path and shortest(n,some):  # # verify if the current path is shorter than the 'ideal' path
                path.append(n[0])
                some += n[1]
                min_path(n[0],destination)  # # recursive
                path.pop()
                some -= n[1]


city = {1:[[2,3],[3,1]],    # # Change the 'city' graph to whatever you want// or use the 'create_tree' to create one
       2:[[1,3],[3,3],[4,5]],  # # eg: {node: [[neighbor,distance],[neighbor,distance]]}
       3:[[1,1],[2,4],[5,5]],  # # node = int number, neighbor = int number, distance = int number
       4:[[2,2],[5,1],[6,3],[7,5]],
       5:[[3,5],[4,1]],
       6:[[4,3],[7,2]],
       7:[[4,5],[6,2]]}
inp = [int(n) for n in input("origin/destination:").split()]
path_s = [[],float("inf")]
path = [inp[0]]
some = 0
min_path(inp[0],inp[1])
print("min path", path_s[0])
print("distance", path_s[1])
