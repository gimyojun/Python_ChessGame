#print(u'\u2654') whiteking
def PrintBoard():
	#보드 출력
	print('    a   b   c   d   e   f   g   h')
	print('  ' + chr(9472) * 16 + '  ', end='')
	print()
	for i in range(0,8):
		print (8-i,'|', end='')
		for j in range(0, 8):
			if board[i][j] != '.':
				print(' ' + realPiece[charPiece.index(board[i][j])], end='|')
			else:
				print('   ', end='|')
			#print (board[i][j], end='|')
		print(" {}".format(8-i))
		print('  ' + chr(9472) * 16 + '  ', end='')
		print()
	print('    a   b   c   d   e   f   g   h')

def isChecked(turnColor):
	#흰색 == 0, 검정색 == 1
	if turnColor == 0:
		king = 'K'
		enemyPiece = 'prnbqk'
		enemyking =  'k'
	else:
		king = 'k'
		enemyPiece = 'PRNBQK'
		enemyking =  'K'
	
	enemyLocationList = []
	existking = 0
	for i in range(8): 
		for j in range(8):
			if board[i][j] == king:
				kingrow = i
				kingcol = j
			if board[i][j] in enemyPiece:
				enemyLocationList.append([i,j])
			if board[i][j] == enemyking:
				existking =1
	if existking== 0:
		print('승리하였습니다!')
		exit(0)
				
	for enemyLocation in enemyLocationList:
		if CanMove(enemyLocation[0], enemyLocation[1], kingrow, kingcol) == True:
			return True
	return False																																			 

	

def InputMoving(turnColor):
	#흰색 == 0, 검정색 == 1
	while True:
		print('이동 할 말의 위치 : ')
		frominput = input()
		fromBoardrow = rowline.index(frominput[1])
		fromBoardcol = colline.index(frominput[0])
		fromPiece = board[fromBoardrow][fromBoardcol]
		if fromPiece.islower() == turnColor and fromPiece != '.':
			print('이동 할 위치 : ')
			toinput = input()
			moving = [frominput, toinput]
			return moving
		else:
			print('자신의 말이 아닙니다')



def Move(moving):
	fromBoardrow = rowline.index(moving[0][1])
	fromBoardcol = colline.index(moving[0][0])
	toBoardrow = rowline.index(moving[1][1])
	toBoardcol = colline.index(moving[1][0])
	fromPiece = board[fromBoardrow][fromBoardcol]
	toPiece = board[toBoardrow][toBoardcol]

	if CanMove(fromBoardrow, fromBoardcol, toBoardrow, toBoardcol) == True:
		board[toBoardrow][toBoardcol] = fromPiece
		board[fromBoardrow][fromBoardcol] = '.'
		isChecked(turnColor)
		#if isChecked(turnColor) == True :
			#print('킹이 죽습니다.')
			#board[toBoardrow][toBoardcol] = toPiece
			#board[fromBoardrow][fromBoardcol]= fromPiece
		return True
	else:
		print('잘못된 이동')
		return False

def CanMove(fromBoardrow, fromBoardcol, toBoardrow, toBoardcol):
	fromPiece = board[fromBoardrow][fromBoardcol]
	toPiece = board[toBoardrow][toBoardcol]
	
	isenemy = 0
	if fromPiece.isupper() != toPiece.isupper():
		isenemy = 1
	
	if fromPiece == 'p':
		#검정 폰
		if fromBoardrow + 1 == toBoardrow and fromBoardcol == toBoardcol and toPiece =='.':
			#폰은 한칸 앞으로 전진 가능
			return True
		if fromBoardrow == 1 and fromBoardrow + 2 == toBoardrow and toPiece == '.':
			#맨 처음 폰은 두칸 전진 가능
			return True
		if fromBoardrow + 1 == toBoardrow and (fromBoardcol + 1 == toBoardcol or fromBoardcol - 1 == toBoardcol) and isenemy == True:
			#상대 말을 대각 이동으로 먹기 가능
			return True
		
	if fromPiece == 'P':
		#흰색 폰
		if fromBoardrow - 1 == toBoardrow and fromBoardcol == toBoardcol and toPiece =='.':
			#폰은 한칸 앞으로 전진 가능
			return True
		if fromBoardrow == 6 and fromBoardrow - 2 == toBoardrow and toPiece == '.':
			#맨 처음 폰은 두칸 전진 가능
			return True
		if fromBoardrow - 1 == toBoardrow and (fromBoardcol + 1 == toBoardcol or fromBoardcol - 1 == toBoardcol) and isenemy == True:
			#상대 말을 대각 이동으로 먹기 가능
			return True
		
	elif fromPiece == 'r' or fromPiece == 'R':
		#룩
		if (fromBoardrow == toBoardrow or fromBoardcol == toBoardcol) and (toPiece == '.' or isenemy == True):
			#룩은 같은 행이나 같은 열로 이동 가능
			if RBPath(fromBoardrow, fromBoardcol, toBoardrow, toBoardcol):
				return True
	
	elif fromPiece == 'n' or fromPiece == 'N':
		#나이트
		rowDifference = abs(fromBoardrow - toBoardrow)
		colDifference = abs(fromBoardcol - toBoardcol)
		if toPiece == '.' or isenemy == True:
		#나이트는 행 2칸 열1칸 또는 행 1칸 열 2칸 이동 가능
			if rowDifference == 2 and colDifference == 1:
				return True
			if rowDifference == 1 and colDifference == 2:
				return True
	
	elif fromPiece == 'b' or fromPiece == 'B':
		#비숍
		if ( abs(fromBoardrow - toBoardrow) == abs(fromBoardcol - toBoardcol)) and (toPiece == '.' or isenemy == True):
			#비숍은 대각선으로 이동 가능
			if RBPath(fromBoardrow, fromBoardcol, toBoardrow, toBoardcol):
				return True
			
	elif fromPiece == 'q' or fromPiece == 'Q':
		#퀸
		if (fromBoardrow == toBoardrow or fromBoardcol == toBoardcol) and (toPiece == '.' or isenemy == True):
			#룩과 같은 이동 가능
			if RBPath(fromBoardrow, fromBoardcol, toBoardrow, toBoardcol):
				return True
		if ( abs(fromBoardrow - toBoardrow) == abs(fromBoardcol - toBoardcol)) and (toPiece == '.' or isenemy == True):
			#비숍은 대각선으로 이동 가능
			if RBPath(fromBoardrow, fromBoardcol, toBoardrow, toBoardcol):
				return True
			
	elif fromPiece == 'k' or fromPiece == 'K':
		#킹
		rowDifference = abs(fromBoardrow - toBoardrow)
		colDifference = abs(fromBoardcol - toBoardcol)
		if toPiece == '.' or isenemy == True:
			if rowDifference == 0 and colDifference == 1:
				return True
			elif rowDifference == 1 and colDifference == 0:
				return True
			elif rowDifference == 1 and colDifference == 1:
				return True
			
	return False

def RBPath(fromBoardraw, fromBoardcol, toBoardraw, toBoardcol):
	#룩과 비숍의 움직이는 경로
	if abs(fromBoardraw - toBoardraw) <= 1 and abs(fromBoardcol - toBoardcol) <= 1:
		return True
	else:
	#룩
		if fromBoardraw < toBoardraw and fromBoardcol == toBoardcol:
			fromBoardraw = fromBoardraw + 1
		elif fromBoardraw > toBoardraw and fromBoardcol == toBoardcol:
			fromBoardraw = fromBoardraw - 1
		elif fromBoardraw == toBoardraw and fromBoardcol < toBoardcol:
			fromBoardcol = fromBoardcol + 1
		elif fromBoardraw == toBoardraw and fromBoardcol > toBoardcol:
			fromBoardcol = fromBoardcol - 1
	#비숍
		elif fromBoardraw < toBoardraw and fromBoardcol < toBoardcol:
			fromBoardraw = fromBoardraw + 1
			fromBoardcol = fromBoardcol + 1
		elif fromBoardraw > toBoardraw and fromBoardcol < toBoardcol:
			fromBoardraw = fromBoardraw - 1
			fromBoardcol = fromBoardcol + 1
		elif fromBoardraw < toBoardraw and fromBoardcol > toBoardcol:
			fromBoardraw = fromBoardraw + 1
			fromBoardcol = fromBoardcol - 1
		elif fromBoardraw > toBoardraw and fromBoardcol > toBoardcol:
			fromBoardraw = fromBoardraw - 1
			fromBoardcol = fromBoardcol - 1

	if board[fromBoardraw][fromBoardcol] != '.':
		return False
	else:
		return RBPath(fromBoardraw, fromBoardcol, toBoardraw, toBoardcol)

global board
board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
			 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
			 ['.','.','.','.','.','.','.','.'],
			 ['.','.','.','.','.','.','.','.'],
			 ['.','.','.','.','.','.','.','.'],
			 ['.','.','.','.','.','.','.','.'],
			 ['P','P','P','P','P','P','P','P'],
			 ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]


global rowline
rowline = ['8','7','6','5','4','3','2','1']
global colline
colline = ['a','b','c','d','e','f','g','h']
global realPiece
realPiece = ''.join(chr(9812 + x) for x in range(12))
global charPiece
charPiece = 'KQRBNPkqrbnp'

turnColor = 1
#흰 색 차례 == 0, 검정 색 차례 == 1

while True:
	PrintBoard()
	turnColor = not turnColor
	while True:
		moving = InputMoving(turnColor)
		if Move(moving) == True:
			break
