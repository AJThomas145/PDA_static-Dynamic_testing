from src.card import Card
# added src to card.py

### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:

  # def __init__(self):

# below should be == and not =, it should be else:,
  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False
   
# dif should be def, should have , after card1 argument,
# indent 2nd-5th line of method, return card 1 not just card
  def highest_card(self, card1, card2):
    if card1.value > card2.value:
      return card1
    else:
      return card2
  

# 1st - 4th line should be indented, total isnt set to anything(should be = 0)
# change total to str as unable to concantenate string and int
  def cards_total(self, cards):
    total = 0
    for card in cards:
      total += card.value
    return "You have a total of " + str(total)