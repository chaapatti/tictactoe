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
        
    def winning_cases(self, c):
        if (self.p[0] == self.p[1] == self.p[2] == c):
            return c  # these are the winning cases that we have to check for player.
        elif (self.p[3] == self.p[4] == self.p[5] == c):
            return c
        elif (self.p[6] == self.p[7] == self.p[8] == c):
            return c
        elif (self.p[0] == self.p[3] == self.p[6] == c):
            return c
        elif (self.p[1] == self.p[4] == self.p[7] == c):
            return c
        elif (self.p[2] == self.p[5] == self.p[8] == c):
            return c
        elif (self.p[0] == self.p[4] == self.p[8] == c):
            return c
        elif (self.p[6] == self.p[4] == self.p[2] ==c):
            return c
        else:
            return ""
    
    def switch_player(self, plyr):
        if (plyr == "o"):
            return "x"
        else:
            return "o"

class Player:
    def __init__(self):
        self.character = ""
        

def game_loop():
    tictactoe = Game()
    game_play = True
    tictactoe.board_display()
    player_one = Player()
    player_two = Player()

    player_one.character = input("Please select a character for player 1: o , x ")
    if (player_one.character == "o"):
        player_two.character = "x"
    else:
        player_two.character = "o"

    print(f"{player_one.character},  {player_two.character}")
    #implemting the character display on the grid
    plyr = player_one.character
    while(game_play):
        
        
        x = int(input("enter the position number to enter the mark [1-9]"))
        if (x == "q"):
            game_play = False
        if (x > 9):
            print("index out of reach")
        else:
            if(tictactoe.p[x] == " " or tictactoe.p[x] == "_"):
                # here we will write a logic to decide whose turn is now. and based on that we will use the player.character
                # to display the character in particular location.
                # what can we do to track the turns.
                # use a flag to indicate the turn or use the player character as an indication of turn
                # lets say in a multiplayer game we can set the variable to the characters respective value. and use it to 
                # display active character.
                tictactoe.p[x]= plyr
                winning_result = tictactoe.winning_cases(plyr)
                if(winning_result == "o"):
                    print("player one is winner")
                    break
                elif(winning_result == "x"):
                    print("player two is winner")
                    break
                plyr = tictactoe.switch_player(plyr)
                tictactoe.board_display()
            else:
                print("enter in the empty position.")
            



#Player implementation. What does a player do? what are some of the actions that a player can take it is always a player.vs player
if __name__ == "__main__":
    print("Welcome to the main screen for tictactoe")
    game_loop()
    
   