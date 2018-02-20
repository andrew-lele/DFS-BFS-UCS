import pandas as pd

def makeGraph(i_file):
	file_to_list = [l.split(' ') for l in i_file.read().split('\n')]
	# print(file_to_list)
	df = pd.DataFrame(file_to_list)
	
	weights = {df[1][i]:{df[2][i]}for i in df}

	# print("len df: " , len(df))
	graph = {}
	# for i in range(len(df)):
		# print(df['0'].loc(i))
		# graph[df[0].loc(i)] = weights[i] 
	graph = {df[0][i]:{df[1][i]:df[2][i]} for i in df}

	# print(graph)


def BFS(graph, start, end):

	from collections import deque
	print("----------BFS---------\n")
	queue = deque([start])
	print('graph: ' , graph)

	#dictionary of previous nodes with the leading node (key - previous, value - node of path taken) 
	prev_nodes = {}
	#list of the nodes for the path taken
	mapping = []

	#loop through nodes in path until queue is empty
	while queue:
		# print('queue: ', queue)
		#grab the current node to inspect for possible paths
		node = queue.popleft()
		# print('node: ', node)

		#check if te node leads anywhere
		if node in graph:

			for neighbor in graph:

				#if explored, ignore it
				if neighbor in graph[node]:
					print('gnode: ' , graph[node], '\t neigh: ', neighbor)
					if neighbor in prev_nodes:
						continue

					prev_nodes[neighbor] = node

					queue.append(neighbor)

					#if the end is found, return the list
					if neighbor == end:
						print("prev node path: " , prev_nodes)
						
						mapping.append(neighbor)

						while prev_nodes[end] != start:
							
							mapping.append(prev_nodes[end])
							end = prev_nodes[end]

						mapping.append(start)
						
						mapping.reverse()

						return (mapping)
		#backtrack if a dead-end is hit
		# if neighbor not in prev_nodes:
			# del mapping[-1]


def DFS(graph, start, end):
	from collections import deque
	print("----------DFS---------\n")

	stack = deque([start])
	prev_nodes = {}

	mapping = []
	
	while stack:

		node = stack.pop()

		if node in graph:

			for neighbor in graph:

				#if explored, ignore it
				if neighbor in graph[node]:

					prev_nodes[neighbor] = [node]
					stack.append(neighbor)
					
					prev_nodes[neighbor] = node

					#if the end is found, return the list
					if neighbor == end:
						mapping.append(neighbor)

						while prev_nodes[end] != start:
							
							mapping.append(prev_nodes[end])
							end = prev_nodes[end]

						mapping.append(start)
						
						mapping.reverse()

						return (mapping)
		#backtrack if a dead-end is hit

	return []

def UCS(graph, start, end):
	import heapq
	queue = []

	#contain the most lit
	heapq.heappush(queue, (0, [startNode]))

	# while queue:
	# 	path = heapq.heappop(queue)
	# 	node = path[1][-1]

	# 	if 

	return []
def main(args):
	import sys

	try:
		i_file = open(sys.argv[1], 'r')
	except:
		print('input_error %s')
		sys.exit(2)

	graph = makeGraph(i_file)
	mapping = []
#delet this 

	graph= {1:{2: 10, 3: 5},
	      2: {4: 10},
	      3: {4: 5},
	      4: {5: 5, 6: 10},
	      5: {7: 5},
	      6: {7: 10},
	      7: {}}
	# graph = {1:{2:34},
	# 			2:{3:192},
	# 			3:{4:43},
	# 			4:{5:137}}

	# graph = [dict([a, int(x)] for a, x in b.items()) for b in graph]
	# for b in graph:
		# print(type(b))
	# print("type: ", sys.argv[4])

	if sys.argv[2] == sys.argv[3]:
		print("Start == End, terminate")
		return

	if sys.argv[4] == "BFS":
		mapping = BFS(graph, int(sys.argv[2]), int(sys.argv[3]) )

	elif sys.argv[4] == "DFS":
		mapping = DFS(graph, int(sys.argv[2]), int(sys.argv[3]) )

	elif sys.argv[4] == "UCS":
		mapping = UCS(graph, int(sys.argv[2]), int(sys.argv[3]) )

	print('\n -----OUTPUT------\n' ,mapping)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

