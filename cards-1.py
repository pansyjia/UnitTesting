# Homework2 - Unit testing
# Siyu Jia

import random
import unittest

# SI 507 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: 009, Monday/4:00 PM - 5:30 PM
# People you worked with:

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p1 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class TestCard(unittest.TestCase):

	# this is a "test"
	# def test_create(self):
	# 	card = Card()
	# 	self.assertEqual(self.card1.suit, "Diamonds")
	# 	self.assertEqual(self.card1.rank, 3)

	'''
	1. Test that if you create a card with rank 12, its rank will be "Queen"
	'''
	def test_one(self):
		c1 = Card(0,12)
		self.assertEqual(c1.rank, "Queen")

	'''
	2.Test that if you create a card with rank 1, its rank will be "Ace"
	'''
	def test_two(self):
		c2 = Card(2,1)
		self.assertEqual(c2.rank, "Ace")

	'''
	3.Test that if you create a card instance with rank 3, its rank will be 3
	'''
	def test_three(self):
		c3 = Card(1,3)
		self.assertEqual(c3.rank_num, 3)

	'''
	4.Test that if you create a card instance with suit 1, it will be suit "Clubs"
	'''
	def test_four(self):
		c4 = Card(1,8)
		self.assertEqual(c4.suit,"Clubs")

	'''
	5.Test that if you create a card instance with suit 2, it will be suit "Hearts"
	'''
	def test_five(self):
		c5 = Card(2,11)
		self.assertEqual(c5.suit,"Hearts")

	'''
	# 6.Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	# '''
	def test_six(self):
		c6 = Card()
		self.assertEqual(c6.suit_names, ["Diamonds","Clubs","Hearts","Spades"])

	'''
	7.Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"
	'''
	def test_seven(self):
		c7 = Card(2,7)
		self.assertEqual(str(c7), "7 of Hearts")

	'''
	8.Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"
	'''
	def test_eight(self):
		c8 = Card(3,13)
		self.assertEqual(str(c8), "King of Spades")

	'''
	9.Test that if you create a deck instance, it will have 52 cards in its cards instance variable
	'''
	def test_nine(self):
		d1 = Deck()
		self.assertEqual(len(d1.cards), 52)

	'''
	10.Test that if you invoke the pop_card method on a deck, it will return a card instance.
	'''
	def test_ten(self):
		d2 = Deck()
		self.assertTrue(type(d2.pop_card())== Card)

	'''
	11. Test that if you invoke the pop_card method on a deck, the deck has one fewer cards in it afterwards.
	'''
	def test_eleven(self):
		d3 = Deck()
		self.assertEqual(len(d3.cards), 52)
		d3.pop_card()
		self.assertEqual(len(d3.cards), 51)

	'''
	12.Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. (This will probably require multiple assertions!)
	'''
	def test_twelve(self):
		self.assertTrue(type(play_war_game(testing=True))== tuple)
		self.assertEqual(len(play_war_game(testing=True)), 3)
		self.assertTrue(type(play_war_game(testing=True)[0])== str)

	'''
	13.(and 14)  Write at least 2 additional tests (not repeats of the above described tests). Make sure to include a descriptive message in these two so we can easily see what you are testing!
	'''
	# 13.Test the replace_card method works as specified
	def test_replace_card(self):
		d = Deck()
		c13 = d.pop_card()
		self.assertEqual(len(d.cards), 51)
		d.replace_card(c13)
		self.assertTrue(c13 in list(d.cards))
		self.assertEqual(len(d.cards), 52)
		d.replace_card(c13)
		self.assertEqual(len(d.cards), 52)

	#14. Test the shuffle method works as specified
	def test_shuffle(self):
		d1 = Deck()
		d2 = d1.cards[:]
		self.assertTrue(d1.cards == d2)
		d1.shuffle()
		self.assertTrue(d1.cards != d2)





################# Part2 ######################
class Hand(object):

	def __init__(self, init_cards):
		self.cards = init_cards

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		return "\n".join(total)

	def add_card(self,card):
		if card not in self.cards:
			self.cards.append(card)

	def remove_card(self,card):
		if card in self.cards:
			return self.cards.remove(card)
		else:
			return None

	def draw(self,deck):
		card = deck.pop_card()
		self.cards.append(card)



class TestHand(unittest.TestCase):

	def test_create(self):
		c_list = [Card(0,1), Card(1,10), Card(2,12)]
		h = Hand(c_list)
		self.assertEqual(h.cards, c_list)

	def testAddAndRemove(self):
		c_list = [Card(0,1), Card(1,10), Card(2,12)]
		h = Hand(c_list)
		c1 = Card(3,13)
		self.assertEqual(h.add_card(c1), c_list.append(c1))
		self.assertEqual(h.remove_card(c1), c_list.remove(c1))

	def test_draw(self):
		c_list = [Card(0,1), Card(1,10), Card(2,12)]
		h = Hand(c_list)
		d = Deck()
		self.assertEqual(len(h.cards), 3)
		self.assertEqual(len(d.cards), 52)
		h.draw(d)
		self.assertEqual(len(h.cards), 4)
		self.assertEqual(len(d.cards), 51)







#############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
