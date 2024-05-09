# import board
from othello_board import OthelloBoard 
import math
'''
    Defines Player class, and subclasses Human and Minimax Player.
'''



class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row

class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
            self.sym = 'X'
        else:
            self.oppSym = 'X'
            self.sym = 'O'
    
    '''
    
        minimax - minimax algorithm
        arg1 - game_board - a grid representing the game board
        arg2 - depth - the current depth
        arg3 - maximizingPlayer - true if first player, false if second player

    '''
    def minimax(self, game_board, depth, maximizingPlayer):
        
        # if the maximum depth is reached or terminal state is achieved, return none and the utility
        if depth == 0 or not game_board.has_legal_moves_remaining(self.sym):
            return None, self.utility(game_board)
        
        # if the maximizingPlayer is first player
        if maximizingPlayer:
            best_move = (0, 0)
            best_value = -math.inf
            
            # traverse grid
            for col in range(game_board.cols):
                for row in range(game_board.rows):
                    
                    # if game_board allows a legal move, clone the board for game instance
                    if game_board.is_legal_move(col, row, 'X'):
                        new_board = game_board.clone_of_board()

                        new_board.play_move(col, row, 'X')
                        
                        # get the new value and compare to current best value and assign if better
                        foo, value = self.minimax(new_board, depth - 1, False)
                        best_value = max(best_value, value)
                        if value >= best_value:
                            best_value = value
                            best_move = (col, row)
            
            # return best move and best value for the recursive computation of best values 
            return best_move, best_value
        else:
            # minimizing player goes second
            
            best_move = (0, 0)
            best_value = math.inf
            value = 0
            
            # traverse grid
            for col in range(game_board.cols):
                for row in range(game_board.rows):
                    
                    # if game_board allows a legal move, clone it
                    if game_board.is_legal_move(col, row, 'O'):
                        new_board = game_board.clone_of_board()
                        
                        new_board.play_move(col, row, 'O')
                        foo, value = self.minimax(new_board, depth - 1, True)
                        
                        #compare with best value and assign if better
                        best_value = min(best_value, value)
                        if type(best_value) is tuple:
                            best_value = best_value[0]
                        if value <= best_value:
                            best_value = value
                            best_move = (col, row)
            
            # return best move and best value for the recursive computation of best values 
            return best_move, best_value
    
    '''
    
        get_move - gets a move from the minimax player
        arg1 - game_board - the game_board in its current state
    
    '''
    def get_move(self, game_board):
        
        # limit depth here
        depth = 2 
        
        if self.sym == 'X':
                best_move, best_value = self.minimax(game_board, depth, True)
        else:
            best_move, best_value = self.minimax(game_board, depth, False)
        
        return best_move

    '''
    
        get_successors - I originally wrote this as a helper function to get successors but I found it easier to work with in the minmax function
        arg1 - board_state
        
    '''
    def get_successors(self, board_state):
        successors = []
        for column in range(board_state.get_num_cols()):
            for row in range(board_state.get_num_rows()):
                if board_state.get_cell(column, row) == '.':
                    board_copy = board_state.clone_of_board()
                    board_copy.grid[column][row] = self.sym
                    
                    
                    if not board_copy.is_legal_move(column, row, self.sym):
                        return
                    board_copy.flip_pieces(column, row, self.sym)
                    successors.append([board_copy, column, row])
        return successors
    
    '''
    
        utility - Utility function to determine goodness of both players by adding each cell they control
        arg1 - board_state - the playing board
        return - both players' scores
      
    '''
    def utility(self, board_state):
        player_1_score = 0
        player_2_score = 0
        for column in range(board_state.get_num_cols()):
            for row in range(board_state.get_num_rows()):
                if board_state.get_cell(column, row) == 'X':
                    player_1_score += 1
                elif board_state.get_cell(column, row) == 'O':
                    player_2_score += 1
        return player_1_score - player_2_score
    
    '''
        
        is_terminal - checks if the game is in a terminal state which would be when the board is completely filled
        arg1 - state - the board
        return - boolean - true if in a terminal state, false all other cases
        
    '''
    def is_terminal(self, state):
        if type(state) is list:
            state = state[0]
        columns = state.get_num_cols()
        rows = state.get_num_rows()
        for column in range(columns):
            for row in range(rows):
                if(state.is_cell_empty(column, row)):
                    return False
        
        return True

