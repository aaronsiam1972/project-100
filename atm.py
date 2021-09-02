class Card(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    def cn(self):
        print(self.card_number)
    
    def pn(self):
        print(self.pin_number)
    


Carter = Card("1928887675567235", "3347")
Kazi = Card("5656543456787656", "5891")
Chris = Card("4567776587945365", "7771")
Alex = Card("2873986577019287", "6715")
Reece = Card("4517698978256327", "1345")

Carter.pn()
