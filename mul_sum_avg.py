#				1) Multiples
#	Part I - Write code that prints all the odd numbers from 1 to 1000. 
#	Use the for loop and don't use a list to do this exercise.
for x in range(1, 1000):
	if x % 2 == 1:
		print(x)

#	Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for y in range(5, 1000000):
	if y % 5 == 0:
		print(y)

# 				2) Sum List
#	Create a program that prints the sum of all the values.
a = [1, 2, 5, 10, 255, 3]
	print sum(a)

#				3) Average List
#	Create a program that prints the average of the values.
a = [1, 2, 5, 10, 255, 3]
	print sum(a)/len(a)