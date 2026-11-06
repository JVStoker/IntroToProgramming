#how to make a list
favgames=["Halo", "Elden Ring", "RE2", "RE2"]

#indexing
#searching through a list via its placement
# print(favgames[0]) #this prints out the first list item
# print(favgames[1])
# print(favgames[2])

#Using the len() with a list
# we can use Len() to count how many items are in a list
# print(len(favgames))

#adding items to a list
#append() adds to the end of the list
#inser() adds an item to a specfic postition
# favgames.append("Mario kart")
# print(len(favgames))

#inserting a list item at a certain position
# favgames.insert(0,"RE4")
# print(favgames)

#common list methods
#count() counts how many times a value appears
#remove() removes a specfic item
#sort() puts the list in a sorted order
#reverse() flips the current order of the list

#Count() example
# print(favgames.count("RE2"))

#remove() example
# favgames.remove("Halo")
# print(favgames)

#sort example
# favgames.sort()
# print(favgames)

#reverse example
# favgames.reverse()
# print(favgames)

#looping through a list
#we use a FOR loop when we want to print out the items in a list
# for game in favgames:
#     print(game)






#Dictionaries
#Dictionaries are usually accessed by key not position
# we use a dictionary when labels matter and you want to look things up by name

# player_stats={
#     #"key": Value
#     "Health":100,
#     "Mana":40,
#     "level":7,
#     "Gold":250
# }
# #a dictionary stores data in key:value pairs

# #How to access data from a dictionary?
# # print(player_stats["Health"])

# #Adding and updating dictionary values
# #you can add a new key value pair by assigning a value to a new key
# #we can also update an existing value or increase it

# #Adding a new key:value
# player_stats["Strength"]=12
# # print(player_stats)

# #update a value
# player_stats["Health"]=250
# # print(player_stats)

# #adding to a value
# player_stats["Gold"]+=50

# player_stats["Mana"]+=50
# print(player_stats)

#keys() and values()
#keys() shows all dictionary keys
#values() shows all dictionart values

# print(player_stats.keys())
# print(player_stats.values())

#looping through dictionaries
#you can loop through keys, values, or both
#.items() is often the most readable way to show everything in a dictionary

#key for loop
# for key in player_stats.keys():
#     print(key)
# #Value for loop
# for value in player_stats.values():
#     print(value)

# for key, value in player_stats.items():
#     print(f"{key}:{value}")


# nested dictionaries
students={
    "001":{
        "Name":"Ana",
        "Major":"Cyber",
        "Credits":15,
        "HS Info":{
            "GPA":3.5
        }
    },
    "002":{
        "name":"Jay",
        "Major":"computer",
        "credits":15
    }
}
#accesing nested dictionary data
#to access nested data, go one level at a time 
print(students["001"]["HS Info"]["GPA"])

# #combining a nested dictionary with a list
# cars={
#     "Honda":{
#         "Location":"Japan",
#         "Founded":1950,
#         "Models": ["NSX", "Civic", "Rebel", "Accord"]
#     }
# }

# print(cars["Honda"]["Models"])