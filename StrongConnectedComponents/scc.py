import sys
import os
from collections import defaultdict
current_time = 0
current_leader = 0
node_times = []
node_leader = defaultdict(list)


def DFS(node,g_dict,mode):
	global current_time,node_times
	global curr_leader,node_leader
	# mark the node as checked
	g_dict[node][0] = 1

	for connected_node in g_dict[node][1:]:
		# if the connected node is not yet checked
		if not g_dict[connected_node][0]:
			# call dfs on it
			DFS(connected_node,g_dict,mode)

	# g_dict[node].append(current_time)
	if mode:
		node_times.append((current_time,node))
		current_time = current_time +1
	else:
		node_leader[curr_leader].append(node)

def cal_scc(g_in):
	global node_times
	global curr_leader,node_leader

	# for node in node_times reverse ordered
	for (time,node) in sorted(node_times,reverse=True):
		if not g_in[node][0]:
			g_in[node][0] = 1
			curr_leader = node
			for connected_node in g_in[node][1:]:
				if not g_in[connected_node][0]:
					DFS(connected_node,g_in,0)

	# print "Node leders"	
	scc_list = [ 0 for _ in range(5)]
	for key,value in node_leader.iteritems():
		# print key,">",value
		if len(value)+1 > min(scc_list):
			index = scc_list.index(min(scc_list))
			scc_list[index] = len(value)+1

	print "SCC sizes:"
	print sorted(scc_list,reverse=True)




def cal_time(rev_g):
	global current_time,node_times

 	# for node,edges in rev_g.iteritems():
 	for node in rev_g.keys():
 		# if the current node is not yet visited
 		if not rev_g[node][0]:
 			# mark the node as checked
 			rev_g[node][0] = 1
 			# loop over all the connected nodes
 			for connected_node in rev_g[node][1:]:
 				# if the connected node is not yet checked
 				if not rev_g[connected_node][0]:
 					# call dfs on it
	 				DFS(connected_node,rev_g,1)

			# rev_g[node].append(current_time)
			node_times.append((current_time,node))
			current_time = current_time + 1

	# print node_times
	# print sorted(node_times,reverse=True)


def main():
	# print "Hello World!"
	
	if len(sys.argv) < 2:
		print "Please provide input file!"
		return

	if not os.path.isfile(sys.argv[1]):
		print "File does not exist:",sys.argv[1]
		return

	print "Using file:",sys.argv[1]

	file_in_use = open(sys.argv[1],'r')

	graph = defaultdict(lambda:[0])
	rev_graph = defaultdict(lambda:[0])

	for line in file_in_use:
		pair = map(int,line.split())
		graph[pair[0]].append(pair[1])
		rev_graph[pair[1]].append(pair[0])

	# print "# printing graph\n"

	# for key,value in graph.iteritems():
		# print key,">",value

	# print "# printing reverse graph\n"

	# for key,value in rev_graph.iteritems():
		# print key,">",value

	sys.setrecursionlimit(800000)
	
	cal_time(rev_graph)
	cal_scc(graph)



if __name__ == '__main__':
	main()