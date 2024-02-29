print("Welcome to Tic Tac Toe")
print("----------------------")

gameBoard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
rows = 3
cols = 3

def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(cols):
      print("", gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

def modifyArray(num, turn):
  num -= 1
  if num == 0:
    gameBoard[0][0] = turn
  elif num == 1:
    gameBoard[0][1] = turn
  elif num == 2:
    gameBoard[0][2] = turn
  elif num == 3:
    gameBoard[1][0] = turn
  elif num == 4:
    gameBoard[1][1] = turn
  elif num == 5:
    gameBoard[1][2] = turn
  elif num == 6:
    gameBoard[2][0] = turn
  elif num == 7:
    gameBoard[2][1] = turn
  elif num == 8:
    gameBoard[2][2] = turn

### Define function to check for a winner
def checkForWinner(gameBoard):
  for i in range(3):
    # Check rows
    if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] and gameBoard[i][0] != ' ':
      print(f"{gameBoard[i][0]} has won!")
      return gameBoard[i][0]
    # Check columns
    if gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i] and gameBoard[0][i] != ' ':
      print(f"{gameBoard[0][i]} has won!")
      return gameBoard[0][i]
  # Check diagonals
  if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] and gameBoard[0][0] != ' ':
    print(f"{gameBoard[0][0]} has won!")
    return gameBoard[0][0]
  if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] and gameBoard[0][2] != ' ':
    print(f"{gameBoard[0][2]} has won!")
    return gameBoard[0][2]
  return "N"


leaveLoop = False
turnCounter = 0

while not leaveLoop:
  printGameBoard()
  # It's the player's turn
  if turnCounter % 2 == 0:
    marker = 'X'
  else:
    marker = 'O'
  numberPicked = int(input(f"\nPlayer {marker}, choose a number [1-9]: "))
  if numberPicked in range(1, 10) and gameBoard[(numberPicked - 1) // 3][(numberPicked - 1) % 3] == ' ':
    modifyArray(numberPicked, marker)
    turnCounter += 1
  else:
    print("Invalid input. Please try again.")
  
  winner = checkForWinner(gameBoard)
  if winner != "N":
    print("\nGame over! Thank you for playing :)")
    printGameBoard()
    break
  # Check for a tie after checking for a winner
  if turnCounter == 9 and winner == "N":
    print("\nIt's a tie! Thank you for playing :)")
    printGameBoard()
    break

