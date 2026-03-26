from brain_games.cli import welcome_user
from brain_games.even import check_even

def main():
	name = welcome_user()
	check_even(name)
