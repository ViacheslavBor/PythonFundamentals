# 				1) Integer
# 	If the integer is greater than or equal to 100, print "That's a big number!". 
# 	If the integer is less than 100, print "That's a small number".
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
temp = spI
if isinstance(temp, int):
	print(temp)
	if temp >= 100:
		print("That's a big number!")
	if temp < 100:
	    print("That's a small number")

#				2)String
# If the string is greater than or equal to 50 characters print "Long sentence." 
# If the string is shorter than 50 characters print "Short sentence."
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
temp = sS
if isinstance(temp, str):
	print len(temp)
	if len(temp) >= 50:
		print("Long sentence!")
	if len(temp) < 50:
	    print("Short sentence")

#				3) List
# 	If the length of the list is greater than or equal to 10 print "Big list!" 
# 	If the list has fewer than 10 values print "Short list."
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
x = eL
if isinstance(x, list):
	print len(x)
	if len(x) >= 10:
		print("Big list!")
	if len(x) < 10:
		print("Short list!")