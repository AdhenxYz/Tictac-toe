board = ["-","-","-",
        "-","-","-",
        "-","-","-", ] 


# if game is still going
game_still_going = True

# who won? or lose?
winner = None

#  who turn is it
current_player = 'X'

# Display Board 
def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# Play the game
def play_games():

  # display board
  display_board()

# when game si still going
  while game_still_going:
   
    # handle a single turn of an arbitrary player
    handle_turn(current_player)
   
    #  check if teh game has ended
    check_if_game_over()

    # Flip to other Player
    flip_player()


# the game has end
  if winner == 'X' or winner == 'O':
    print(winner + " Won.")
  elif winner == None:
    print('Lose.')

# Handle turn player
def handle_turn(player):
  print(player + "'s. turn.'")
  position = input("Choose a position from 1-9: ")
  
  valid = False
  while not valid:

    while position not in ['1', '2', '3', '4', '5', '6', '7', '8','9']:
      position = input("Choose a Position from 1-9: ")


    position = int(position) - 1

    if board[position] == '-':
      valid = True
    else:
      print("you cant go there. Go again.")


  board[position] = player
  display_board()

def check_if_game_over():
  check_if_winner()
  check_if_lose()

def check_if_winner():
  # set up global variable
  global winner
  # check rows
  row_winner = check_rows()
  # Check coloums
  coloums_winner = check_coloums()
  # check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif coloums_winner:
    winner = coloums_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


def check_rows():
  # set Up global variable
  global game_still_going
  # check if the rows have all the same value
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # if any row does have a match, flag taht theere is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # return the winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6] 
  return

def check_coloums():
  # set Up global variable
  global game_still_going
  # check if the rows have all the same value
  coloum_1 = board[0] == board[3] == board[6] != "-"
  coloum_2 = board[1] == board[4] == board[7] != "-"
  coloum_3 = board[2] == board[5] == board[8] != "-"
  # if any row does have a match, flag taht theere is a win
  if coloum_1 or coloum_2 or coloum_3:
    game_still_going = False
  # return the winner (X or O)
  if coloum_1:
    return board[0]
  elif coloum_2:
    return board[1]
  elif coloum_3:
    return board[2] 
  return


def check_diagonals():
  # set Up global variable
  global game_still_going
  # check if the rows have all the same value
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  # if any row does have a match, flag taht theere is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # return the winner (X or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6] 
  return

def check_if_lose():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  global current_player
  if current_player == 'X':
    current_player = 'O'
  elif current_player == 'O':
    current_player = 'X'
  return

play_games()

# board
# display board
# play game
# check win
  # check rows
  # check columns
  # check diagonals
# check tie
# flip player