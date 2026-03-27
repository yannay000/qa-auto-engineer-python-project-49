import random
from brain_games.games.base_game import BaseGame

class GcdGame(BaseGame):

	NUMBER_RANGE = 100

	def __init__(self) -> None:
		super().__init__()
		self.rules = 'Find the greatest common divisor of given numbers.'

	def get_question(self) -> str:
		first_number = round(random.random() * self.NUMBER_RANGE) + 1 # NOSONAR
		second_number = round(random.random() * self.NUMBER_RANGE) # NOSONAR
		return f"{first_number} {second_number}"
	
	def get_nod(self, first: int, second: int) -> int:
		if second == 0:
			return first
		else:
			old_first = first
			first = second
			second = old_first % second
			return self.get_nod(first=first, second=second)

	
	def get_result(self, question) -> str:
		question_list = question.split()
		result = self.get_nod(int(question_list[0]), int(question_list[1]))
		return str(result)