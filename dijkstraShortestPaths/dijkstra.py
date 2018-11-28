import sys
import os
from collections import defaultdict
explored=[] 
shortest_path=[] 

def dijkstra(in_graph,node):
	global explored,shortest_path
	explored.append(node)

	while len(explored) != len(in_graph):
		greedy_lst = []
		for node_x in explored:
			for (conn_node,edge_weight) in in_graph[node_x]:
				if conn_node not in explored:
					greedy_lst.append((shortest_path[node_x]+edge_weight,conn_node))
		if(len(greedy_lst)):
			(score,node_moved) = min(greedy_lst)
			shortest_path[node_moved] = score
		else:
			print "ERROR! no paths"
		explored.append(node_moved)

	print "Done!"
	# print shortest_path


def main():
	print "Hello World"
	global explored,shortest_path

	if len(sys.argv) < 2:
		print "Please provide input file!"
		return

	if not os.path.isfile(sys.argv[1]):
		print "File does not exist:",sys.argv[1]
		return

	print "Using file:",sys.argv[1]

	file_in_use = open(sys.argv[1],'r')

	graph = defaultdict(list)
	for line in file_in_use:
		# print line.split()
		for edge in line.split()[1:]:
			graph[int(line.split()[0])].append(tuple(map(int,edge.split(','))))

	# for key,value in graph.iteritems():
	# 	print key,'>',value

	# initialize for X and U-X
	# explored.extend([0 for _ in range(len(graph))])
	shortest_path.extend([0 for _ in range(len(graph)+1)])

	dijkstra(graph,1)

	print "Answer for the assignment:"

	for index in (7,37,59,82,99,115,133,165,188,197):
		print shortest_path[index],




if __name__ == '__main__':
	main()
