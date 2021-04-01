import random
#Adding both white and black for future development with linked image of highlighted square
black = ["a1","a3","a5","a7","b2","b4","b6","b8","c1","c3","c5","c7","d2","d4","d6","d8","e1","e3","e5","e7","f2","f4","f6","f8","g1","g3","g5","g7","h2","h4","h6","h8"]
white = ["a2","a4","a6","a8","b1","b3","b5","b7","c2","c4","c6","c8","d1","d3","d5","d7","e2","e4","e6","e8","f1","f3","f5","f7","g2","g4","g6","g8","h1","h3","h5","h7"]
colors = ['b','w']

def squareQuestionnaire():
	color = colors[random.randint(0,1)]
	if color == 'b':
		square = black[random.randint(0,31)] # 64 squares on chess board, half white and half black so 32
	else:
		square = white[random.randint(0,31)]

	print(square)
	response = input("Black or White? (b/w)\n")
	if response == color:
		print(u'\u2705'+"Correct\n\n")
	else:
		print(u'\u274C'"Wrong\n\n")
	squareQuestionnaire()

def main():
	print("\n\n\n\n\n\n\n\n\n\n")
	squareQuestionnaire()
			
if __name__ == "__main__":
	main()
