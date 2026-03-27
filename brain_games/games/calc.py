import random
from brain_games.games.base_game import BaseGame

class CalcGame(BaseGame):

	SIGNS = ["+", "-", "*"]

	def __init__(self) -> None:
		super().__init__()
		self.rules = 'What is the result of the expression?'

	def get_question(self) -> str:
		first_number = round(random.random() * 100) # NOSONAR
		second_number = round(random.random() * 100) # NOSONAR
		sign = random.choice(self.SIGNS)
		return f"{first_number} {sign} {second_number}"
	
	def get_result(self, question) -> str:
		question_list = question.split()
		if question_list[1] == "+":
			result = int(question_list[0]) + int(question_list[2])
		elif question_list[1] == "-":
			result = int(question_list[0]) - int(question_list[2])
		else:
			result = int(question_list[0]) * int(question_list[2])
		return str(result)