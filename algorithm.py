import random

class AntColonyOptimization:
    def __init__(self, G, n_ants=10, n_iterations=100, alpha=1.0, beta=2.0, evaporation_rate=0.5, pheromone_constant=100):
        self.G = G
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha  
        self.beta = beta  
        self.evaporation_rate = evaporation_rate
        self.pheromone_constant = pheromone_constant

        self.pheromones = {}
        for edge in self.G.edges:
            u,v = edge
            self.pheromones[(u,v)] = 1.0
            self.pheromones[(v,u)] = 1.0

    def _initialize_ants(self):
        """Initialize ants at random supplier nodes"""
        suppliers = [node for node, attr in self.G.nodes(data=True) if attr['type'] == 'supplier']
        ants = []
        for _ in range(self.n_ants):
            start_node = random.choice(suppliers)
            ants.append({'current_node': start_node, 'visited': [start_node], 'distance': 0})
        return ants

    def _choose_next_node(self, ant):
        """Choose the next node based on pheromone and distance"""
        current_node = ant['current_node']
        neighbors = list(self.G.neighbors(current_node))
        probabilities = []

        for neighbor in neighbors:
            if neighbor not in ant['visited']:
                edge = (current_node, neighbor)
                pheromone = self.pheromones[edge]
                distance = self.G.edges[edge]['distance']
                prob = (pheromone ** self.alpha) * ((1.0 / distance) ** self.beta)
                probabilities.append(prob)
            else:
                probabilities.append(0)

        total_prob = sum(probabilities)
        if total_prob == 0:
            return None
        probabilities = [p / total_prob for p in probabilities]
        return random.choices(neighbors, weights=probabilities)[0]

    def _update_pheromones(self, all_ants):
        """Update pheromone levels based on ants' paths"""
        for edge in self.pheromones:
            self.pheromones[edge] *= (1 - self.evaporation_rate)  

        for ant in all_ants:
            total_distance = ant['distance']
            for i in range(len(ant['visited']) - 1):
                edge = (ant['visited'][i], ant['visited'][i+1])
                self.pheromones[edge] += self.pheromone_constant / total_distance

    def run(self):
        """Run the ACO algorithm"""
        best_path = None
        best_distance = float('inf')

        for iteration in range(self.n_iterations):
            ants = self._initialize_ants()
            for ant in ants:
                while True:
                    next_node = self._choose_next_node(ant)
                    if not next_node:
                        break
                    ant['visited'].append(next_node)
                    ant['distance'] += self.G.edges[(ant['current_node'], next_node)]['distance']
                    ant['current_node'] = next_node

                if ant['distance'] < best_distance:
                    best_path = ant['visited']
                    best_distance = ant['distance']

            self._update_pheromones(ants)
            print(f"Iteration {iteration + 1}, Best Distance: {best_distance}")

        return best_path, best_distance
