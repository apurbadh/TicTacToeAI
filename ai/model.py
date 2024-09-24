import json
from game.tictactoe import TicTacToe
from copy import deepcopy

class Move:

    def __init__(self, move, outcome) -> None:
        

        self.move = move 
        self.outcome = outcome 
        self.nextMoves = [] 
        self.winCount = [0]


    def get_move(self):
        return self.move
    
    def add_move(self, ticTacToe: TicTacToe, prevMoves, winCount = [0]):

        prevMoves.append(self.move)


        for i in range(0, 9):
            if i not in prevMoves:
                temp = deepcopy(ticTacToe)
                ticTacToe.make_move(i)

                if ticTacToe.check_win() == 'O':
                    move = Move(i, 'win')
                    winCount[0] = winCount[0] + 1
                elif ticTacToe.check_win() == 'X':
                    move = Move(i, 'lost')

                elif ticTacToe.check_draw():
                    move = Move(i, 'draw')
                else:
                    move = Move(i, 'next')
                    prevMoves2 = deepcopy(prevMoves)
                    ttt = deepcopy(ticTacToe)
                    ttt.switch_player()
                    move.add_move(ttt, prevMoves2, winCount)


                self.nextMoves.append(move)
                ticTacToe = temp
                self.winCount[0] = self.winCount[0] + winCount[0]
                winCount = [0]
        # print(self.winCount)



    def toJSON(self):

        return {
            f"{self.move}": {
                'outcome': self.outcome,
                'wins': self.winCount[0],
                'next': [move.toJSON() for move in self.nextMoves]
            }
        }





class MoveJSONEncoder(json.JSONEncoder):

    def default(self, o: Move):
        return o.toJSON()


