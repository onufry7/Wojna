from random import shuffle

class Deck:
    def __init__(self, card):
        self.cards = []
        self.card = card

        for i in range(2, 15):
            for j in range(4):
                self.cards.append(self.card(i,j))

        shuffle(self.cards)


    def remove_card(self):
        if len(self.cards) == 0:
            return
        
        return self.cards.pop()
