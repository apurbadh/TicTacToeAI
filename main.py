from game.tictactoe import TicTacToe
from ai.ai import AI
from sys import argv


def main():
    

    if len(argv) == 2:
        file = open(argv[1], 'r+')
        ai = AI()
        ai.setData(file)
    
    else:
        ai = None


   
    game = TicTacToe(ai)
    game.run()

if __name__ == '__main__':
    main()