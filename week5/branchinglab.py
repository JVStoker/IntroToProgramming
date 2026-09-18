#grading system based on what percent there grades are

score=int(input("what is your grade percent?"))
if score >90:
    print("You have an A")
elif 80 <= score <=90:
    print("You have a B")
elif 70 <= score <=80:
    print("You have a C")
elif 60 <= score <=70:
    print("You have a D")
else:
    print("You have an F")


#discount calculator
price=float(input("Enter your price: "))
if price>250:
    print("discount is 15 percent")
elif price>100 <250:
    print("discount is 15 percent ")
elif price>50 <99:
    print("Discount is 10 percent")
elif price>30 <50:
    print("Discount is 5 percent")
else:
    print("no discount")



#password
#len is used to count how many characters an obj is
password=input("Enter your password")
if len(password)>=8:
    print("Password is the right length")
else:
    print("Password is too short")