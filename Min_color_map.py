def try_colors(graph, num_color):
   if num_color < 0 :
       return None
   colors = {}


   def neighbor_color(node,color):
       for n in node:
           if color == colors.get(n):
               return False
       return True
   for node,adjacents in graph.items():
       found_color = False

       for color in range(num_color):
           if neighbor_color(adjacents,color):
               found_color = True
               colors[node] = color
               break
       if not found_color:
           return None
   return colors



def find_num_color(graph):
   for num_color in range(len(graph)+1):
       colors = try_colors(graph,num_color)
       if colors : return colors


def create_tree():
    graph = {}
    print("Create Node:")
    print("(0 = leave)")
    while True:
        inp = input("Node name: ")
        if inp == "0": break
        adds = []
        while True:
            branch = input("Node %s is connected to: "%inp)
            if branch == "0":
                graph[inp] = adds
                break
            else: adds.append(branch)
    return graph


graph = create_tree()

print(graph)
print(find_num_color(graph))
