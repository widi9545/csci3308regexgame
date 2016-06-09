class player:
	
	score = 0
	
	def __init__(self):
		self.score = 0
	
	def addScore(self):
		Player = self
		Player.score += 1
		return Player.score
			
	def printScore(self):
		Player = self
		print("The score of the player is: ", Player.score)
		return Player.score
				

	
