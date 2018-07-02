
# #### Quiz While Loop 1
# # 3.13.5
# # Let's learn a little bit of Data Analysis and how we can use
# # loops and lists to create, aggregate, and summarize data

# # For the part 1, we'll learn a basic way of creating data using
# # Python's random number generator.

# # To create a random integer from 0 to 10, we first import the 
# # "random" module

# import random

# # We then print a random integer using the random.randint(start, end) function
# print "Random number generated: " + str(random.randint(0,10))

# # Remember that if we want to concatenate a string and a number, we need to convert the 
# # integer into a string using the str() function

# # We now want to create a list filled with random numbers. The list should be 
# # of length 20

# random_list = []
# list_length = 20

# # Write code here and use a while loop to populate this list of random integers. A crucial
# # function that will help you is to use the append() method to add elements to a list.

# def listGen():
# 	while len(random_list) < list_length:
# 		random_list.append(random.randint(0,10))
# 	return random_list

# listGen()

# # When we print this list, we should get a list of random integers such as:
# # [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
# print random_list




# ######## Quiz While Loop 2
# # 3.13.6
# # Now, we want to ask ourselves the question: How many occurrences of 
# # the number 9 appear in our randomly made list?
# # 
# # For example, if we have a list: [2,8,9,9,4,5,9], we want to figure out
# # how to loop through the list and count the number of occurrences of the
# # number 9. In the example list above, the number 9 occurs three times.

# import random

# # 1. Create random list of integers using while loop
# random_list = []
# list_length = 20

# while len(random_list) < list_length:
#   random_list.append(random.randint(0,10))
    
# # Write code here to loop through the list and count all occurrences
# # of the number 9. Note that `if` statements and `while` loops will help you solve
# # this problem.

# index = 0
# count = 0

# while index < len(random_list):
#   if random_list[index] == 9:
#     count = count + 1
#   index = index + 1

# # Test: If the `while` loop we wrote works, we should manually count
# # how many times the number 9 is present in the list.
# print random_list
# print count


# ##### While Loop 3
# # 3.13.7
# # Great! We now want to create a new list that contains the counts
# # of all occurrances of every number seen in the randomly generated 
# # list. That means we want counts of all occurrences of all numbers
# # from 0 through 10 in our randomly generated list.

# # Let's store our counts in a list of length 11 
# # with zeros filled in.

# # We can multiply a list construct to create a list with the same
# # elements n number of times.
# count_list = [0] * 11

# # Check that we have a list of length 11 with all 0 elements
# print count_list

# # We use this list to store our count of numbers 0 to 10 - take note 
# # that total numbers 0 to 10 is 11. We can use the index number of
# # each element to refer to the count of our target
# # number. Our target number is actually the index of the list.
# # For example, assume count_list looks like this:

# count_list = [1,2,3,2,2,1,1,2,3,1,2]

# # Let's print out the occurrences for the numbers 0, 4, 5, and 6
# print count_list[0]
# print count_list[4]
# print count_list[5]
# print count_list[6]

# # Therefore, for our output, we want a count_list that looks like:
# # [1,2,3,2,2,1,1,2,3,1,2]

# # Here's our code that we coded before

# import random

# # Create random list of integers using while loop --------------------
# random_list = []
# list_length = 20

# while len(random_list) < list_length:
#   random_list.append(random.randint(0,10))
# # --------------------------------------------------------------------

# # Initialize count_list for every integer between 0 and 10. 
# # A number will correspond to an index of this count_list
# # Therefore if we see that there are 3 occurrences of the number 4, 
# # we assign count_list[4] = 3, if there are 5 occurrences of the 
# # number 6, we assign count_list[6] = 5

# count_list = [0] * 11
# index = 0
# count = 0

# # Write code here to loop through every number in random_list and
# # update count_list appropriately

# while index < len(random_list):
# 	number = random_list[index]
#  	count_list[number] = count_list[number] + 1
#   	index = index + 1
	

# # Check the list we created
# print count_list
# # If we coded everything correctly, the sum of all of the numbers 
# # in count_list should be 20
# print sum(count_list)



# #########
# # 3.13.8 While Loop 4
# # We now would like to summarize this data and make it more visually appealing
# # We want to go through count_list and print a table that shows the number and its 
# # corresponding count.

# # The output should look like this neatly formatted table:
# """
# number | occurrence
#      0 | 1
#      1 | 2
#      2 | 3
#      3 | 2
#      4 | 2
#      5 | 1
#      6 | 1
#      7 | 2
#      8 | 3
#      9 | 1
#     10 | 2
# """
# # Here is our code we have written so far:

# import random

# # Create random list of integers using while loop --------------------
# random_list = []
# list_length = 20

# while len(random_list) < list_length:
#     random_list.append(random.randint(0,10))

# # Aggregate the data -------------------------------------------------
# count_list = [0] * 11
# index = 0

# while index < len(random_list):
#     number = random_list[index]
#     count_list[number] = count_list[number] + 1
#     index = index + 1
    
# # Write code here to summarize count_list and print a neatly formatted table that looks
# # like this:

# """
# number | occurrence
#      0 | 1
#      1 | 2
#      2 | 3
#      3 | 2
#      4 | 2
#      5 | 1
#      6 | 1
#      7 | 2
#      8 | 3
#      9 | 1
#     10 | 2
# """

# print "number | occurrence"
# index = 0
# num_len = len("number")

# while index < len(count_list):
#   num_spaces = num_len - len(str(index))
#   print " " * num_spaces + str(index) + " | " + count_list[index]*"*"
#   index = index + 1

# # Hint: To print 10 blank spaces in a row, we can multiply a string by a number "n"
# # to print this string n number of times:
# # print "Udacity! "*10

# # print "number | occurrence"
# # print "     " + str(number) + " | " + str(count_list[number])


# # BONUS!
# # From your summarize code you just wrote, can you make the table even more visual by 
# # replacing the count with a string of asterisks that represent the count of a number?
# # The table should look like

# """
# number | occurrence
#      0 | *
#      1 | **
#      2 | ***
#      3 | **
#      4 | **
#      5 | *
#      6 | *
#      7 | **
#      8 | ***
#      9 | *
#     10 | **
# """

# # Congratulations! You just created a distribution table of a list of numbers! 
# # This is also known as a histogram



# ########
# # 3.13.9 Product List
# # Define a procedure, product_list,
# # that takes as input a list of numbers,
# # and returns a number that is
# # the result of multiplying all
# # those numbers together.

# def product_list(list_of_numbers):
# 	# Count the number of items in the list
# 	total = 1
# 	for i in list_of_numbers:
# 		total = total * i
# 	return total

# 	# else:
# 	# 	i = 1
# 	# 	while i < len(list_of_numbers):
# 	# 		product = list_of_numbers[i]*list_of_numbers[i+1]
# 	# 		i += 1
# 	# 	return product
		
# 	# Cycle through each of the item by taking the current product and multiply it by next
# 	# if list is done, complete and return product


# print "product_list([9]): " + str(product_list([9]))
# #>>> 9

# print "product_list([1,2,3,4]): " + str(product_list([1,2,3,4]))
# #>>> 24

# print "product_list([]): " + str(product_list([]))
# #>>> 1



# #######
# # 3.13.10 Quiz Greatest
# # Define a procedure, greatest,
# # that takes as input a list
# # of positive numbers, and
# # returns the greatest number
# # in that list. If the input
# # list is empty, the output
# # should be 0.

# def greatest(list_of_numbers):
# 	if len(list_of_numbers) > 0:
# 		maxlist = max(list_of_numbers)
# 		return maxlist
# 	else:
# 		return 0


# print greatest([4,23,1])
# #>>> 23
# print greatest([])
# #>>> 0


# ######
# # 3.13.11 Strings to Lists
# # Let's play around with one more string method: string.split(), which
# # splits a string into a list of substrings, and returns it as a new list. 
# # Assign list_of_words1 to the split string1 and list_of_words2 to the split string2.

# string1 = "Yesterday, PERSON and I went to the PLACE. On our way, we saw a ADJECTIVE NOUN on a bike."
# string2 = "PLACE is located on the ADVERB side of Dublin, near the mainly ADJECTIVE areas of PLACE."
# list_of_words1 = string1.split(" ")
# print list_of_words1
# list_of_words2 = string2.split(" ")
# print list_of_words2


# ######
# # 3.13.12 Madlibs take two notes
# madlib_1 = "I can VERB around Place."
# madlib_2 = "NAME is what they call PLURALNOUN"
# parts_of_speech = ["VERB", "PLACE", "NAME", "NOUN"]
# madlib1.split()
# replaced = [...]
# " ".join(replaced)
# # cycle through madlib1 and test if in parts of speech, if so replace with UI

# # Here's another chance to practice your for loop skills. Write code for the 
# # function word_in_pos (meaning word in parts_of_speech), which takes in a string 
# # word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# # that is a substring of the variable word, then return that word in parts_of_speech, 
# # else return None.


# def word_in_pos(word, parts_of_speech):
#     for pos in parts_of_speech:
#     	if pos in word:
#     		return pos
#     return 


# test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
# parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

# print word_in_pos(test_cases[0], parts_of_speech)
# print word_in_pos(test_cases[1], parts_of_speech)
# print word_in_pos(test_cases[2], parts_of_speech)
# print word_in_pos(test_cases[3], parts_of_speech)



######
# 3.13.14 Putting it all together
# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, we have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
    	replacement = word_in_pos(word, parts_of_speech)
    	if replacement != None:
    		user_input = raw_input("Type in a " + replacement + ": ")
    		word = word.replace(replacement, user_input)
    		replaced.append(word)
    	else:
    		replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(test_string, parts_of_speech)       





