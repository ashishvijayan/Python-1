def sumtree(L):
	'''
	computing the sum of all the 
	numbers in a nested sublists
	'''
	total = 0
	for x in L:
		if not isinstance(x,list):
			total += x
		else:
			total += sumtree(x)
	
	return total
	
L = [1, [2, [3, 4], 5], 6, [100, 8]]       
print(sumtree(L))
