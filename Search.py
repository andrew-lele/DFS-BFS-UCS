import pandas as pd

def makeGraph(i_file):
	file_to_list = [l.split(' ') for l in i_file.read().split('\n')]
	print(file_to_list)
	df = pd.DataFrame(file_to_list)
	# print(df)
	# graph = {i:df[i] for i in df.columns}
	graph = {df[k][0]:df[k][1] for k in df.columns}

	# k:list(df[k].unique()) for k in df.columns
	print(graph)


def BFS(start, end, graph):
	print("----------BFS---------\n")


def main(args):
	import sys

	try:
		i_file = open(sys.argv[1], 'r')
	except:
		print('input_error %s')
		sys.exit(2)

	makeGraph(i_file)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
