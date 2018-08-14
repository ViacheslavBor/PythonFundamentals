# Write a program that takes a list and prints a message for each element in the list, 
# based on that element's data type.

def arrayfunc(arr):
	count = 0
	mysum = 0
	mystr = ""
	for x in range(0, len(arr)):
		if isinstance(arr[x], int) or isinstance(arr[x], float): 
			mysum += arr[x]
		elif isinstance(arr[x], str):
			count = count + 1
			mystr += str(arr[x])
	if count > 0 and mysum > 0 :
		print "The list you entered is of mixed type"
		print "String:", mystr
		print "Sum:", mysum
	elif count > 0  and mysum == 0:
		print "The list you entered is of string type"
		print "String:", mystr
	elif mysum > 0 and count == 0:
		print "The list you entered is of integer type"
		print "Sum:", mysum

arrayfunc(['magical','unicorns'])