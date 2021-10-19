import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    # changed to TestCase
    
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card("clubs", 9)
        self.card2 = Card("hearts", 7)
        self.card3 = Card("spades", 2)
        self.cards = (self.card1, self.card2, self.card3)

    def test_card_has_a_suit(self):
        self.assertEqual("clubs", self.card1.suit)

    def test_check_card_for_ace(self):
        self.assertEqual(False,  self.cardgame.check_for_ace(self.card1))

    def test_check_highest_card(self):
        self.assertEqual(self.card1, self.cardgame.highest_card(self.card1, self.card2))

    def test_total_value_of_cards(self):
        self.assertEqual("You have a total of 18", self.cardgame.cards_total(self.cards))