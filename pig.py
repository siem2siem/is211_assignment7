#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment7 - A simple game called Pig - Tested in Python 2.7.15"""

import random

class Player():
	def __init__(self):
		self.turn = False
		self.roll = True
		self.hold = False
		self.score = 0

	def choose(self):
		decision = raw_input('%s: Hold (h) or Roll (r)? ' % self.name)
		decision = str(decision)
		if decision == 'h':
			self.hold = True
			self.roll = False
		elif decision == 'r':
			self.hold = False
			self.roll = True
		else:
			print
			print('Please choose h to Hold or r to Roll')
			self.choose()

class Die():
	def __init__(self):
		self.value = int()
	def roll(self):
		self.value = random.randint(1,6)

class Game():
	def __init__(self,player1,player2,die):
		self.turn_score = 0
		self.die = die
		self.player1 = player1
		self.player2 = player2
		self.player1.score = 0
		self.player2.score = 0
		self.player1.name = "Player 1"
		self.player2.name = "Player 2"


		coin = random.randint(1,2)
		if coin == 1:
			self.current_player = player1
			print "Player 1 has been randomly selected to roll first."
		else:
			self.current_player = player2
			print "Player 2 has been randomly selected to roll first."
		self.turn()

	def next_turn(self):
		self.turn_score = 0
		if self.player1.score >= 100:
			print "*************************************************************"
			print "Player 1 has reached a score of 100 or more and won the game!"
			print "*************************************************************"
			print
			print "Player 1 final score is:",self.player1.score
			print
			print "Player 2 final score is:",self.player2.score
			self.endgame()
			startNewGame()
		elif self.player2.score >= 100:
			print "*************************************************************"
			print "Player 2 has reached a score of 100 or more and won the game!"
			print "*************************************************************"
			print
			print "Player 2 final score is:",self.player2.score
			print
			print "Player 1 final score is:",self.player1.score            
			self.endgame()
			startNewGame()
		else:
			if self.current_player == self.player1:
				self.current_player = self.player2
			elif self.current_player == self.player2:
				self.current_player = self.player1
			print
			print "********************************************************"
			print "Please switch player.  Active player is now:  ", self.current_player.name
			print "********************************************************"
			print         
			self.turn()

	def turn(self):
		print "Player 1 Score:", self.player1.score
		print
		print "Player 2 Score:", self.player2.score
		print
		self.die.roll()
		if(self.die.value == 1):
			print "You have rolled a 1.  Sorry no points will be added and you lose your turn."
			self.turn_score = 0
			self.next_turn()
		else:
			self.turn_score = self.turn_score + self.die.value
			print "You have rolled a:",self.die.value
			print       
			print "Current turn score is:", self.turn_score
			self.current_player.choose()
			if(self.current_player.hold == True and self.current_player.roll == False):
				self.current_player.score = self.current_player.score + self.turn_score
				self.next_turn()
			elif(self.current_player.hold == False and self.current_player.roll == True):
				self.turn()
	def endgame(self):
		self.player1 = None
		self.player2 = None
		self.die = None
		self.turn_score = None

def startNewGame():
	start = raw_input("Do you want to start a new game? Y = Yes or type any key to exit?  ")

	if start == 'Y' or start == 'y':
		player1 = Player()
		player2 = Player()
		die = Die()
		startgame = Game(player1,player2,die)
        
        else:
            print
            print "Thank you for playing. "
            print
            print "The game will now exit. "
        
startNewGame()
