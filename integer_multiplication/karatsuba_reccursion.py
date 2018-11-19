def mul_karatsuba(num1,num2):

	if num1<10 and num2<10 :
		return num1*num2

	max_length = len(str(num1)) if len(str(num1)) > len(str(num2)) else len(str(num2)) 

	m = max_length//2

	x0 = num1%(10**m)
	x1 = num1//(10**m)

	y0 = num2%(10**m)
	y1 = num2//(10**m)


	z0 = mul_karatsuba(x0,y0)
	z2 = mul_karatsuba(x1,y1)
	z1 = mul_karatsuba(x0+x1,y0+y1)-z0-z2

	result = z2*(10**(2*m)) + z1*(10**m) + z0

	return result


def main():

	# num1 = int(input("Enter num1:"))
	# num2 = int(input("Enter num2 (Same length):"))

	# from the course
	num1 = 3141592653589793238462643383279502884197169399375105820974944592
	num2 = 2718281828459045235360287471352662497757247093699959574966967627

	answer = num1*num2
	print 'Answer\t=',answer

	ans_cal = mul_karatsuba(num1,num2)
	print 'Calculated=', ans_cal


if __name__ == '__main__':
	main()
