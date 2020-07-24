def aStar(start_node, goal_node):
        
        open_set = set(start_node) 
        closed_set = set()
        g = {} 
        parents = {}
        g[start_node] = 0 
        parents[start_node] = start_node
        
        
        while len(open_set) > 0:
            n = None 

            for v in open_set:
                if n == None or g[v] + h_func(v) < g[n] + h_func(n): # S->A (cost 7) > so S->B  first S-> B (cost 6)
                    n = v
                   
            if n == goal_node or adj_list[n] == None:
                pass
            else:
                for (m, cost) in child_nodes(n):

                    if m not in open_set and m not in closed_set:
                        open_set.add(m) # creating obj, adding to queue S A B, S A C, S A D, ( S B C from before/already in queue )
                        parents[m] = n
                        g[m] = g[n] + cost  # g(n) is cost of S->A from before, + cost of A ->B, or A->C, or A->D
                        
                    else:
                        if g[m] > g[n] + cost:
                            g[m] = g[n] + cost
                            parents[m] = n
                            
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)

            if n == None:
                print('there\'s no path')
                return None

            # path create if it's goal
            if n == goal_node:
                path = []

                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(start_node)

                path.reverse()

                print('path: {}'.format(path))
                return path

            open_set.remove(n)
            closed_set.add(n)

        print('there\'s no path')
        return None


def child_nodes(v):
    if v in adj_list:
        return adj_list[v]
    else:
        return None
def h_func(n):
        h = {
            'S': 7,
            'A': 6,
            'B': 2,
            'C': 1,
            'D': 0   
        }

        return h[n]

adj_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 3)]  
}
aStar('S', 'D')