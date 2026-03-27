import random

import prompt

from brain_games.games.base_game import BaseGame


# old realization
def check_even(name: str):
	print('Answer "yes" if the number is even, otherwise answer "no".')
	counter = 0
	while counter < 3:
		number = round(random.random() * 100)  # NOSONAR
		result = "yes" if number % 2 == 0 else "no"
		print(f'Question: {number}')
		answer = prompt.string("Your answer: ")
		if result == answer:
			print("Correct!")
			counter += 1
		else:
			print(
				f"'{answer}' is wrong answer ;(. Correct answer was '{result}'."
			)
			print(f"Let's try again, {name}!")
			return
	print(f"Congratulations, {name}!")
	return


class EvenGame(BaseGame):

	NUMBER_RANGE = 100

	def __init__(self) -> None:
		super().__init__()
		self.rules = 'Answer "yes" if the number is even, otherwise answer "no".' # noqa

	def get_question(self) -> int:
		return round(random.random() * self.NUMBER_RANGE)  # NOSONAR
	
	def get_result(self, question) -> str:
		result = "yes" if question % 2 == 0 else "no"
		return result