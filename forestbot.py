# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
def forestbot():
    treeList = ["🌳", "🌲", "🌲", "🌱", "🏕","🏡","🌳","🌳", "🌲", "🌲","🌳","🌳", "🌲", "🌲"]
    buildingList = ["🛖","🪵"]
    animalList = [ "🐕", "🐈", "🦝","🐿", "🦔" ]
    stellaList = ["🌙", "⭐", "☀️"]
    cloudList = ["☁️"]
    forest=[["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "]]
    animalAmount = random.randint(0,3)
    buildingAmout = random.randint(0,3)
    stellaX = random.randint(0,7)
    stellaY = random.randint(0,1)
    stella = stellaList[random.randint(0,2)]
    forest[stellaY][stellaX] = stella
    for x in range(11):
        cloudX = random.randint(0, 7)
        cloudY = random.randint(0, 2)
        if (forest[cloudY][cloudX] == "  "):
            forest[cloudY][cloudX] = cloudList[0]
    for x in range(animalAmount):
        animalX = random.randint(0, 7)
        animalY = random.randint(3, 7)
        if (forest[animalY][animalX] == "  "):
            forest[animalY][animalX] = animalList[random.randint(0,4)]
    for x in range(buildingAmout):
        buildingX = random.randint(0, 7)
        buildingY = random.randint(3, 7)
        if (forest[buildingY][buildingX] == "  "):
            forest[buildingY][buildingX] = buildingList[random.randint(0,1)]
    for x in range(44):
        treeX = random.randint(0, 7)
        treeY = random.randint(3, 7)
        if (forest[treeY][treeX] == "  "):
            forest[treeY][treeX] = treeList[random.randint(0,13)]
    print("森林bot🤖️>>>")
    print("为您提供每日新鲜树林中...")
    for y in forest:
        for x in y:
            print(x, end = "")

        print("")

forestbot()
