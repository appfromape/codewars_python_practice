'''

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

'''


def square_digits(num):
	str_num_list = []
	str_num = str(num)
	for s in str_num:
		str_num_list.append(str(int(s)**2))
	
	return int("".join(str_num_list))

print(square_digits(9119))