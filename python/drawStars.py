# Part 1
# x = [4, 6, 1, 3, 5, 7, 25]
# def draw_stars(arr):
# 	for val in arr:
# 		str = ""
# 		for count in range(0, val):
# 			str += "*"
# 		print str

# Part 2
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(arr):
	for val in arr:
		str = ""
		if type(val) is int:
			for count in range(0, val):
				str += "*"
		else:
			length = len(val)
			for count in range(0, length):
				str += val[0].lower()
		print str

draw_stars(x)