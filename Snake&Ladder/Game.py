from Board import Board
from Dice import Dice
from Player import Player
from collections import deque


class Game:
    def __init__(self):
        print("Initialise the Game")
        self.board = None
        self.dice = None
        self.winner = None
        self.playerList = deque([])
        self.initialiseGame()

    def initialiseGame(self)-> None:
        self.board = Board(boardSize=10, numberOfSnakes=5, numberOfLadders=5)
        self.dice = Dice(diceCount=1)
        self.winner = None
        self.addPlayer()


    def addPlayer(self):
        player_1 = Player(id="1", current_position=0)
        player_2 = Player(id="2", current_position=0)

        self.playerList.append(player_1)
        self.playerList.append(player_2)

    def startGame(self):
        while self.winner is None:

            # check whose turn now
            player_turn = self.findPlayerTurn()
            print(f'Player turn is : {player_turn.id} , current position is : {player_turn.current_position}')

            dice_number = self.dice.rollDice()


            new_position = player_turn.current_position + dice_number
            new_position = self.jumpCheck(new_position)

            player_turn.current_position = new_position

            print(f'player turn is : {player_turn.id} new position is : {new_position}')

            if new_position >= len(self.board.Cells[0]) * len(self.board.Cells[0]) - 1:
                self.winner = player_turn


        print(f'winner is : {self.winner.id}')

    def findPlayerTurn(self):
        player = self.playerList[0]
        self.playerList.popleft()
        self.playerList.append(player)

        return player

    def jumpCheck(self, new_position):

        # if new_position is outside the board limit
        if new_position > len(self.board.Cells) * len(self.board.Cells) -1:
            return new_position

        cell = self.board.getCell(new_position)
        if cell.jump and cell.jump.startPosition == new_position:
            jumpBy = "ladder" if cell.jump.startPosition < cell.jump.endPosition else "snake"

            print(f'Jump done by : {jumpBy}')
            return cell.jump.endPosition

        return new_position