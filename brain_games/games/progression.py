import random

from brain_games.games.base_game import BaseGame


class ProgressionGame(BaseGame):

	INIT_RANGE = 10
	STEP_RANGE = 10
	PROGRESSION_MIN_LENGTH = 5
	PROGRESSION_LENGTH_RANGE = 5

	def __init__(self) -> None:
		super().__init__()
		self.rules = 'What number is missing in the progression?'

	def get_question(self) -> str:
		progression_length = round(
			random.random() * self.PROGRESSION_LENGTH_RANGE  # NOSONAR
		) + self.PROGRESSION_MIN_LENGTH
		init = round(random.random() * self.INIT_RANGE) + 1  # NOSONAR
		step = round(random.random() * self.STEP_RANGE) + 1  # NOSONAR
		self.element_num = round(
			random.random() * (progression_length - 1)  # NOSONAR
		)
		self.progression = [
			str(init + step * elem) for elem in range(progression_length)
		]
		question_first = " ".join(self.progression[:self.element_num])
		question_second = " ".join(self.progression[self.element_num + 1:])
		return f"{question_first} .. {question_second}"
	
	def get_result(self, question) -> str:
		result = self.progression[self.element_num]
		return str(result)