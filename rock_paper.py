import random


def play():
	user = input(" 'r' for rock,'p' for paper , 's' for scissors")
	computer = random.choice(['r','p','s'])


	if user == computer:
		return "it's a tie"

	#r > s , s>p, p>r

	if is_win(user,computer):
		return "you have won"


	return "you have lost!"


def is_win(player,opponent):
	if( player== 'r' and opponent == 's') or ( player == 's' and opponent == 'p') or ( player == 'p' and opponent =='r'):
		return true



		

