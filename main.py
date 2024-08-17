# the first thing is to build the logic and then chunck it into different blocks
# The game has a state at every turn represented by the list below. 
#THe game will also have a winning state or conditions for winning the game. 8 winning possiblities 
""" How can we represent all the possibilities
SUm of all indices where a character is."""
class Game:
    def __init__(self):
        self.p = ["_","_","_","_","_","_"," "," "," "]
    
    def board_display(self):
     # lets treat these as a possibilities or one scenerio.
    
        print(f"""_{self.p[0]}_|_{self.p[1]}_|_{self.p[2]}_
_{self.p[3]}_|_{self.p[4]}_|_{self.p[5]}_
 {self.p[6]} | {self.p[7]} | {self.p[8]}""")
class Player:
    def __init__(self):
        self.character = ""


def game_loop():
    tictactoe = Game()
    game_play = True
    tictactoe.board_display()
    player_one = Player()
    player_two = Player()
#     print("""__|__|__
# __|__|__
#   |  |""")

#     print("""  |  |
# ----------
#   |  |  
# ---------
#   |  |""")
    player_one.character = input("Please select a character for player 1: o , x ")
    if (player_one.character == "o"):
        player_two.character = "x"
    else:
        player_two.character = "o"

    print(f"{player_one.character},  {player_two.character}")
#implemting the character display on the grid
    while(game_play):
        x = input("enter the position number to enter the mark [1-9]");
        if (x == "q"):
            game_play = False
        if(tictactoe.p[x] == " " or tictactoe.p[x] == "_"):
            # here we will write a logic to decide whose turn is now. and based on that we will use the player.character
            # to display the character in particular location.
            # what can we do to track the turns.
            # use a flag to indicate the turn or use the player character as an indication of turn
            # lets say in a multiplayer game we can set the variable to the characters respective value. and use it to 
            # display active character.



#Player implementation. What does a player do? what are some of the actions that a player can take it is always a player.vs player
if __name__ == "__main__":
    print("Welcome to the main screen for tictactoe")
    game_loop()
    
   