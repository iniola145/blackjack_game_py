############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# import random
# ask = input("Input yes or no to continue the blackjack game: ")
# def checker(player1, computer1):
#   if (computer1 > 21 and player1 < 21):
#     print(f"You win")
#   elif player1 == 21:
#     print(f"You win")
#   elif computer1 == player1 and computer1 <= 21 and player1 <= 21:
#     print(f"You draw")
#   elif player1 > computer1 and computer1 <= 21 and player1 <= 21:
#     print(f"You win")
#   else:
#     print(f"You lose")
# if ask == "yes":
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   player = 0
#   computer = 0
#   player_list = []
#   computer_list = []
#   for i in range(2):
#     layer_c = random.choice(cards)
#     computer_list.append((layer_c))
#     computer += layer_c
#   for i in range(2):
#     layer = random.choice(cards)
#     player_list.append(layer)
#     player += layer
#   print(f"The 2 numbers you have {player_list[0]} and {player_list[1]}")
#   print(f"The computer's number is {computer_list[0]}")
#   is_True = True
#   while is_True:
#     ask_again = input("input 'y' to get another card or 'n' to pass: ")
#     if ask_again == "y":
#
#       layer = random.choice(cards)
#       player_list.append(layer)
#       player += layer
#       print(f"Your cards are {player_list}")
#
#     elif ask_again == "n":
#       print(f"The computer final's card is {computer_list[1]}")
#       while computer < 17:
#         layer_c = random.choice(cards)
#         computer_list.append((layer_c))
#         computer += layer_c
#       print(f"Your total is {player} while the computer's total is {computer}")
#       is_True = False
#   checker()
# else:
#   print("Goodbye")

import random

ask = input("Input yes or no to continue the blackjack game: ")
while ask == "yes":
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer = 0
    player = 0
    dealer_list = []
    player_list = []
    for i in range(2):
        layer_d = random.choice(cards)
        dealer_list.append(layer_d)
        dealer += layer_d
    for i in range(2):
        layer_p = random.choice(cards)
        player_list.append(layer_p)
        player += layer_p
    print(f"The 2 numbers you have {player_list[0]} and {player_list[1]}")
    print(f"The computer's number is {dealer_list[0]}")
    # if player == 21:
    #   print("Blackjack!")
    #   print("You won")
    #   break
    # elif dealer == 21:
    #   print("You lost")
#   #   break
#   isTrue = True
#   while isTrue:
#     print(player_list)
#     extra = input("Do you want an extra card. Input 'y' for yes and 'n' for no. ")
#     if extra == "y":
#       layer = random.choice(cards)
#       player_list.append(layer)
#       player += layer
#       if player > 21:
#         isTrue = False
#     else:
#       isTrue = False
#   if player < 21:
#     while (dealer < 21):
#       if (dealer >= 17) and (dealer < 21):
#         break
#       layer_de = random.choice(cards)
#       dealer_list.append(layer_de)
#       dealer += layer_de
#   print(dealer_list)
#   print(dealer)
#   print(player_list)
#   print(player)
#   if (player < 21) and (player > dealer) :
#     print("You win")
#   elif (player < dealer) and (dealer < 21):
#     print("You lose")
#   elif (player > 21):
#     print("You lose")
#   elif (dealer > 21):
#     print("You win")
#   elif(player == dealer):
#     print("Draw")
#   if player == 21:
#     print("You won")
#   elif dealer == 21:
#     print("You lost")
#   ask = input("Do you want to play again ")
#   if ask == "no":
#     print("End of game")
#     break
#   elif ask == "yes":
#     continue
# print("Bye")


############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
