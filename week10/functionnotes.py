#week 10 notes, function
#what is a function
# a function is a named set of instructions you can run whenever you want
#functions let us write code once and reuse it when we need it

#Def(define) a function: create a function by starting with def
#Call a function: run the function by using its name with parantheses()
#parameter: placeholder variable inside the function definition
#Argument: The real value that we pass into the function via the parameter

#create a function that says hello
# def say_hello():
#     print("Hello")
# #call the function
# say_hello()

#def tells python: im defining a function
#code inside the function must be indented
#nothing runs until you call it


#parameters and arguments
# def greet(name):
#     #name is a parameter(a placeholder)
#     print(f"Hello, {name}")
# name=input("enter your name: ")
# greet(name)
# greet("Carl")
#paramaters are like blanks, arguments fill them in

#the only time you need parameters is when we are passing information from outside the function into the function
# def greet():
#     name=input("Enter your name: ")
#     print(f"Hello, {name}")
# greet()

# #print vs return
#a function that prints:
# def hello_print():
#     print("Hello world")
# #This shows the text to the user
# #but it does not give a value back to the rest of the program

#a function that returns:
# def hello_return():
#     return "return Hello World"
# #this sends a value back to wherever the function was called
# #the caller can store it, print it, etc

# hello_return()
# hello_print()

# msg=hello_return()
# print(msg)

# result=hello_print()
# print(result) #this will print none because hello_print doesnt return the value back to the function

#print is for the user whereas return is for the program

#function example
#calc program
#PART TWO OF LAB RIGHT HERE!!!

# def calc(num1,num2):
#     operator=input("What sort of math do you want to do: +, -, *,/,")
#     #use if/else tod ecide what to do
#     #perform the math 
#     #print or return the result
#     if operator == "+":
#         return num1+num2
#     elif operator == "-":
#         return num1-num2
#     elif operator == "*":
#         return num1*num2
#     elif operator == "/":
#         return num1/num2
#     else:
#         print("invalid operation")

# print(calc(1,3))#function no has the value of 4


#fake loop
#a function can call itself, this is called recursion
#a function can behave like a loop if it repeats until a condition is met
#if a function is calling itself it must have a stop condition

#a function that prompts user if they want to continue, 
# if user says yes, ask them again
# if user doesnt want to continue "loop" stops
# def play_again():
#     answer=input("Again? (y/n): ").lower()
#     if answer=="y":
#         play_again()#calls itself again
#     else:
#         print("goodbye")
# play_again()


#LAB STUFF EXEPT PART TWO BECAUSE I JUST ADDED TO WHAT WE DID ABOVE FOR THAT
#PART ONE

# def greet_user():
#     name=input("Enter user name: ")
#     prename=input("Mr or Mrs? ")
#     print(f"Hello, {prename} {name}")
# greet_user()

#PART THREE
# def length(name):
#     return len(name)

# name=input("what is your first name? ")
# print(length(name))

#TASK FOUR

def sky_color():
    answer=input("What color is the sky: ").lower()
    if answer=="blue":
        print("correct")
    else:
        print("try again")
        sky_color()
sky_color()            


# def play_again():
#     answer=input("Again? (y/n): ").lower()
#     if answer=="y":
#         play_again()#calls itself again
#     else:
#         print("goodbye")
# play_again()