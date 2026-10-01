#I wrote a program to see if you have enough money to buy a certain product

product=input("would you like to buy a computer, a nintendo switch 2, or a mp3 player?")
price=int(input("how much money do you have to spend? (ex. 20)"))
if product == "mp3 player":
    if 49 <= price <=100000:
        print("you can afford it!")
    else:
        print("You can't afford it")
elif product == "nintendo switch 2":
    if 499 <= price <=100000:
        print("you can afford it")
    else:
        print("you can't afford it")
elif product == "computer":
    if 999 <= price <=10000000:
        print("you can afford it!")
    else:
        print("You can't afford it")
else:
    print("that product is not an option")