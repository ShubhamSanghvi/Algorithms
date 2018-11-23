import sys
import os
import random
import copy 

def get_edge_matrix(vertex_matrix):
	edge_matrix = {}
	edge_num = 0

	for vertex,connection_list in vertex_matrix.iteritems():
		for node in connection_list:
				if not (node,vertex) in edge_matrix.values():
					if not node == vertex:
						edge_matrix[edge_num] = (vertex,node)
						edge_num = edge_num + 1

	return edge_matrix


def contrap_one(vertex_matrix):

	edge_matrix = get_edge_matrix(vertex_matrix)
	# print edge_matrix

	count =0
	for key,value in vertex_matrix.iteritems():
		count = count + len(value)

	# print "total count:",count

	# print random.choice(edge_matrix.keys())

	contrap = edge_matrix[random.choice(edge_matrix.keys())]

	# print "-----------------"
	# print "contrap", contrap
	# print "-----------------"
	# print "connections 1:",vertex_matrix[contrap[0]]
	# print "connections 2:",vertex_matrix[contrap[1]]

	vertex_matrix[contrap[0]].extend(vertex_matrix[contrap[1]])
	vertex_matrix[contrap[0]].remove(contrap[0])
	vertex_matrix[contrap[0]].remove(contrap[1])


	# print vertex_matrix[contrap[0]]
	# print vertex_matrix[contrap[1]]
	del vertex_matrix[contrap[1]]

	del edge_matrix[random.choice(edge_matrix.keys())]


	for key,value_l in vertex_matrix.iteritems():
		vertex_matrix[key] = [contrap[0] if x==contrap[1] else x for x in value_l]
		# print "value1",[contrap[0] if x==contrap[1] else x for x in value_l]


	# print "keys remaining:",sorted(vertex_matrix.keys())
	# print "new_matrix", vertex_matrix

	return vertex_matrix

def karger_ki_karigari(graph_dict):

	in_put = graph_dict

	while len(graph_dict) > 2:
		graph_dict = contrap_one(graph_dict)

	edge_matrix = get_edge_matrix(graph_dict)
	# print edge_matrix

	# print "Count of connection :", len(edge_matrix)

	return len(edge_matrix)


def main():
	print "hello world"

	if len(sys.argv) < 2:
		print "Please provide file containing array as argument"
		return

	if(os.path.isfile(sys.argv[1])):
		print "Using file :", sys.argv[1]
	else:
		print "Invalid File name! File does not exist"
		return

	file = open(sys.argv[1],'r')
	# array = []
	map_of_things = { }
	for line in file:
		 map_of_things[int(line.split()[0])]=map(int, line.split()[1:])

	# print sorted(map_of_things.keys())
	# print sorted(map_of_things.items())
	# print array

	min_count = len(map_of_things)

	for i in range(len(map_of_things)):
		temp = copy.deepcopy(map_of_things)
		cur_count = karger_ki_karigari(temp)
		print cur_count
		if cur_count < min_count:
			min_count = cur_count


	print "-------------------"
	print "min_count:",min_count



if __name__ == '__main__':
	main()
