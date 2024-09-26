import networkx as nx
import matplotlib.pyplot as plt
def findCyclesOfSize2(G):
    check = {}
    edges = list(G.edges())
    n = len(edges)
    arr = []
    for i in range(0,n):
        check[i] = False
    for i in range(0,n-1):
        u1 = edges[i][0]
        v1 = edges[i][1]
        for j in range(i+1,n):
            u2 = edges[j][0]
            v2 = edges[j][1]
            if(u2 == v1 and v2 == u1):
                if(check[i] == False):
                    check[i] = True
                    check[j] = True
                    arr.append([edges[i],edges[j]])
    return arr

G = nx.DiGraph()
G.add_nodes_from(['A','B','C','D'])
G.add_edges_from([('A', 'B'), ('B', 'D'), ('D', 'C'), ('A', 'C'), ('D', 'A'), ('C', 'D'), ('B', 'A')])
v = findCyclesOfSize2(G)
print(v)
nx.draw_networkx(G) # will draw the graph labeling the nodes
# nx.draw(G): will draw the graph without labeling the nodes
plt.show() # to plot the graph that we just drew