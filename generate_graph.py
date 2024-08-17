import random
import networkx as nx
import matplotlib.pyplot as plt


class SupplyChainGraph:
    def generate_supply_chain_graph(num_suppliers=3, num_warehouses=3, num_distribution_centers=3):
        G = nx.Graph()
        
        # Add suppliers
        for i in range(1, num_suppliers + 1):
            G.add_node(f'Supplier {i}', type='supplier')
        
        # Add warehouses
        for i in range(1, num_warehouses + 1):
            G.add_node(f'Warehouse {i}', type='warehouse')
        
        # Add distribution centers
        for i in range(1, num_distribution_centers + 1):
            G.add_node(f'Distribution {i}', type='distribution')

        nodes = list(G.nodes)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                distance = random.randint(10, 100)  
                G.add_edge(nodes[i], nodes[j], distance=distance)
        
        return G

    supply_chain_graph = generate_supply_chain_graph()

    def draw_graph(G):
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'distance')
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

