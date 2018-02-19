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

	from queue import PriorityQueue

	print("----------BFS---------\n")
	queue = [[start]]
	print('graph: ' , graph)

	mapping = []

	while queue:
		print('queue: ', queue)
		node = queue.pop(0)
		# print('node: ', type(node), node,  '\tmapping: ', mapping)
		if node[-1] not in mapping:
			# mapping.append(node)


		# if int(node) == int(end):
			# return mapping

		# neighbors = graph[int(node)]
###
		# 	for neighbor in graph[int(node[-1])]:
		# 		print("here's papa: ", neighbor)
		# 		paths = list(node)
		# 		if neighbor not in mapping:
		# 			queue.append(neighbor)

		# 	mapping.append(node[-1])
		# print("MAP: \t", mapping)

			for neighbor in graph.items():
				print("here's papa: ", neighbor)
				paths = list(node)
				if neighbor[2] not in mapping:
					queue.append(neighbor[1])

			mapping.append(node[-1])
		# print("MAP: \t", mapping)
#############################
	# print('graph: ' , type(graph[1][2]))
	# explored = []
 #    # keep track of all the paths to be checked
	# queue = [[start]]
 
	# # return path if start is goal
	# if start == end:
	# 	return "That was easy! Start = goal"
 
 #    # keeps looping until all possible paths have been checked
	# while queue:
	# 	# pop the first path from the queue
	# 	path = queue.pop(0)
 #        # get the last node from the path
	# 	node = path[-1]
	# 	print("node: ", type(node))
	# 	if node not in explored:
	# 		print("node explored: ", node)
	# 		neighbours = graph[int(node)]
 #            # go through all neighbour nodes, construct a new path and
 #            # push it into the queue
	# 		for neighbour in neighbours:
	# 			new_path = list(path)
	# 			new_path.append(neighbour)
	# 			queue.append(new_path)
 #                # return path if neighbour is goal
	# 			if int(neighbour) == end:
	# 				print("done: " , new_path)
	# 				return new_path
 
 #            # mark node as explored
	# 		explored.append(node)
	# print('rip: ', explored )
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

	print('\n -----OUTPUT------\n' ,mapping)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

