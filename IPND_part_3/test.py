# print 'hello, world!'

s = 'a'
#print s[3] , s[1 + 1 + 1]
#print s[0] , (s + s)[0]
#print s[0] + s[1] , s[0 + 1]
#print s[1] , (s + 'ity')[1]
#print s[-1] , (s + s)[-1]

# word = 'assume'
# print word[3]
# print word[4:6]
# print word[4:]
# print word[:2]
# print word[:]

# s = 'audacity'
# print 'U' + s[2:]

# s = "any string"
# print s[:]
# print s + s[0:-1+1]
# print s[0:]
# print s[:-1]
# print s[:3] + s[3:]

# pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres.'
# print pythagoras.find('string')
# print pythagoras[40:]
# print pythagoras.find('T')
# print pythagoras.find('sphere')
# print pythagoras[86:]
# print pythagoras.find('algebra')

# print "Test".find('te')
# print 'west'.find('test')

# s = "any string"
# print s.find('')
# print s.find(s + '!!!') + 1

# print "Example 1: Finding substrings in a string"
# print "test".find("te")
# print "test".find("st")
# print "test"[2:]

# print "Example 2: Finding substrings in a string which is stored as a variable"
# my_string = "test"
# print my_string.find("te")
# print my_string.find("st")
# print my_string[2:]

# print "Example 3: Printing out everything after a certain substring"
# my_string = "My favorite color: blue"
# color_start_location = my_string.find("color:")
# favorite_color = my_string[color_start_location:]
# print favorite_color # oops, this line prints out 'color: ' as well...
# print favorite_color[7:] # this fixes it!
# print color_start_location
# print favorite_color
# print my_string[color_start_location + 7:]

# print "Example 1: using find to print the second occurrence of a sub-string"
# print "test".find("t")
# print "test".find("t", 1)

# # Given the variables s and t defined as:
# s = 'udacity'
# t = 'bodacious'
# # write Python code that prints out udacious
# # without using any quote characters in
# # your code.
# begin = s[:-2]
# end = t[-3:]
# final = begin + end
# print final

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.

# sentence = "A NOUN went on a walk. It can VERB really fast."
# substring1 = sentence[:2]
# substring2 = sentence[6:-17]
# substring3 = sentence[-13:]
# print substring1
# print substring2
# print substring3


# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

# mary = "Mary"
# # Your code goes here
# randa = mary
# katie = randa
# salwa = katie
# kathleen = salwa
# gamriel = kathleen


# # In South America, the alias Kathleen is known as the alias Gabriel, this means that:
# gabriel = kathleen

# # Test to see if all of these variables will print out the string "Mary"
# print gabriel
# print kathleen
# print salwa
# print katie
# print randa
# print mary


# def udacify(string1):
# 	return 'U' + string1

# print udacify('dacians')


# def double1(x):
# 	return 2 * x
# print "1:"
# print double1(5)

# def double2(x):
# 	print 2 * x
# print "2:"
# print double2(5)

# def double3(x):
# 	return 2 * x
# 	print 2 * x
# print "3:"
# print double3(5)

# def double4(x):
# 	print 2 * x
# 	return 2 * x
# print "4:"
# print double4(5)

# def bigger (num1, num2):
#     if num1-num2 > 0:
# 		return num1
#     else:
#     	if num1 - num2 == 0:
# 			return num1
#     	return num2


# def bigger2 (anum1, anum2):
# 	if anum1 < anum2:
# 		return anum2
# 	else:
# 		return anum1


# print bigger2(2,2)
# print bigger2(2,1)
# print bigger2(2,3)


# def bigger1(num1, num2):
# 	if num1<num2:
# 		return num2
# 	else:
# 		return num1

# def bigger2(num2, num3):
# 	if num2<num3:
# 		return num3
# 	else:
# 		return num2

# def biggest(num1, num2, num3):
# 	if bigger1<bigger2 or bigger1<num3:
# 		return bigger2
# 	else:
# 		bigger 


# def biggest(num1, num2, num3):
# 	if (num1 > num2 or num1 == num2) and (num1 > num3 or num1 == num3):
# 		return num1
# 	else:
# 		if (num2 > num1 or num2 == num1) and (num2 > num3 or num2==num3):
# 			return num2
# 		else:
# 			if (num3 > num1 and num3 == num1) or (num3 > num2 or num3==num2):
# 				return num3
# 	return False

# better version of above block

# def biggest(a,b,c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c

# print biggest(3, 6, 9)
# #>>> 9

# print biggest(6, 9, 3)
# #>>> 9

# print biggest(9, 3, 6)
# #>>> 9

# print biggest(3, 3, 9)
# #>>> 9

# print biggest(9, 3, 9)
# #>>> 9

# print biggest(2, 2, 1)


# def print_numbers(num):
# 	i=1
# 	while i < (num + 1):
# 		print i
# 		i=i+1
# print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

# def bigger(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# def biggest(a,b,c):
#     return bigger(a,bigger(b,c))

# def median(a,b,c):
# 	big = biggest(a,b,c)
# 	if big == a:
# 		return bigger(b,c)
# 	if big == b:
# 		return bigger(a,c)
# 	else:
# 		return bigger(a,b)

# print(median(1,3,2))

# print(median(1,2,3))
# #>>> 2

# print(median(9,3,6))
# #>>> 6

# print(median(7,8,7))
# #>>> 7

# import the random function, randint(low,high)
# from random import randint
# num = randint(1, 3)
# print num

# from random import randint

# def random_noun():
#     # your code here
#     num = randint(0,1)
#     if num == 0:
#         return "sofa"
#     else:
#         if num == 1:
#             return "llama"
#     return

# print random_noun()


# # Write code for the function random_verb, which takes in no inputs but outputs 
# # one of two verbs randomly. Use the randint function to generate a number from 0-1 
# # and return a verb depending on whether the number is equal 0 or 1. Feel free to 
# # experiment with different verbs, but for submission purposes return the string "run"
# # if the number is 0, else return "kayak".

# from random import randint

# def random_verb():
#     # your code here 
#     num = randint(0,1)
#     if num == 0:
#         return "run"
#     else:
#         if num == 1:
#             return "kayak"
#     return

# print random_verb()


# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

# from random import randint

# def random_verb():
#     random_num = randint(0, 1)
#     if random_num == 0:
#         return "run"
#     else:
#         return "kayak"
        
# def random_noun():
#     random_num = randint(0,1)
#     if random_num == 0:
#         return "sofa"
#     else:
#         return "llama"

# def word_transformer(word):
#     # your code here
#     if word == "NOUN":
#         return random_noun()
#     if word == "VERB":
#         return random_verb()
#     else:
#         return word[0]

        
# def process_madlib(mad_lib):
#     processed = ""
#     # print "test 1: " + mad_lib[0]
#     # print "test 2: " + mad_lib[4]
#     # print "test 3: " + mad_lib[1:]
#     # print "test 5: " + mad_lib[1:6]
#     # print "test 4: " + mad_lib[:len(mad_lib)]
#     # # print len(processed)
#     # your code here
#     # you may find the built-in len function useful for this quiz
#     # documentation: https://docs.python.org/2/library/functions.html#len

#     # i continues down the sentence until done
#     # comp_lenth is the comparison length, 1 for not NOUN or VERB, and 4 otherwise
#     i = 0
#     comp_length = 4
#     while i < len(mad_lib):
#     	frame = mad_lib[i : i + comp_length]
#     	construction = word_transformer(frame)
#     	processed = processed + construction
#     	if len(construction)==1:
#     		i = i + 1
#     	else:
#     		i = i +4
#     return processed

    
# test_string_1 = "This is a good NOUN to use when you VERB your food."
# test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
# print process_madlib(test_string_1)
# print process_madlib(test_string_2)

# Given the variable,

# days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# # define a procedure, how_many_days,
# # that takes as input a number
# # representing a month, and returns
# # the number of days in that month.

# def how_many_days(month_number):
#     return days_in_month[month_number - 1]


# print how_many_days(1)
# #>>> 31

# print how_many_days(9)
# #>>> 30

# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
# countries = [['China','Beijing',1350],
#              ['India','Delhi',1210],
#              ['Romania','Bucharest',21],
#              ['United States','Washington',307]]

# # Write code to print out the capital of India
# # by accessing the list

# # print countries[1][1]
# print countries[0][2]/countries[2][2]

# We defined:

# stooges = ['Moe','Larry','Curly']

# # but in some Stooges films, Curly was
# # replaced by Shemp.

# # Write one line of code that changes
# # the value of stooges to be:

# # ['Moe','Larry','Shemp']

# # but does not create a new List
# # object.

# stooges[2] = 'Shemp'
# print stooges


# spy = [0,0,7]
# agent = spy
# spy[2] = agent[2] + 1

# print agent[2]


# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

# spy = [0,0,7]

# def replace_spy(nums):
# 	nums[2] = nums[2] + 1
# 	return nums



# # In the test below, the first line calls your 
# # procedure which will change spy, and the 
# # second checks you have changed it.
# # Uncomment the top two lines below.

# replace_spy(spy)
# print spy
# #>>> [0,0,8]


# def print_all_elements(p):
#     i = 0
#     while i < len(p):
#         print p[i]
#         i = i + 1

# p = [1,2,[3,4,5]]
# print_all_elements(p)

#############
# 3.11.26
# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

# def sum_list(p):
# 	sumup = 0
# 	for items in p:
# 		sumup = sumup + items
# 	return sumup

# print sum_list([1, 7, 4])
# #>>> 12

# print sum_list([9, 4, 10])
# #>>> 23

# print sum_list([44, 14, 76])
# #>>> 134

#####
# 3.11.28
# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

# def measure_udacity(p):
# 	capUs = 0
# 	for e in p:
# 		if e[0] == 'U':
# 			capUs = capUs + 1
# 	return capUs


# print measure_udacity(['Dave','Sebastian','Katy'])
# #>>> 0

# print measure_udacity(['Umika','Umberto'])
#>>> 2


#########
# 3.11.29
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# def find_element(p, q):
# 	for e in p:
# 		if e == q:
# 			return p.index(q)
# 	return -1

###### or Index Methog

# def find_element(p, q):
# 	if q in p:
# 		return p.index(q)
# 	return -1

# print find_element([1,2,3],3)
# #>>> 2

# print find_element(['alpha','beta'],'gamma')
# #>>> -1


#######
# 3.12.3
# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

# #inputs
# today = 5/28/2018
# birthday = 8/31/1968
# # second date is not before first date

# daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def isLeapYear(year):
#     ##
#     # Your code here. Return True or False
#     # Pseudo code for this algorithm is found at
#     # http://en.wikipedia.org/wiki/Leap_year#Algorithm
#     ##

# def daysBetweenDates(y1, m1, d1, y2, m2, d2):
#     ##
#     # Your code here.
#     ##
#     return days

# Problem is defined by possible inputs and desired outputs
# 0. Don't Panic
# 1. understand possible inputs
# 2. what are the outputs
# 2.5 understand the relationship between inputs and outputs
# 2.7 work through examples by hand
# 3. solve the problem  in simple mechanical solution
# 4. develop and test incrementally 

# Complicated solution pseudocode
# days left in starting month
# days = number of days in month1 - day1
# month += 1
# while month1 < month2:
# 	days += number of days in month1
# 	month1 += 1
# days += day2
# while year1 < year2:
# 	days += days in year1

# #simple psedo code
# days = 0
# while date1 is before date2:
# 	date1 = advnace to next day
# 	days += 1

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

# def nextDay(year, month, day):
#     """
#     Returns the year, month, day of the next day.
#     Simple version: assume every month has 30 days.
#     """
#     # YOUR CODE HERE
#     if month < 12:
#         if day < 30:
#             day = day + 1
#         else:
#             month += 1
#             day = 1
#     else:
#     	if day < 30:
#     		day += 1
#     	else:
#         	year += 1
#         	month = 1
#         	day = 1
#     return (year, month, day)

# def daysBetweenDates()

# print nextDay(2012, 1, 1)
# print nextDay(2012, 4, 30)
# print nextDay(1999, 12, 30) 
# print nextDay(2012, 12, 30)
# print nextDay(2012, 12, 1)



######
# 3.12.25
# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def daysInMonth(year, month):
	if month == 1 or month == 3 or month == 5 or month ==7 \
		or month == 8 or month == 10 or month ==12:
		return 31
	else:
		if month == 2:
			if is_leap_year(year):
				return 29
			else:
				return 28
	return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

# My veersion that worked, but pasting in instrcotr version below
# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
# 	days = 0
# 	while(not(year1==year2 and month1==month2 and day1==day2)):
# 		year1, month1, day1 = nextDay(year1, month1, day1)
# 		days = days + 1
# 	return days

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def is_leap_year(year):
    """Determine whether a year is a leap year."""
    if year % 400 == 0:
    	return True
    if year % 100 == 0:
    	return False
    if year % 4 == 0:
    	return True
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1) 
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        # print result
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()