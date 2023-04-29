from Cell import Cell
from Jump import Jump
import random

class Board:
    def __init__(self, boardSize: int, numberOfSnakes: int, numberOfLadders: int) -> None:
        self.Cells = None
        self.boardSize= boardSize
        self.initialiseCells(boardSize)
        self.addsnakesladders(self.Cells, numberOfSnakes, numberOfLadders)

    def initialiseCells(self, boardSize: int):
        self.Cells = [[0]*boardSize]*boardSize
        for row in range(boardSize):
            for col in range(boardSize):
                self.Cells[row][col] = Cell()


    def addsnakesladders(self, cells,  number_of_snakes: int, number_of_ladders: int):

        while number_of_snakes > 0:
            snake_head = random.randint(1,self.boardSize*self.boardSize-1)
            snake_tail = random.randint(1,self.boardSize*self.boardSize-1)

            if snake_tail >= snake_head :
                continue

            snake_obj = Jump(startPosition=snake_head, endPosition=snake_tail)

            cell = self.getCell(snake_head)
            cell.jump = snake_obj

            number_of_snakes = number_of_snakes-1



        while number_of_ladders > 0:
            ladder_head = random.randint(1,self.boardSize*self.boardSize)
            ladder_tail = random.randint(1,self.boardSize*self.boardSize)

            if ladder_tail <= ladder_head:
                continue

            ladder_obj = Jump(startPosition=ladder_head, endPosition=ladder_tail)

            cell = self.getCell(ladder_head)
            cell.jump = ladder_obj
            # cell.setJump(Jump=ladder_obj)

            number_of_ladders = number_of_ladders - 1


    def getCell(self, position) -> Cell:
        row = int(position/self.boardSize)
        col = int(position%self.boardSize)
        return self.Cells[row][col]