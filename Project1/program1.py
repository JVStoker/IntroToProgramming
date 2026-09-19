#DnD ability check
check=int(input("What did you roll with your D20?"))
if check <=6:
    print("You suddenly die. To bad.")
elif check <=12:
    print("You notice a spiked pit. Immediately beneath you. You fall to your death. To bad.")
elif check >=13 <=19:
    print("You notice a spiked pit open beneath you. You manage to twist in midair, only taking half damage.")
else:
    print("The pit is so scared of you it lets you walk right past.")


#buying a car
answer=input("Do you have a drivers license? (yes or no)").lower()
answer2=input("Do you have a Job? (yes or no)").lower()
if answer=="yes" and answer2=="yes":
    print("You may buy this car")
elif answer=="yes" and answer2=="no":
    print("You can't afford this car")
else:
    print("You can't drive cars. Get a license before you buy a car.")