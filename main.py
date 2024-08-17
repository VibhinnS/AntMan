from algorithm import AntColonyOptimization
from generate_graph import SupplyChainGraph
import networkx as nx
import matplotlib.pyplot as plt


supply_chain_graph = SupplyChainGraph.generate_supply_chain_graph()

SupplyChainGraph.draw_graph(supply_chain_graph)

aco = AntColonyOptimization(supply_chain_graph, n_ants=10, n_iterations=50, alpha=1, beta=2, evaporation_rate=0.2)

best_path, best_distance = aco.run()

print("Best Path:", best_path)
print("Best Distance:", best_distance)

def visualize_best_path(G, best_path):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10)
    path_edges = [(best_path[i], best_path[i+1]) for i in range(len(best_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4, edge_color='r')
    plt.show()

visualize_best_path(supply_chain_graph, best_path)
