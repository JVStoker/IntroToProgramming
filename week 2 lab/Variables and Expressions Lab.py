# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.
favgame="Legend of Zelda"
favgame2="Splatoon"
favegamecompany="Nintendo"

# Then print your variables.
print(favgame)
# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
favgame="Monster Hunter Rise"
print(favgame)
# After you've done this, try to print your variables in string using f-strings.
print(f"My favorite video game is {favgame} because it is so fun to play with friends.")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome
num1=3
num2=2
num3=7
addition=num1+num2
print(addition)
subtraction=num3-num2
print(subtraction)
multiplication=num3*num1
print(multiplication)
division=multiplication/num2
print(division)

score=10
penalty=-2
print(score)
score+=5
print(score)
score*=2
print(score)
score/=2
print(score)
finalscore=score+penalty
print(finalscore)

# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp


# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
firstname="Jamison"
lastname="Stoker"
print(f"My name is {firstname} {lastname}. It is nice to meet you!")

# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)


# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.
favcolor="blue"
favanimal="bluejay"
nickname="Jay"
print(f"Hi, my name is {firstname}! My favorite color is {favcolor} and my favorite animal is the {favanimal}.")
print(f"The reason {favanimal} is my favorite animal is because my favorite color is {favcolor} and my nickname is {nickname}")
# Upload this to Canvas under the Variable and Expressions Lab assignment.
