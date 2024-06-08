import random

players =[ "martin", "craig" ,"sue", "claire" ,"dave" ,"alice" ,"sona","harry","ben","monica","joe","pam","jim","sara","adam","grace","jack","henry","may","william","norman"]


print(" Welcome to the team allocator!")
while True: 
    random.shuffle(players)
    team1 =players[:len(players)//3]
    print("team 1 captain:" + random.choice(team1))
    print("team 1:")
    for player in team1:
     print(player)

    team2 = players[len(players)//3:len(players)//3*2]
    print("\n team 2  captain: " + random.choice(team2))
    print("team 2:")
    for player in team2:
     print(player)

    team3 = players[(len(players)//3)*2:]
    print("\nteam 3 captain :" + random.choice(team3) )
    print("team 3 :")
    for player in team3:
      print(player)


    responce = input("pick again? type y or n:")
    if responce == "n":
       break


     