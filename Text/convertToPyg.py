from sys import exit

while True:
		userInput = raw_input("Enter a word: ")
		
		# make sure user enters something    
		if len(userInput) > len("") and userInput.isalpha():
		
				# convert all to lowercase letters
				validatedInput = userInput.lower()
				pygResult = validatedInput + validatedInput[0] + "ay"
    
				# take everything after the first character in pygResult
				pygResult = pygResult[1:len(pygResult)]
				
				print userInput + "in pyglatin is: " + pygResult + "."
						
				quit = raw_input("\nEnter 'quit' to exit the program or enter any key to continue: ")
						
				if quit == "quit":
						exit(0)

		else:
				print "Error. Please try again."
