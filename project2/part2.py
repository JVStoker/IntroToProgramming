

food=input("What food item do you want?")
number=int(input("How many do you want?"))

for i in range(1,100):
    print(i)
    if i==number:
        break 
print(f"you got {number} {food}")