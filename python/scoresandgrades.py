def scoreGrade():
	for count in range(0,11):
		data = raw_input("What is your score? ")
		try:
			score = int(data)
		except ValueError:
			print "Please insert a valid integer"
		else: #What is this else a complement to?  As there is no if, do you need to say 'else'?  Just curious :)
			if 60 <= score <= 69:
				print "Scores:", score , "; Your grade is D"
			elif 70 <= score <= 79:
				print "Scores:", score , "; Your grade is C"
			elif 80 <= score <= 89:
				print "Scores:", score , "; Your grade is B"
			elif 90 <= score <= 100: 
				print "Scores:", score , "; Your grade is A"
			elif score > 100: 
				print "You're an overachiever!"
			else: 
				print "You have failed"
	print "End of program. Bye!"
scoreGrade()
