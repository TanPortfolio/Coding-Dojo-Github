a = [2,4,10,16] 
b = []
def multiply(a,integer):
	for i in a:
		b.append(i*integer)
newlist = multiply(a,5)
print b