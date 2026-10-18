

#do you have enough money to buy a tank of gas?
gas_money=int(input("how much money do you have for gas?"))
while gas_money < 52 or gas_money > 120:
    print("not enough")
    gas_money=int(input("how much money do you have for gas?"))
print("you have enough for a tank of gas")