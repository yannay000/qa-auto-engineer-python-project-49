import random
from brain_games.games.base_game import BaseGame

class PrimeGame(BaseGame):

	NUMBER_RANGE = 100

	def __init__(self) -> None:
		super().__init__()
		self.rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'

	def get_question(self) -> int:
		return round(random.random() * self.NUMBER_RANGE) + 1 # NOSONAR
	
	def check_prime(self, number: int) -> bool:
		# if number <= 1: return False
		if number in (1, 2): 
			return True
		elif number % 2 == 0: 
			return False
		for i in range(3, int(number**0.5) + 1, 2):
			if number % i == 0: 
				return False
		return True
	
	def get_result(self, question: int) -> str:
		result = "yes" if self.check_prime(question) else "no"
		return result