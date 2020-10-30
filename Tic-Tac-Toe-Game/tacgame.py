"""Board
   display board
   play game
   hundle turn
   check win
     check rows
     check diagnols
   check tie
   flip player
"""""
row=[]
columns=[]
diagnal=[]
win=[]
tie=[]
player1="Circle"
player2="Cross"

def display_board(board):
  return (board)
playing_board=display_board(["box1","box2","box3",
"box3","box4","box5","box6","box7","box8","box9"])
print(playing_board)

def play_game():
  display_board()
  start=row.append(playing_board[1])
  print("Box Marked")
  
def flip_player():


