import networkx as nx
import matplotlib.pyplot as plt

def findCyclesOfSize3(G):
    check = {}
    edges = list(G.edges())
    n = len(edges)
    arr = []
    for i in range(0,n):
        check[i] = False
    for i in range(0,n-2):
        u1 = edges[i][0]
        v1 = edges[i][1]
        for j in range(i+1,n-1):
            u2 = edges[j][0]
            v2 = edges[j][1]
            if(u2 == v1):
                for k in range(j+1,n):
                    u3 = edges[k][0]
                    v3 = edges[k][1]
                    if(v2 == u3 and v3 == u1):
                        if(check[i] == False):
                            check[i] = True
                            check[j] = True
                            check[k] = True
                            arr.append([edges[i],edges[j],edges[k]])
    return arr

G = nx.DiGraph()
G.add_nodes_from(['A','B','C','D'])
G.add_edges_from([('A', 'B'), ('B', 'D'), ('D', 'C'), ('A', 'C'), ('D', 'A'), ('C', 'D'), ('B', 'A')])
v = findCyclesOfSize3(G)
print(v)
nx.draw_networkx(G, pos = nx.spring_layout(G)) # pos represents the graph layout and nx.spring_layout(G) is a predefined layout in NetworkX 
plt.show()
# spring_layout(), shell_layout(), spiral_layout() are all predefined layouts in NetworkX 