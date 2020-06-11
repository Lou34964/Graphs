
def earliest_ancestor(ancestors, starting_node):
    
    #build graph
    graph = {}
    for p, c in ancestors:
        if c not in graph:
            graph[c] = []
        graph[c].append(p)

    s = []
    s.append(starting_node)
    visited = []
    
    #get ancestors
    while len(s):
        v = s.pop()
        if v not in visited:            
            visited.append(v)
            if v not in graph:
                if len(visited) > 1:
                    return v
                else:
                    return -1

            s.append(min(graph[v]))

    return visited.pop()