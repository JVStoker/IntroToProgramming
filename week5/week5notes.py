#What is a boolean?
#A boolean is a value that is either true or false
# print(5>10)
# print(10<20)
# print(3>=74)
# print("Cat" == "Cat")

#Any expression that evaluates to true or false is a boolean expression
#if statements use these to decide what to run

# answer=input("Do you want to continue? (yes or no)").lower()
# if answer=="yes":
#     print("Continuing the program....")
# elif answer=="no":
#     print("Exiting the program now")
# else:
#     print("Invalid response")


# answer=int(input("Enter your percentage and I'll tell you what grade you have"))
# if answer=="yes":
#     print("Continuing the program....")
# elif answer=="no":
#     print("Exiting the program now")
# else:
#     print("Invalid response")

#== equal to
#!= not equal to
#<less than
#>greater than
#<= less than or equal To
#>= greater than or equal to

# score=85
# print(score>75)
# print(score<75)
# print(score==100)

#using AND & OR
# temp=72
# if temp>=72 and temp <=75:
#     print("This is comfortable room temp")

#When using AND, both conditions must be true
#When using OR, only one condtiond must be true

#I want this program to ouptu ("You don't have class today")
# day="saturday"
# is_holiday=False
# if day=="saturday" or day=="sunday" or is_holiday:
#     print("You don't have class today")
#this program compares multiple conditions at the same time

#same program, diffrent method
# day="saturday"
# is_holiday=False
# if day=="saturday":
#     print("No class its saturday")
# elif day=="sunday":
#     print("No class its sunday")
# elif is_holiday==False:
#     print("It's a holiday")

#Chained comparisons
# score=75
# #how to write out 65 is <=score but less than 90
# if 60 <= score <90:  #this is also the same thing as score>=60 and score <90
#     print("score is passing but not perfect")

#Using if+elif+else
#This is a simple 3 catagory example
#THis program prints out the shipping cost based on the order price
#When using any sort of money input use float because float does decimals
# total=float(input("Enter your total: "))
# if total<25:
#     print("Shipping is $10")
#if user input is less than 50 they get $5 shipping
# elif total<50:
#     print("You get $5 dollar shipping! ")
# else:
#     print("Free shipping!!")

#compare ==& is
# list1=[1,2,3]
# list2=[1,2,3]
# list3=list1
# print(list1==list2) #True: contents are equal
# print(list1 is list2) #false: diffrent objects in memory
# print(list1==list3) #True: Contents still the same
# print(list1 is list 3) #True: because list 3 points to the the same object as list 1

#== compares values and content
#IS compares indentity(Are they literally the same object?)
#2 diffrent boxes can have the same stuff inside (==)
#but they are still two diffrent boxes (IS)

#Multibranch example
#program that tells me if a number is positive or negative
number=int(input("Enter your number"))
if number <0:
    print("This number is negative")
elif number >0:
    print("This number is positive")
else:
    print("Your number is 0")
