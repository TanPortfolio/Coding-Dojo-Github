import random 
def coinToss():
	headCount = 0;
	tailCount = 0;
	tossCount = 0;
	for x in range(1, 5001): 
		toss = round(random.random())
		if toss == 0:
			headCount += 1
			tossCount += 1
			print "Attempt #", tossCount , ": Throwing a coin... It's a head! ... Got " , headCount , "head(s) so far and " , tailCount , "tail(s) so far"
		else: 
			tailCount += 1
			tossCount += 1
			print "Attempt #", tossCount , ": Throwing a coin... It's a tail! ... Got " , headCount , "head(s) so far and " , tailCount , "tail(s) so far"
coinToss()