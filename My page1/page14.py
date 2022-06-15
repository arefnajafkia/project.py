# Hello World project 
# python3
#تاس انداختن چندتايي 
#باچندتاتاس ميخواهي بازي کني 
#هم ميشه دوتاسه بازي کردمناسب تخته نربازي وهم اينکه چندتايي وهم تکي

import random


while True:
    playerDecision = int (input ("what you want to do ?\n چيکارميکنيدشما؟ اگه تاس ميريزي 1روبزن واگرميخواهي خارج بشي 2روبزن \n 1.roll the dice  2.exit \n"))
    if playerDecision == 1:
        totalplayers = int (input ("How many dice do you want to play with ? \n باچندتاتاس ميخواهي بازي کني؟ :"))
        playerNumber = 1
        for player in range(totalplayers):
            result = random.randint(1,6)
            print (f"Result for {playerNumber} is:" , result)
            playerNumber+=1
            print()
    else:
        break