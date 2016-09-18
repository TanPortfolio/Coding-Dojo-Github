Part 1
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(arr):
	for val in arr:
		str = ""
		for count in range(0, val):
			str += "*"
		print str