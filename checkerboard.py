# Write a program that prints a 'checkerboard' pattern to the console.

for i in range(0,8):
	for j in range(0,4):
		print ("* "),
	print "\n"
	if (i % 2 == 0):
		print " ",