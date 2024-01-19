class Game:
    def __init__(self, deck, players):
        self.deck = deck
        self.player1 = players[0]
        self.player2 = players[1]


    def wins(self, winner):
        win = "Tę rundę wygrywa {}!"
        win = win.format(winner)
        print(win)


    def draw(self, player1_card, player2_card):
        draw_cards = "{}: wyciągnął {} - {}: wyciągnął {}."
        draw_cards = draw_cards.format(self.player1.name, player1_card, self.player2.name, player2_card)
        print(draw_cards)


    def winner(self):
        winner_is = "Jest remis!"

        if self.player1.wins > self.player2.wins:
            winner_is = self.player1.name

        if self.player1.wins < self.player2.wins:
            winner_is = self.player2.name

        return winner_is


    def play_game(self):
        cards = self.deck.cards

        print("Zaczynamy rozgrywkę!")

        while len(cards) >= 2:
            message = "\nNaciśnij q, aby zakończyć grę " + \
                      "lub inny klawisz, aby kontynuować grę: "
            response = input(message)

            if response == 'q':
                break

            print("\n")

            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()

            self.draw(player1_card, player2_card)

            if player1_card > player2_card:
                self.player1.wins += 1
                self.wins(self.player1.name)
            else:
                self.player2.wins += 1
                self.wins(self.player2.name)

        win = self.winner()

        print("\nWojna zakończona - Wygrał {}!".format(win))