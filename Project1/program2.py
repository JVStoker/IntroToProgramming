#buying a car
#I recently bought a car so this was on my mind. if you say no to something it will tell you
#what you need to do to buy a car.
answer=input("Do you have a drivers license? (yes or no)").lower()
answer2=input("Do you have a Job? (yes or no)").lower()
if answer=="yes" and answer2=="yes":
    print("You may buy this car")
elif answer=="yes" and answer2=="no":
    print("You can't afford this car")
else:
    print("You can't drive cars. Get a license before you buy a car.")