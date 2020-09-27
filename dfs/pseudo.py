# Global or class scope variables
n = number of nodes in the graph
g = adjacency list representing graph
visited = [false, ..., false] # size n

function dfs(at):
	if visited[at]: return
	visited[at] = true

	neighbors = graph[at]
	for next in neighbors:
		dfs(next)

# Start DFS at node zero
start_node = 0
dfs(start_node)