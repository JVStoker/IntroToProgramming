#file modes
#when you open a file you give python 2 things
# the filename
#the mode

#common modes
# "W"=write
#creates the file if it doesn't exist
#also overwrites the file if it does exist (deletes all the content that was in the file)

#"R"=read only
# you can read the file but can't change it
#error if file doesn't exist

#"A"=append
#creates file if it doesn't exist
#also adds new text to the end without deleting existing content

# with open("Foldername/filename", "mode")
# with open("week9/stuff.txt","r") as file:
#     contents=file.read()
#     print(contents)

# with open("week9/stuff.txt","w") as file:
#     file.write("This is going to be line 1 \n")
#     file.write("This is going to be on line 2 \n")
#     file.write("This is going to be on line 3 \n")
    #\n means new line
    #if you forget\n it will run everything on one line

#created a new document
# with open("week9/stuff2.txt","w")as file:
#     file.write("This is a new document")

#reading from a file
#method A: read the whole file at once
# with open("week9/stuff.txt","r") as file:
#     contents=file.read()
#     print(contents)

#Method B: read line by line using a for loop
# with open("week9/stuff.txt","r") as file:
#     for line in file:
#         print(line)

#appending the file
with open("week9/stuff.txt","a") as file:
    file.write("I am adding to this file \n")
    file.write("Stuff is going on this page \n")
#file.write(variable name) to put a variable in a txt file