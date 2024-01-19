from game import Game
from card import Card
from deck import Deck
from player import Player

print("\n")
name1 = input("Imię gracza 1: ")
name2 = input("Imię gracza 2: ")
players = [Player(name1), Player(name2)]
print("\n")

while True:
    endgame = input('Naciśnij q, aby zakończyć program lub inny klawisz, aby rozdać karty: ')
    if endgame == 'q':
        break

    print("\n")
    print("Zasady: ")
    print("Wyższa karta wygrywa: " + \
          "2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < Walet < Dama < Król < As")
    print("W razie remisu wygrywa wyższy kolor: " + \
          "Trefl < Karo < Kier < Pik")
    print("\n")

    game = Game(Deck(Card), players)
    game.play_game()

    print("\n")
