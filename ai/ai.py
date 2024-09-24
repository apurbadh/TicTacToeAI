import json
from ai.exceptions import CannotReadAIFile
import random

class AI:

    def __init__(self):
        self.data = None
        self.file = None


    def check_next_loss(self, move):

        key = list(move.keys())[0]
        nextMoves = move[key]['next']

        for m in nextMoves:
            mv = m[list(m.keys())[0]]
            
            if mv['outcome'] == 'lost':                
                return True 
            
        return False

        



    def predict(self, moves):


        # if len(moves) == 1:

        #     randnum = random.randrange(0, 9)
        #     while randnum in moves: 
        #         randnum = random.randrange(0, 9)
        #     return randnum
            

        data = self.data

        for move in moves:
            
            for d in data:

                if f"{move}" in d.keys():

                    data = d[f"{move}"]['next']

        firstKey = list(data[0].keys())[0]
        highest = {
            'move': firstKey,
            'prob': 0
        }

        for move in data:
            key = list(move.keys())[0]
            prob = move[key]['prob']

            if move[key]['outcome'] == 'win':
                highest ={
                    'move': key,
                    'prob': prob
                }
                break

            if not self.check_next_loss(move) and prob >= highest['prob']:
                highest = {
                    'move': key,
                    'prob': prob
                }
                

        predicted_move = int(highest['move'])
        return predicted_move
        


    def setData(self, file):
        try:
            data = json.load(file)
        except:
            raise CannotReadAIFile("Invalid Content")
        self.data = data
        self.file = file
        return self