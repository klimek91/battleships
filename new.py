from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship1_row = random_row(board)
ship1_col = random_col(board)
print ('Ship1 row and col: ',ship1_row,ship1_col)

while True:
  ship2_row = random_row(board)
  ship2_col = random_row(board)
  if ship2_row != ship1_row and ship2_col != ship1_col:
    break
  
print("Ship2 row and col: ",ship2_row,ship2_col)

for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship1_row and guess_col == ship1_col or guess_row == ship2_row and guess_col == ship2_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print("Game Over")
    print_board(board)