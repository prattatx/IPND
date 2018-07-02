# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# finding the number of prompts

# below block only finds descrete prompts, doesnt work if repeated
# prompt_count = 0
# prompt_count = sample.count(" ___")
# print prompt_count

# find the highest prompt number, strike that, just make a prompt matrix to test against
quest_prompts = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]

def prompt_in_pos(prompt, quest_prompts):
    for pos in quest_prompts:
        if pos in prompt:
            return pos
    return None
        
def play_game(ml_string, quest_prompts):    
    replaced = []
    ml_string = ml_string.split()
    for prompt in ml_string:
    	replacement = prompt_in_pos(prompt, quest_prompts)
    	if replacement != None:
    		user_input = raw_input("What should be substituted for " + replacement + "? ")
    		replacement = [w.replace(user_input, quest_prompts) for w in replacement]
    		# prompt = prompt.replace(replacement, user_input)
    		replaced.append(prompt)
    	else:
    		replaced.append(prompt)
    replaced = " ".join(replaced)
    return replaced

print play_game(sample, quest_prompts) 