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
   for num_color in range(len(graph)):
       colors = try_colors(graph,num_color)
       if colors : return colors

graph = {"a":["b","c"],
        "b":["a","c","d","g"],
        "c":["a","b","d","e","f"],
        "d":["c","b","e","g"],
        "e":["d","c","f","g"],
        "f":["c","e","g","h"],
        "g":["b","d","e","f","h"],
        "h":["f","g"]}

print(find_num_color(graph))