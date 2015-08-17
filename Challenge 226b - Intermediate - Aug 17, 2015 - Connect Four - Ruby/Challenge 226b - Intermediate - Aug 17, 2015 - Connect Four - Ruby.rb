def checkMoveAcross(c,r,n,board)
	total = 1
	pos = [[c,r]]
	for i in 1..3
		if(c+i<board.length && board[c+i][r] == n && total<4)
			total+=1
			pos << [c+i,r]
		end
		if(c-i>=0 && board[c-i][r]==n && total<4)
			total+=1
			pos << [c-i,r]
		end
	end
	return pos
end

def checkMoveDown(c,r,n,board)
	total = 1
	pos = [[c,r]]
	for i in 1..3
		if(r-i>=0 && board[c][r-i] == n)
			total+=1
			pos << [c,r-i]
		end
	end
	return pos
end

def checkMoveDiagonalOne(c,r,n,board)
	total = 1
	pos = [[c,r]]
	for i in 1..3
		if(c+i<board.length && i+r<6 && board[c+i][r+i]==n && total<4)
			total+=1
			pos << [c+i,r+i]
		end
		if(c-i>=0 && r-i>=0 && board[c-i][r-i]==n && total<4)
			total+=1
			pos << [c-i,r-i]
		end
	end
	return pos
end

def checkMoveDiagonalTwo(c,r,n,board)
	total = 1
	pos = [[c,r]]
	for i in 1..3
		if(c-i>=0 && i+r<6 && board[c-i][r+i]==n && total<4)
			total+=1
			pos << [c-i,r+i]
		end
		if(c+i<board.length && r-i>=0 && board[c+i][r-i]==n && total<4)
			total+=1
			pos << [c+i,r-i]
		end
	end
	return pos
end

def makeMove(alpha,board,moves)
	col = ["a","b","c","d","e","f","g"]
	c = col.index(alpha.downcase)
	winText = alpha == alpha.upcase ? "X won at move #{moves} (with " : "O won at move #{moves} (with "
	pos = 1
	n = 1
	for r in 0..5
		if(board[c][r]!=0)
			pos+=1
		elsif(alpha == alpha.upcase)
			board[c][r] = n
			break
		else
			n = 2
			board[c][r] = n
			break
		end
	end
	if((pos = checkMoveAcross(c,r,n,board)).length==4)
		winningMoves = "#{col[pos[0][0]]}#{pos[0][1]+1} #{col[pos[1][0]]}#{pos[1][1]+1} #{col[pos[2][0]]}#{pos[2][1]+1} #{col[pos[3][0]]}#{pos[3][1]+1})"
		puts(winText+winningMoves)
		return true
	elsif((pos = checkMoveDown(c,r,n,board)).length==4)
		winningMoves = "#{col[pos[0][0]]}#{pos[0][1]+1} #{col[pos[1][0]]}#{pos[1][1]+1} #{col[pos[2][0]]}#{pos[2][1]+1} #{col[pos[3][0]]}#{pos[3][1]+1})"
		puts(winText+winningMoves)
		return true
	elsif((pos = checkMoveDiagonalOne(c,r,n,board)).length==4)
		winningMoves = "#{col[pos[0][0]]}#{pos[0][1]+1} #{col[pos[1][0]]}#{pos[1][1]+1} #{col[pos[2][0]]}#{pos[2][1]+1} #{col[pos[3][0]]}#{pos[3][1]+1})"
		puts(winText+winningMoves)
		return true
	elsif((pos = checkMoveDiagonalTwo(c,r,n,board)).length==4)
		winningMoves = "#{col[pos[0][0]]}#{pos[0][1]+1} #{col[pos[1][0]]}#{pos[1][1]+1} #{col[pos[2][0]]}#{pos[2][1]+1} #{col[pos[3][0]]}#{pos[3][1]+1})"
		puts(winText+winningMoves)
		return true
	else
		return false
	end
end

player1Moves = []
player2Moves = []
board = []
for i in 0..6
	board << [0,0,0,0,0,0]
end
File.open("input.txt") do |f|
	f.each_line do |moves|
		player1Moves << moves[0]
		player2Moves << moves[3]
	end
end

for i in 0..player1Moves.length-1
	if(makeMove(player1Moves[i],board,i+1))
		break
	elsif(makeMove(player2Moves[i],board,i+1))
		break
	end
end