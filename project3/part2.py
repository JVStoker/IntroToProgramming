
#favorite number

favorite=int(input("what is your favorite number 1-99?"))
for number in range(1,100):
    print(number)
    if number==favorite:
        break 