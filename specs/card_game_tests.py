import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.Testcase):
    
    def setUp(self):
        self.card1 = Card("clubs", 9)
        self.card2 = Card("hearts", 7)
        self.card3 = Card("spades", 2)

    def test_check_card_for_ace(self):
        self.asserEqual(False,  self.card.check_for_ace())

    def test_check_highest_card(self):
        self.asserEqual(card1, self.card.highest_card())

    def test_total_value_of_cards(self):
        self.assertEqual(18, self.card.cards_total(cards))