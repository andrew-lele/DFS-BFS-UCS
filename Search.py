# import sys

#open the file with the graph, read it in as a dictionary, then return the dictionary nammed "graph"
def makeGraph(i_file_name):

	#make sure the file exists, and open it if it is. 
	try:
		i_file = open(i_file_name, 'r')
		
		graph = {}
		#loop through each line in the file
		for row in i_file:
			#split up the spacees '[1 2 3] -> [1,2,3]
			split_by_space = row.split()

			#assume that the start is pos 0, end is pos 1, and distance/weight is pos 3
			start = int(split_by_space[0])
			end = int(split_by_space[1])
			weight = int(split_by_space[2])


			if start not in graph:
				graph[start] = {}

			graph[start][end] = weight

	#if the file does not exist, throw an error
	except:
		print('input_error %s')
		sys.exit(2)

	# print(graph)
	return graph

def BFS(graph, start, end):

	from collections import deque
	#create a datastructure to seach through the nodes
	queue = deque([start])

	#dictionary of previous nodes with the leading node (key - previous, value - node of path taken) 
	prev_nodes = {}
	#list of the nodes for the path taken
	mapping = []
	#loop through nodes in path until queue is empty
	while queue:

		#grab the current node to inspect for possible paths
		node = queue.popleft()

		#check if te node leads anywhere
		if node in graph:

			for neighbor in graph[node]:
				#if explored, ignore it

				# if neighbor in graph[node]: #or graph[node][0] == end:

				if neighbor in prev_nodes:
					continue

				#if the end is found, return the list
				elif neighbor == end:

					prev_nodes[neighbor] = node
					mapping.append(neighbor)

					while prev_nodes[end] != start:
						mapping.append(prev_nodes[end])
						end = prev_nodes[end]

					mapping.append(start)
					
					mapping.reverse()
					return (mapping)
				else:
					prev_nodes[neighbor] = node
					queue.append(neighbor)

	return []


def DFS(graph, start, end):
	from collections import deque

	#initalize the stack stat structure for DFS
	stack = deque([start])
	#holds previous paths taken
	prev_nodes = {}
	#the path from start to end
	mapping = []
	
	#loop trhough the stack to check for all paths, expand furthest node first (DFS) 
	while stack:

		#grab current node to see possible paths
		node = stack.pop()

		if node in graph:

			for neighbor in graph[node]:
				#if explored, ignore it

				# if neighbor in graph[node]: #or graph[node][0] == end:

				if neighbor in prev_nodes:
					continue

				#if the end is found, return the list
				elif neighbor == end:

					prev_nodes[neighbor] = node
					mapping.append(neighbor)

					while prev_nodes[end] != start:
						mapping.append(prev_nodes[end])
						end = prev_nodes[end]

					mapping.append(start)
					
					mapping.reverse()
					return (mapping)
				else:
					prev_nodes[neighbor] = node
					stack.append(neighbor)

		# if node in graph:

		# 	for neighbor in graph:

		# 		#if explored, ignore it
		# 		if neighbor in graph[node]:

		# 			prev_nodes[neighbor] = [node]
		# 			stack.append(neighbor)
					
		# 			prev_nodes[neighbor] = node

		# 			#if the end is found, return the list
		# 			if neighbor == end:
		# 				mapping.append(neighbor)

		# 				while prev_nodes[end] != start:
							
		# 					mapping.append(prev_nodes[end])
		# 					end = prev_nodes[end]

		# 				mapping.append(start)
						
		# 				mapping.reverse()

		# 				return (mapping)
		#backtrack if a dead-end is hit

	return []

def UCS(graph, start, end):
	import heapq as hq
	
	queue = []
	hq.heappush(queue, (0, [start]))
	mapping = []
	prev_nodes = {}


	while queue:
		node = hq.heappop(queue)
		curr = node[1][-1]

		# if node in prev_nodes:
			# continue
    
		if end in node[1]:
			prev_nodes[neighbor] = node
			mapping.append(neighbor)

			while prev_nodes[end] != start:
				mapping.append(prev_nodes[end])
				end = prev_nodes[end]

			mapping.append(start)
			
			mapping.reverse()
			return (mapping)
        
		if curr in graph:
			cost = node[0]

			for neighbor in graph[curr]:
				hold = list(node[1])
				hold.append(neighbor)
				hq.heappush(queue, ((cost + graph[curr][neighbor]), hold ) )


	#contain the most lit
	# heapq.heappush(queue, (0, [start]))
	# while queue:
	# 	path = heapq.heappop(queue)
	# 	node = path[1][-1]

	# 	if 

	return []
def main(args):
	i_file_name = str(sys.argv[1])

	graph = makeGraph(str( i_file_name) )
	mapping = []

	if sys.argv[2] == sys.argv[3]:
		print("Start == End, terminate")
		return

	if sys.argv[4] == "BFS":
		mapping = BFS(graph, int(sys.argv[2]), int(sys.argv[3]) )

	elif sys.argv[4] == "DFS":
		mapping = DFS(graph, int(sys.argv[2]), int(sys.argv[3]) )

	elif sys.argv[4] == "UCS":
		mapping = UCS(graph, int(sys.argv[2]), int(sys.argv[3]) )

	print(mapping)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])


