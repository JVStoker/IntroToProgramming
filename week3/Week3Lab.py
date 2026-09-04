a=4
b=8.5
print(a+b) #yes you can do math because they are both treated as numbers
a=input("Enter a whole Number")
b=input("Enter a decimal number")
print(a+b)

#A string is what goes between"" and has no numeric value
color="Blue"
skycolor="The sky is "
print(skycolor,color)

mysubstring=color[0:3]
print(mysubstring)

#A list can contain words, letters, numbers, or whatever else you can type out
fruit=["Strawberry","Watermellon","Mango","Apple"]
fruit.append("Pears")
print(fruit) #it added pears to my list
fruit.remove("Mango")
print(fruit)
print(len(fruit))
