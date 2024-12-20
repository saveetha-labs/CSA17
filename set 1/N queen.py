N = 4
def solve_queen(board,col):
	if col==N:
		print_board(board)
		return True
	for i in range(N):
		if is_safe(board,i,col):
			board[i][col]=1
			if solve_queen(board,col + 1):
				return True
			board[i][col]=0
	return False
def is_safe(board,row,col):
	for x in range(col):
		if board[row][x]==1:
			return False
	for x, y in zip(range(row,-1,-1),range(col,-1,-1)):
		if board[x][y] == 1:
			return False
	for x,y in zip(range(row,N,1),range(col,-1,-1)):
		if board[x][y] == 1:
			return False
	return True
def print_board(board):
	for row in board:
		for col in row:
			print(col,end=" ")
		print()
board = [[0 for i in range(N)] for i in range(N)]
if not solve_queen(board,0):
	print("NO SOLUTION")