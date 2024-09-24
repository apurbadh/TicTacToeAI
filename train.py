from game.tictactoe import TicTacToe
from typing import List
from ai.model import Move, MoveJSONEncoder
import json

ticTacToe = TicTacToe(None)

moves: List[Move] = []

for i in range(0, 9):
    move = Move(i, 'next')
    moves.append(move)


for move in moves:
    ticTacToe.make_move(move.get_move())
    ticTacToe.switch_player()
    move.add_move(ticTacToe, [])
    ticTacToe.recreate()



print(json.dumps(moves, cls=MoveJSONEncoder))
        


