# Correct the tree structure
import networkx as nx
import matplotlib.pyplot as plt
edges = [
    ('Root', 'LeftHalf'),
    ('Root', 'RightHalf'),
    ('LeftHalf', 'LL'),
    ('LeftHalf', 'LR'),
    ('RightHalf', 'RL'),
    ('RightHalf', 'RR'),
    ('LL', 'LLL'),
    ('LL', 'LLR'),
    ('LR', 'LRL'),
    ('LR', 'LRR'),
    ('RL', 'RLL'),
    ('RL', 'RLR'),
    ('RR', 'RRL'),
    ('RR', 'RRR')
]

# Create a new directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from(edges)

# Plot the graph
plt.figure(figsize=(10, 8))
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True, arrows=False, node_size=1500, node_color='skyblue', font_size=10)
plt.show()
