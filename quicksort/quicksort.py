import sys
import os

comparision_cnt = [0,0,0]

def part_array(in_list,method):

	# print "in_list",in_list

	# change according to the method
	if method == 0:
		index = 0
	elif method == 1:
		index = -1
	else:
		center = (len(in_list)-1)/2

		if in_list[0] > in_list[center]:
			if in_list[center] > in_list[-1]:
				index = center
			elif in_list[0] > in_list[-1]:
				index = -1
			else:
				index = 0
		else:
			if in_list[0] > in_list[-1]:
				index = 0
			elif in_list[center] > in_list[-1]:
				index = -1
			else:
				index = center

	# bring the chosen pivot to first location
	temp = in_list[0]
	in_list[0] = in_list[index]
	in_list[index] = temp

	i = 0
	for j in range(len(in_list)-1):
		if in_list[j+1]<in_list[0]:
			if not i == j:
				temp = in_list[i+1]
				in_list[i+1] = in_list[j+1]
				in_list[j+1] = temp
			i=i+1

	temp = in_list[i]
	in_list[i] = in_list[0]
	in_list[0] = temp

	return (in_list,i)


def quicksort(to_list,method):
	global comparision_cnt
	if len(to_list) < 2:
		return to_list

	(part_list,p) = part_array(to_list,method)

	# print "part_list",part_list

	part_list[:p] = quicksort(part_list[:p],method)
	part_list[p+1:] = quicksort(part_list[p+1:],method)
	comparision_cnt[method] = comparision_cnt[method] + len(part_list) - 1

	return part_list


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
	array = []
	for line in file:
		array.append(int(line))

	# print "Array :\n", array

	for car in range(3):
		ar1 = quicksort(array[:],car)

	# print ar1
	print comparision_cnt

if __name__ == '__main__':
	main()
