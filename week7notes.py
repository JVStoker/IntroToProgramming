#what is a loop
#a loop repeats code
#python uses while and for loops

#repeat this loop 3 times
# for number in range(3):
#     #print hello each time the loop runs
#     print("Hello")


#while loops 
# a while loop repeats while a condition is true
#create a starting variable
# number=1
#keep looping while number is less than or equal to 5
# while number<=5:
#     #print the current value of number
#     print(number)
#     #add 1 to number after each loop
#     number+=1

#make sure something changes inside a while loop otherwise you may create an infinite loop

#while loops with user input
#A while loop is useful when you want to keep asking until a user gives a valid answer

# #ask user for their age
# age=int(input("Enter your age"))
# #keep looping if the age is less than 1 or greater than 120
# while age < 1 or age > 120:
#     #tell the user their input was invalid
#     print("invalid age")
#     #ask user to give age again
#     age=int(input("Enter your age"))
# #This runs after loop finishes
# #loop stops once the condition becomes false
# print("age is valid")

#for loops
#a for loop works through items one at a time

# #create a list containing anything
# games=["Minecraft, Mario, Zelda"]
# #take 1 item from the games list at a time
# for game in games:
#     #print the current game
#     print(game)


#using range
#range() is a sequence of numbers

#start at 2 and stop before 8
# for number in range(2,8):
#      #2 is our starting point and we will stop before 8
#      print(number)
#      #remember the ending number is range() is not included

#loop through 2 through7
# for number in range(2,8):
#      #multiply the number by itself
#      square=number*number
#      #print the squared number
#      print(square)

#looping through strings
#a string can be looped through one character at a time
#store a string value inside a variable

# word="Tanks"
# #take one character from the string at a time
# for letter in word:
#     #prints the current letter
#     print(letter)


#using break
#break stops a loop early
#loop through numbers one through 10
# for number in range(1,11):
#     #print the current number
#     print(number)
#     #want to stop the loop when the number =5
#     if number==5:
#         #stops the loop immediately
#         break 


# #nested loops
# #nested loops are loops inside of loops
# #outer loop that runs through 123
# for number in range(1,4):
#     #inner loop also runs through 123
#     for number2 in range(1,4):
#         #print the current value from both loops
#         print(number,number2)



#choosing the right loop
#use a while loop when repition depends on a condition
#keep looping while answer is not yes
# answer=input("enter yes")
# while answer != "yes":
#     #ask the user again
#     answer=input("enter yes")

# #use a for loop when working through items
# #go through each item in the list
# itemlist=[1,2,3,]
# for item in itemlist:
#     print(item)

# #use for loop with range() when working through numbers
# #go through 1-10
# for number in range(1,11):
#     #print current number
#     print(number)


#MY LAB THINGS START HERE!!!!!

# for number in range(1,6):
#     print(number)


# nuggets=int(input("How many chicken nuggets do you want?"))
# while nuggets < 5 or nuggets > 30:
#     print("we don't sell that count of nuggets")
#     nuggets=int(input("How many chicken nuggets do you want?"))
# print("Here's your nuggets")


# berries=["blueberry, strawberry, rasberry"]
# for berry in berries:
#     print(berry)

#loop with range
# for number in range(2,8):
#     print(number)

#modified loop with range to square each number
# for number in range(2,8):
#     square=number*number
#     print(square)


# name="Jamison"
# for letter in name:
#     print(letter)


# for number in range(1,11):
#     print(number)
#     if number==8:
#         break


# for x in range(1,7):
#     for y in range(1,7):
#         print(x,y)
#what this is doing is it is printing all of y for every x
#once y is done, it goes to the next x and prints all of y again
