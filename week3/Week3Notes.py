a=10
#reassign
a=12
b=12
sum=a**b
print(f"the of the 2 variables is {sum}")

# #INT: Whole numbers (decimanl point, 10, 5, 3, 6)
# num1=10 #INT value because there's no decimal
# #Float: decimal numbers (10.0, 5.0, 6.6, 3.6)
# num2=2.25
# word="cat"

# print(num1,type(num1))
# print(num2,type(num2))
# print(word,type(word))

# #between these two operators / and //, which gives INT value and what gives Float
# #// is Floor division and gives INT result
# print(10//3)
# #/ is regular division and gives Float result
# print(10/3)


# user_text=input("Type something")
# print(user_text)
# print(type(user_text))
# #No matter what the input is, the data type of User Input is always string


# age_text=input("How old are you now?") #age_text is a string
# age_number=int(age_text) #This converts our string variable into a INT variable
# print(age_number,type(age_number))
# print(f"Next year, you will be {age_number+1}")

# #String is what goes between these"", String holds no numeric value
# a="54"
# b="54"
# print(a+b) #This will give 5454 instead of adding them because they are strings in "" and not INT

# word="Python"
# #indexing is used to select one character
# print(word[0]) #This will index the first character
# #Computers start with 0, so the first letter of this example is 0
# print(word[1]) #letter 2
# print(word[2]) #letter3

# #Slicing (Substring) is when we want to show a range of character
# word2="Programming"
# print(word2[0:4]) #I want to print the first 4 characters
# #print(variable_name[Start:END])
# #Start at said number and stop right before END
# print(word2[3:8])
# print(word2[:6]) #Starts at beginning and goes until number
# print(word2[6:]) #Starts at 6 and goes to the END

# phrase="Hello, World!"
# print(phrase.upper()) #To uppercase everything use .upper() function
# print(phrase.lower()) #To lowercase everything, use .lower() function

# #List is an ordered collection of values, stored within a variable using []
# numbers=[10,2,3,5]
# words=["Cat","Dog","Hamster"]
# mixed=["snake",10.25,3]
# print(numbers[0:3])
# print(numbers)
# print(numbers[3:])
# words.append("Gerbil") #this added Gerbil to the words list
# print(words)

# words.remove("Cat") #.remove to remove from list
# print(words)
