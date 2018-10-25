# By: Marcos Gil

def collectData(): # Function for getting the integers from the user and adding them to a list that will be returned for use in other functions
	
	userList = []
	
	print("You will now be prompted to enter as many integers as you'd like to use for the mean/median/trimmed mean calculations later. ")
	print("If you enter a negative number you will not be able to add more numbers. ")
	print()
	
	while True:
		try:
			userInput = int(input('What integer would you like to enter? '))
	
			while userInput >= 0: # A while loop that will continously ask the user for more integers until you enter one that is less than 0
				userList.append(userInput)
				userInput = int(input('What integer would you like to enter? '))
			
			break
		
		except:
			
			print('Sorry you can only input integers. ') 
			continue
	
	return userList
	
def sortList(userList): # Function for sorting the list the user inputed
	
	userList.sort()
	return userList
		

def mean(list): # Function for calculating the mean which takes the list returned from collectData as a parameter
	
	if len(list) == 0:
		return 'A negative number was entered first so there are no integers in the list to calculate the mean with. '
	
	x = 0
	for item in list:
		x = x + item
	
	return float(x/len(list))



def trimmedMean(list): # Function for calculating the trimmed mean(popping off first and last index of list) which takes the list returned from collectData as a parameter
	
	if len(list) <= 2:
		return 'You either entered a negative number as the very first number, or you did not enter at least 3 positive integers; therefore the trimmed mean cannot be calculated. '
	
	list.pop(0)
	list.pop()
	
	x = 0
	for item in list:
		x = x + item
	
	return float(x/len(list))


def median(list): # Function for calculating the median which takes the list returned from collectData as a parameter
	
	if len(list) == 0:
		return 'A negative number was entered first so there are no integers in the list to calculate the median with. '

	a = len(list)

	if a % 2 == 0:
		b = list[len(list)//2]
		c = list[(len(list)//2)-1]
		d = (b + c) / 2
		return float(d)

	if a % 2 > 0:
		return float(list[len(list)//2])

def main(): # Main function which will be used to initialize the program and call on the functions I created above to do the necessary calculations then output the results to the user
	
	userList = collectData()
	print("The list being used for these calculations: ", userList)
	userList = sortList(userList)
	print("List after being sorted: ", userList)
	print()
	print("The mean of your list is: ", mean(userList))
	print()
	print("The trimmed mean of your list is: ", trimmedMean(userList))
	print()
	print("The median of your list is: ", median(userList))