


hours=int(input("how many hours did you work?"))
pay=int(input("How much do you get paid per hour?"))

for i in range(1,100):
    
    #print(i)
    if i==hours:
        break 
print(f"you got {hours*pay} dollars")