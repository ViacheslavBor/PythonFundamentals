# 					1) Odd/Even:
# Have your program print the number of that iteration and specify whether it's an odd or even number.
for x in range(1, 100):
	if x % 2 == 1:
 		print "Number is", x, "This is an odd number" 
 	else:
 		print "Number is", x,"This is an even number"

# 					2) Multiply:
# Create a function called 'multiply' that iterates through each value in a list
# and returns a list where each value has been multiplied by 5.
a = [1,2,3,4,5]
b = 5
def multiply(a, b):
	for i in range(0, len(a)):
		a[i] *= b
	return a
print multiply(a, b)

# 					3) Hacker Challenge:
def layered_multiples(arr):
	y =[]
	for i in arr:
		a = []
		for j in range(0,i):
			a.append(1)
		y.append(a)
	return y
x = layered_multiples(multiply([2,4,5], 3))
print x
