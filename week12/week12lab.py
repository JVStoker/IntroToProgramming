
# shopping_cart=["apple", "apple", "orange", "blueberry", "bread", "pizza", "expired chips"]
# print(len(shopping_cart))
# print(shopping_cart[3])
# print(shopping_cart[1])
# shopping_cart.append("juice")
# shopping_cart.insert(3, "milk")
# print(shopping_cart)


# print(shopping_cart.count("apple"))
# shopping_cart.remove("expired chips")
# shopping_cart.sort()
# print(shopping_cart) #alphabetized my list
# shopping_cart.reverse()
# print(shopping_cart)#printed my alphabetized list in reverse


# inventory={
#     "Apples":10,
#     "Bananas":15,
#     "Oranges":8,
#     "Blueberrys":12
# }
# print(len(inventory.keys()))
# inventory["Grapes"]=4
# inventory["Apples"]+=5
# # print(inventory.keys())
# # print(inventory.values())

# for key in inventory.keys():
#     print(key)
# for value in inventory.values():
#     print(value)

# for key, value in inventory.items():
#     print(f"{key}:{value}")


customers={
    "001":{
        "name":"James Bond",
        "items bought": ["Melee weapon", "Spy watch", "Disguise Kit"],
        "total spent":421.20
    },
    "002":{
        "name":"mario",
        "items bought": ["pipe wrench", "overalls", "gift card"],
        "total spent":110.00 
    }

}

print(customers["001"]["name"])
print(customers["002"]["total spent"])

