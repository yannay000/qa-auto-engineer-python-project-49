import prompt
import random

def check_even(name: str):
	print('Answer "yes" if the number is even, otherwise answer "no".')
	counter = 0
	while counter < 3:
		number = round(random.random() * 100)
		result = "yes" if number % 2 == 0 else "no"
		print(f'Question: {number}')
		answer = prompt.string("Your answer: ")
		if result == answer:
			print("Correct!")
			counter+=1
		else:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
			print(f"Let's try again, {name}!")
			return
	print(f"Congratulations, {name}!")
	return