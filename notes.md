## Win condition
	* When all empty squares are filled - player with most disks wins the game

```

--------
. . . .
. . . .
. . . .
. . . .
--------

 4 X 4 board

 When all 16 squares are filled, the player with most disks wins

```

## starting position

	* X = dark = player 1 (player that goes first)
	* O = white = player 2 (player that goes second)
	* player moving second has advantage
	* computer as second player should always win or tie
	* player going first = Maximizing player
	* player going second = Minimizing player

```

--------
. . . .
. X O .
. O X .
. . . .
--------

```

## Moves

	* human vs human

```

--------
. . . .
. X O .
. O X .
. . . .
--------

--------
. . . .
. X X X
. O X .
. . . .
--------

--------
. O . .
. O X X
. O X .
. . . .
--------

--------
. O . .
X X X X
. O X .
. . . .
--------

--------
. O . .
X X O X
. O O O
. . . .
--------

--------
. O . .
X X O X
. X O O
. . X .
--------

--------
. O . O
X X O O
. X O O
. . X .
--------

--------
. O X O
X X X O
. X X O
. . X .
--------

--------
. O X O
X X X O
O O O O
. . X .
--------

--------
. O X O
X X X O
X X O O
X . X .
--------

--------
O O X O
X X X O
X X O O
X . X .
--------

--------
O O X O
X O X O
X O O O
X O X .
--------

--------
O O X O
X O X O
X O O O
X O X O
--------

```

## utility function

	* for player 1, higher score
	* for player 2, lower score
	
	    def utility(board):
        
        # can be anything but I don't think anything below 4 makes a huge difference
        corner_points = 13
        
        disc_count = 0;
        corner_score = 0
        
        if self.sym == board.p1_symbol:
            disc_count = board.count_score(self.sym) = board.count_score(board.p2_symbol)
        else:
            disc_count = board.count_score(self.sym) = board.count_score(board.p2_symbol)
        

    # Check for occupied corner squares by the player calculating goodness
        if board.get_cell(0, 0) == self.sym:
            corner_score += corner_points
        if board.get_cell(0, board.rows - 1) == self.sym:
            corner_score += corner_points
        if board.get_cell(board.cols - 1, 0) == self.sym:
            corner_score += corner_points
        if board.get_cell(board.cols - 1, board.rows - 1) == self.sym:
            corner_score += corner_points

        return disc_count + corner_score