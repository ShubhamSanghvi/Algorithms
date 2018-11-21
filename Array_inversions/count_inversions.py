import sys
import os.path

def count_inversion(array):
	if len(array) == 1:
		return 0,array

	ret1 = count_inversion(array[:len(array)/2])
	ret2 = count_inversion(array[len(array)/2:])

	sorted_arr = []
	count = 0
	j = 0
	k = 0

	for i in range(len(array)):
		if(j<len(ret1[1]) and k<len(ret2[1])):
			if ret1[1][j] < ret2[1][k]:
				sorted_arr.append(ret1[1][j])
				j=j+1
			else:
				sorted_arr.append(ret2[1][k])
				k=k+1
				count=count+len(ret1[1])-j


	if j<len(ret1[1]):
		sorted_arr.extend(ret1[1][j:])

	if k<len(ret2[1]):
		sorted_arr.extend(ret2[1][k:])


	count = count+ret1[0]+ret2[0]

	return count,sorted_arr


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

	inversions = count_inversion(array)

	print "Inversions :",inversions[0]


if __name__ == '__main__':
	main()