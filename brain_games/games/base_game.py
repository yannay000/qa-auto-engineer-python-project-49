import prompt

from brain_games.cli import welcome_user


class BaseGame:

	STEPS_COUNT = 3

	def __init__(self) -> None:
		self.user_name = ""
		self.rules = ""
		self.counter = 0

	def start_game(self):
		self.user_name = welcome_user()
		print(self.rules)

	def get_question(self):
		raise NotImplementedError
	
	def get_result(self, question: str | int) -> str:
		raise NotImplementedError

	def game_step(self) -> bool:
		question = self.get_question()
		result = self.get_result(question)
		print(f'Question: {question}')
		answer = prompt.string("Your answer: ")
		if result == answer:
			self.success_step()
			return True
		else:
			self.failed_game(answer, result)
			return False

	def success_step(self):
		print("Correct!")
		self.counter += 1

	def failed_game(self, answer, result):
		print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
		print(f"Let's try again, {self.user_name}!")

	def end_game(self):
		print(f"Congratulations, {self.user_name}!")

	def process_game(self):
		self.start_game()
		while self.counter < self.STEPS_COUNT:
			if not self.game_step():
				return
		return self.end_game()