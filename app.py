"""
Mahjong Game
Game where the user plays mahjong against a bot
ICS3U
Jasmine Li
History:
May 28, 2024: Program Creation
June 7, 2024: Program Completion
June 8, 2024: Program updated with README file.
"""

import random


# ========= FUNCTIONS ============
def otherPlayersPlay(handPlayer, playerNum):
  """
  Chooses a random tile from other players' hands to play. The other player picks up a random new tile from deck. Their hand is updated.
  Args:
    handPlayer: list (one of handPlayer1, handPlayer2, or handPlayer3)
    playerNum: int (one of 2, 3, 4)
  Returns:
    handPlayer: list (the updated hand of the player)
    playerChosen: str (the tile the player put out)
  """
  # a random tile is chosen from player's hand, their hand is updated
  playerChosenIdx = random.randint(0,10)
  playerChosen = handPlayer[playerChosenIdx]
  print("\n\nPlayer",playerNum,"played:",playerChosen)
  # player recieves a random new tile from the deck, their hand is updated
  handPlayer.pop(playerChosenIdx)
  newPickUp = deck[random.randint(0,tilesLeftNum)]
  handPlayer.append(newPickUp)
  deck.remove(newPickUp)

  # the updated hand of the player and the tile the player played are returned
  return handPlayer, playerChosen

  
def inquiryPengChi(lastTile, turn0):
  """
  Prompts the user for a choice to peng, chi, or not do anything, checks if the move is valid, and updates hands if a peng or chi is completed.
  Args:
      lastTile: str (one of player2Chosen, player3Chosen, or player4Chosen)
  Returns: 
      turn0: int (returns -1 if peng or chi successful so that the right person has a turn afterwards.)
  """
  # user is prompted with whether they want to peng or chi
  pengChiChoice = input("\nDo you want to peng or chi? (peng/chi/no): ").lower()

  # prompting user until a valid response given
  while pengChiChoice != "peng" and pengChiChoice != "chi" and pengChiChoice != "no":
    pengChiChoice = input("\nPlease input one of peng, chi, no: ").lower()
    
  #depending on the user's wishes to peng or chi, program checks whether that move is valid
  if pengChiChoice == "peng":
    # initializing the counter for how many of the lastTile tile are in handMine
    sameCount = 0
    # sift through handMine to count how many same
    for i in handMine:
      if i == lastTile:
        sameCount += 1
    # if more than or equal to 2 are the same as lastTile, peng is successful, the three tiles are removed from player's hand.
    if sameCount >= 2:
      print("peng successful making",lastTile+',',lastTile+',',lastTile)
      handMine.remove(lastTile)
      handMine.remove(lastTile)
      # now it's your turn again so turn0 is set to -1 such that the right processes follow
      turn0 = -1
    else:
      print("you do not have the tiles to be able to peng (remember, to peng you need two identical tiles and the one you're trying to take in is a third identical tile)")

  # if player chooses chi, verify it's possible
  elif pengChiChoice == "chi":
    # initialize an empty list
    tileNumList = []
    # if it is a numbered tile, and in the same catagory ex. bing as the one the player before just put out, append to the list
    if lastTile.split( )[0].isdigit():
      for i in handMine:
        splitTile = i.split( )
        if splitTile[0].isdigit() and splitTile[1] == lastTile.split( )[1]:
          if splitTile[0] not in tileNumList:
            tileNumList.append(splitTile[0])
          if lastTile[0] not in tileNumList:
            tileNumList.append(lastTile[0])
      tileNumList = sorted(tileNumList)
      # modified from source: https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
      # converting all the numbers collected into integers
      for i in range(0, len(tileNumList)):
        tileNumList[i] = int(tileNumList[i])
      # if the list has at least 3 tiles in it, set the lastTile's index within the list as a variable.
      if len(tileNumList) >= 3:
        idxlastTile = tileNumList.index(int(lastTile[0]))
        # heavily modified from source: https://www.tutorjoes.in/Python_example_programs/three_consecutive_common_number
        # if there are three in a row including the tile just played, then the chi is successful.
        if idxlastTile >=2 and tileNumList[idxlastTile-2]+1 == tileNumList[idxlastTile-1] and tileNumList[idxlastTile-1]+1 == tileNumList[idxlastTile]:
          downTile1 = "{} {}".format(str(tileNumList[idxlastTile-2]), lastTile.split( )[1]) 
          downTile2 = "{} {}".format(str(tileNumList[idxlastTile-1]), lastTile.split( )[1]) 
          downTile3 = "{} {}".format(str(tileNumList[idxlastTile]), lastTile.split( )[1]) 
          print("chi successful making",downTile1+",",downTile2+",",downTile3)
          handMine.remove(downTile1)
          handMine.remove(downTile2)
          print("your hand is now",handMine)
          # this allows the turns to reset so that you now have to play a tile and the next person to go is player2 again.
          turn0 = -1

        # similar processes but with different cases (the lastTile being the first of the 3 consecutive, the second, or the third.)
        elif idxlastTile >=1 and idxlastTile <= len(tileNumList)-2 and tileNumList[idxlastTile-1]+1 == tileNumList[idxlastTile] and tileNumList[idxlastTile]+1 == tileNumList[idxlastTile+1]:
          downTile1 = "{} {}".format(str(tileNumList[idxlastTile-1]), lastTile.split( )[1]) 
          downTile2 = "{} {}".format(str(tileNumList[idxlastTile]), lastTile.split( )[1]) 
          downTile3 = "{} {}".format(str(tileNumList[idxlastTile]+1), lastTile.split( )[1]) 
          print("chi successful making",downTile1+",",downTile2+",",downTile3)
          handMine.remove(downTile1)
          handMine.remove(downTile3)
          print(handMine)
          turn0 = -1
        elif idxlastTile <= len(tileNumList)-3 and tileNumList[idxlastTile]+1 == tileNumList[idxlastTile+1] and tileNumList[idxlastTile+1]+1 == tileNumList[idxlastTile+2]:
          downTile1 = "{} {}".format(str(tileNumList[idxlastTile]), lastTile.split( )[1]) 
          downTile2 = "{} {}".format(str(tileNumList[idxlastTile+1]), lastTile.split( )[1]) 
          downTile3 = "{} {}".format(str(tileNumList[idxlastTile+2]), lastTile.split( )[1]) 
          print("chi successful making",downTile1+",",downTile2+",",downTile3)
          handMine.remove(downTile2)
          handMine.remove(downTile3)          
          print(handMine)
          turn0 = -1
        else:
          print("you do not have the tiles to be able to chi. Remember, to chi you must be able to create a progression of three adjacent-numbered tiles using the piece you want to pick up.")
      else:
        print("you do not have the tiles to be able to chi. Remember, to chi you must be able to create a progression of three adjacent-numbered tiles using the piece you want to pick up.")
    else:
      print("you do not have the tiles to be able to chi. Remember, to chi you must be able to create a progression of three adjacent-numbered tiles using the piece you want to pick up.")

  return turn0



# ====================MAIN==============================

# printing instructions
print('Welcome to this game of mahjong! Here are the rules: \n You and all players start out with 11 tiles. Each player takes their turn in playing a tile and picking up a new one. The deck consists of: \n\n "1 tiao", "2 tiao", "3 tiao", "4 tiao", "5 tiao", "6 tiao", "7 tiao", "8 tiao", "9 tiao", "1 bing", "2 bing", "3 bing", "4 bing", "5 bing", "6 bing", "7 bing", "8 bing", "9 bing", "1 wan", "2 wan", "3 wan", "4 wan", "5 wan", "6 wan", "7 wan", "8 wan", "9 wan","dong", "nan", "xi", "bei", "bai ban", "hong zhong", "fa cai" \n\nThere are four of each of the above. \n Your goal is to be left with no more tiles. To do so, you can make triples (three of the same tile) by "peng" or consecutive triples (ex. 1 bing, 2 bing, 3 bing) by "chi".\nYou can peng or chi the tile that any other player played out if in your deck, you have the other two tiles needed to complete the triple. Have fun!')

# making the deck (all the tiles within)
deck = ["1 tiao", "2 tiao", "3 tiao", "4 tiao", "5 tiao", "6 tiao", "7 tiao", "8 tiao", "9 tiao", "1 tiao", "2 tiao", "3 tiao", "4 tiao", "5 tiao", "6 tiao", "7 tiao", "8 tiao", "9 tiao", "1 tiao", "2 tiao", "3 tiao", "4 tiao", "5 tiao", "6 tiao", "7 tiao", "8 tiao", "9 tiao", "1 tiao", "2 tiao", "3 tiao", "4 tiao", "5 tiao", "6 tiao", "7 tiao", "8 tiao", "9 tiao", "1 bing", "2 bing", "3 bing", "4 bing", "5 bing", "6 bing", "7 bing", "8 bing", "9 bing", "1 bing", "2 bing", "3 bing", "4 bing", "5 bing", "6 bing", "7 bing", "8 bing", "9 bing", "1 bing", "2 bing", "3 bing", "4 bing", "5 bing", "6 bing", "7 bing", "8 bing", "9 bing", "1 bing", "2 bing", "3 bing", "4 bing", "5 bing", "6 bing", "7 bing", "8 bing", "9 bing", "1 wan", "2 wan", "3 wan", "4 wan", "5 wan", "6 wan", "7 wan", "8 wan", "9 wan", "1 wan", "2 wan", "3 wan", "4 wan", "5 wan", "6 wan", "7 wan", "8 wan", "9 wan","1 wan", "2 wan", "3 wan", "4 wan", "5 wan", "6 wan", "7 wan", "8 wan", "9 wan","1 wan", "2 wan", "3 wan", "4 wan", "5 wan", "6 wan", "7 wan", "8 wan", "9 wan","dong", "nan", "xi", "bei", "bai ban", "hong zhong", "fa cai", "dong", "nan", "xi", "bei", "bai ban", "hong zhong", "fa cai", "dong", "nan", "xi", "bei", "bai ban", "hong zhong", "fa cai", "dong", "nan", "xi", "bei", "bai ban", "hong zhong", "fa cai"]

# this is the starting number of tiles
tilesLeftNum = 135

# making my hand by randomly choosing tiles from the deck and adding to my list.
handMine = []
for i in range(11):
  randomInt = random.randint(0,tilesLeftNum)
  # adding picked up to list
  handMine.append(deck[randomInt])
  # removing the picked up tile from deck list
  deck.pop(randomInt)
  # updating mumber of tiles left in deck
  tilesLeftNum -= 1
# printing your hand
print("Your hand:",handMine)

# do the same for the other players
handPlayer2 = []
for i in range(11):
  randomInt = random.randint(0,tilesLeftNum)
  handPlayer2.append(deck[randomInt])
  deck.pop(randomInt)
  tilesLeftNum -= 1

handPlayer3 = []
for i in range(11):
  randomInt = random.randint(0,tilesLeftNum)
  handPlayer3.append(deck[randomInt])
  deck.pop(randomInt)
  tilesLeftNum -= 1

handPlayer4 = []
for i in range(11):
  randomInt = random.randint(0,tilesLeftNum)
  handPlayer4.append(deck[randomInt])
  deck.pop(randomInt)
  tilesLeftNum -= 1

# initializing turn to be 1
turn = 1

# while handMine still has tiles (not yet won)
while len(handMine) > 0:
  # if turn gets to 5, reset it to 1
  if turn == 5:
    turn = 1

  if turn == 1:
    # letting user choose the tile they wish to play out
    playChosen = input("\nType in the tile you wish to play out (ex: {}): ".format(handMine[0])).lower()
    #verification that tile chosen is in hand
    while playChosen not in handMine:
      playChosen = input("\nYou do not have this tile in your hand, please choose another: ").lower()
    # printing the tile you played
    print("\nYou Played:",playChosen)
    # updating handMine
    handMine.remove(playChosen)
    # randomly choosing new tile from deck for user to pick up
    newPickUp = deck[random.randint(0,tilesLeftNum)]
    handMine.append(newPickUp)
    deck.remove(newPickUp)
    tilesLeftNum -= 1
    # printing updated hand
    print("\nYour hand is now:",handMine)

  # turn taken right after a chi or peng success
  elif turn == 0:
    # letting user choose the tile they wish to play out
    playChosen = input("\nType in the tile you wish to play out (ex: {}): ".format(handMine[0])).lower()
    #verification that tile chosen is in hand
    while playChosen not in handMine:
      playChosen = input("\nYou do not have this tile in your hand, please choose another: ").lower()
    # printing the tile you played, updating handMine and printing updated hand
    print("\nYou Played:",playChosen)
    handMine.remove(playChosen)
    print("\nYour hand is now:",handMine)
    turn+=1
  
  # player 2's turn, they put out a tile and recieve a new one as well as user is inquired whether they wish to peng or chi  
  elif turn == 2:
    handPlayer2, player2Chosen = otherPlayersPlay(handPlayer2, 2)
    tilesLeftNum -= 1
    turn = inquiryPengChi(player2Chosen, turn)
  # player 3's turn
  elif turn == 3:
    handPlayer3, player3Chosen = otherPlayersPlay(handPlayer3, 3)
    tilesLeftNum -= 1
    turn = inquiryPengChi(player3Chosen, turn)
  # player 4's turn
  else:
    handPlayer4, player4Chosen = otherPlayersPlay(handPlayer4, 4)
    tilesLeftNum -= 1
    turn = inquiryPengChi(player4Chosen, turn)
  turn += 1

print ("Congradulations! You won!")
