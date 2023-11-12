import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10), dpi=80, facecolor='#161616')
plt.axes().set_facecolor('#1F1F1F')

G = nx.MultiDiGraph()
numArr = [(1, 2), (1, 3)]

# {{x, y}, {x, z}} -> {{x, y}, {x, w}, {y, w}, {z, w}}

iter_i = 0
max_iter = 3
w = 4

while True:
    if iter_i == max_iter: break
    for i in range(len(numArr)):
        x, y = numArr[i]
        z = numArr[i + 1][1]
        numArr.pop(1)
        numArr.append((x, w))
        numArr.append((y, w))
        numArr.append((z, w))
        w += 1
    iter_i += 1
    print(iter_i)

G.add_edges_from(numArr)
pos = nx.planar_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=50, node_color='#bf00ff')
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='cyan')

plt.show()