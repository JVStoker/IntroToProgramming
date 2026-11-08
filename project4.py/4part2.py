character_stats={
    "goblin":{
        "health":25,
            "mana":0,
            "level":1,
            "gold":15
    },
    "wolf":{
        "health":30,
            "mana":0,
            "level":2,
            "gold":0
    },
    "theif":{
        "health":50,
            "mana":10,
            "level":3,
            "gold":25
    },
    "wizard":{
        "health":100,
            "mana":100,
            "level":7,
            "gold":100
    },
    "evil king":{
        "health":200,
            "mana":150,
            "level":15,
            "gold":250
    }
}

answer=input("do you want to learn more about the goblin, the wolf, the thief, the wizard, or the evil king?")
answer2=input("do you want to know its health, mana, level, or gold?")
if answer=="goblin":
    if answer2=="health":
        print(character_stats["goblin"]["Health"])
    elif answer2=="mana":
        print(character_stats["goblin"]["mana"])
    elif answer2=="level:":
        print(character_stats["goblin"]["level"])
    elif answer2=="gold":
        print(character_stats["goblin"]["gold"])

elif answer=="wolf":
    if answer2=="health":
        print(character_stats["wolf"]["health"])
    elif answer2=="mana":
        print(character_stats["wolf"]["mana"])
    elif answer2=="level:":
        print(character_stats["wolf"]["level"])
    elif answer2=="gold":
        print(character_stats["wolf"]["gold"])

if answer=="theif":
    if answer2=="health":
        print(character_stats["theif"]["health"])
    elif answer2=="mana":
        print(character_stats["theif"]["mana"])
    elif answer2=="level:":
        print(character_stats["theif"]["level"])
    elif answer2=="gold":
        print(character_stats["theif"]["gold"])

if answer=="wizard":
    if answer2=="health":
        print(character_stats["wizard"]["Health"])
    elif answer2=="mana":
        print(character_stats["wizard"]["mana"])
    elif answer2=="level:":
        print(character_stats["wizard"]["level"])
    elif answer2=="gold":
        print(character_stats["wizard"]["gold"])

if answer=="evil king":
    if answer2=="health":
        print(character_stats["evil king"]["health"])
    elif answer2=="mana":
        print(character_stats["evil king"]["mana"])
    elif answer2=="level:":
        print(character_stats["evil king"]["level"])
    elif answer2=="gold":
        print(character_stats["evil king"]["gold"])
