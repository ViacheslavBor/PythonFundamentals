#				1) Find and Replace
#	Print the position of the first instance of the word "day". 
#	Then create a new string where the word "day" is replaced with the word "month".
string = "It's thanksgiving day. It's my birthday,too!";
print string.find("day")
print string.replace("day", "month", 1)

# 				2) Min and Max
# 	Print the min and max values.
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# 				3) First and Last
# 	Print the first and last values.
# 	Create a new list containing only the first and last values in the original list.
x = ["hello",2,54,-2,7,12,98,"world"]
print [x[0], x[-1]]

# 				4) New List
# 	Sort your list first. 
# 	Then, split your list in half. 
# 	Push the list created from the first half to position 0 of the list created from the second half. 
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y = sorted(x)
z = y[:5]
newarr = y[5:]
newarr.insert(0,z)
print newarr