import tweepy
import time
import random
import datetime


CONSUMER_KEY = 'AAAA'
CONSUMER_SECRET = 'BBBB'
ACCESS_KEY = 'CCCC'
ACCESS_SECRET = 'DDDD'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return



def forestbot():
    treeList = ["🌳", "🌲", "🌲", "🍀" ,"🌳","🌳", "🌲", "🌲","🌳","🌳","🌲", "🌲","🌿"]
    buildingList = ["🏕","⛺️","🏡"]
    animalList = [ "🐕", "🐈", "🦝","🐿", "🦔","🐻","🦌","🦊","🐯","🐰","🐢","🐗","🐐","🐒"]
    stellaList = ["🌙", "☀️","⛅️","🌨","🌥","🌨","🌦","🌑"]
    cloudList = ["☁️"]
    forest=[["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "]]

    skyHeight = random.randint(2,4)
    groundHeight = skyHeight + 1
    animalAmount = random.randint(0,4)
    buildingAmount = random.randint(0,3)
    cloudAmount = random.randint(skyHeight*3,skyHeight*5)
    treeAmount = random.randint((9-skyHeight)*7,(9-skyHeight)*9)
    stellaX = random.randint(0,9)
    stellaY = random.randint(0,1)
    stella = stellaList[random.randint(0,len(stellaList)-1)]
    forest[stellaY][stellaX] = stella
    for x in range(cloudAmount):
        cloudX = random.randint(0, 9)
        cloudY = random.randint(0, skyHeight)
        if (forest[cloudY][cloudX] == "  "):
            forest[cloudY][cloudX] = cloudList[0]
    for x in range(animalAmount):
        animalX = random.randint(0, 9)
        animalY = random.randint(groundHeight, 9)
        if (forest[animalY][animalX] == "  "):
            forest[animalY][animalX] = animalList[random.randint(0,len(animalList)-1)]
    for x in range(buildingAmount):
        buildingX = random.randint(0, 9)
        buildingY = random.randint(groundHeight, 9)
        if (forest[buildingY][buildingX] == "  "):
            forest[buildingY][buildingX] = buildingList[random.randint(0,len(buildingList)-1)]
    for x in range(treeAmount):
        treeX = random.randint(0, 9)
        treeY = random.randint(groundHeight, 9)
        if (forest[treeY][treeX] == "  "):
            forest[treeY][treeX] = treeList[random.randint(0,len(treeList) - 1)]
    output = ""
    for x in forest:
        output += "".join(x) + "\n"
    return output


def reply_to_tweets():
  """reply when someone @ you and used hashtags #forest #emoji"""
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(since_id = last_seen_id)
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#emoji' or '#forest' in mention.text.lower():
            print('responding back...', flush=True)
            message = "@" + mention.user.screen_name + forestbot()
            api.update_status(message,in_reply_to_status_id = mention.id)


def tweets_forest():
  """tweet when the time is 18:30, 19:30, 20:30 etc."""
    now = datetime.datetime.now()
    if now.minute == 30:
        print("It's time to tweet!")
        api.update_status(forestbot())


while True:
    reply_to_tweets()
    tweets_forest()

    time.sleep(60)

