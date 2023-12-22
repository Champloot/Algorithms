def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
	if cost < lowest_cost and node not in processed:
	    lowest_cost = cost
	    lowest_cost_node = node
    return lowest_cost_node

graph = {'start': {'A': 3, 'B': 6, 'C': 1},
	 'A': {'D': 4, 'F': 2},
	 'B': {'D': 2, 'finish': 5},
         'C': {'E': 6},
	 'D': {'F': 1},
	 'F': {'finish':2},
	 'E': {'finish': 3},
	 'finish': {}}
				
costs = {'A': 3, 
	 'B': 6, 
	 'C': 1, 
	 'D': float("inf"), 
	 'E': float("inf"), 
	 'F': float("inf"), 
	 'finish': float("inf")}

parents = {'A': 'start', 
	   'B': 'start', 
	   'C': 'start', 
	   'D': None, 
	   'E': None, 
           'F': None, 
	   'finish': None}

processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
	if costs[n] > new_cost:
	    costs[n] = new_cost
	    parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print('Shortest distance to finish: ' ,costs['finish'])
