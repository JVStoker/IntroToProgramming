#DnD ability check
#I like DnD, so roll a D20 and the program will take the number and let you know what happens
check=int(input("What did you roll with your D20?"))
if check <=6:
    print("You suddenly die. To bad.")
elif check <=12:
    print("You notice a spiked pit. Immediately beneath you. You fall to your death. To bad.")
elif check >=13 <=19:
    print("You notice a spiked pit open beneath you. You manage to twist in midair, only taking half damage.")
else:
    print("The pit is so scared of you it lets you walk right past.")

