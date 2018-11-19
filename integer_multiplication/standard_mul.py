
# single digit multiplication

# convert numbers to lists of single digit integers
def num_list(num):
	num_l = []
	while num>0:
		num_l.append(num%10)
		num=num//10
	num_l.reverse()
	return num_l

# convert lists of single digit integers to number
def list_num(sum_l):
	sum_l.reverse()
	return sum([sum_l[i]*(10**i) for i in range(len(sum_l))])

# convert numbers to lists of single digit integers
def carry_manage(num_l):
	for i in range(len(num_l)-1):
		if num_l[i]>9:
			num_l[i]=num_l[i]-10
			num_l[i+1]=num_l[i+1]+1

	if num_l[-1]>9:
		num_l[-1] = num_l[-1]-10
		num_l.append(1)

	return num_l


# single digit multiplication
def mul_base(n1,n2):

	if n1>9 or n2>9:
		raise ValueError('Single digit multiplication only')

	return n1*n2

# n1, n2 are lists of single digit integers
def mul_std(int1_l,int2_l):

	# check for same length. For now.
	count1 = len(int1_l)
	count2 = len(int2_l)

	if count1!=count2:
		raise ValueError('Please provide numbers of same length')

	intr_result=[]
	for int2_digit in int2_l:
		sub = []
		for int1_digit in int1_l:
			sub.append(mul_base(int1_digit,int2_digit))
		intr_result.append(sub)

	intr_result.reverse()
	for i in range(len(intr_result)):
		intr_result[i].extend([ 0 for _ in range(i)])
		intr_result[i].reverse()
		# print intr_result[i]

	# res_l=[sum([x[i] if i<len(x) else 0 for x in intr_result]) for i in range(len(intr_result[-1]))]

	res_l = []
	for i in range(len(intr_result[-1])):
		res_l.append(sum([x[i] if i<len(x) else 0 for x in intr_result]))

	res_l = carry_manage(res_l)
	res_l.reverse()

	return res_l

def main():
	print 'Shubham'

	#multiply numbers with 2
	num1 = int(input("Enter num1:"))
	num2 = int(input("Enter num2 (Same length):"))

	answer = num1*num2
	print 'Answer=',answer

	num1_l = num_list(num1)
	num2_l = num_list(num2)

	ans_l = mul_std(num1_l,num2_l)
	print 'Answer calculated =', ans_l

	ans = list_num(ans_l)
	print 'Answer calculated =', ans


if __name__ == '__main__':
	main()
