import random
import copy
from optparse import OptionParser
import util

class SolveEightQueens:
    def __init__(self, numberOfRuns, verbose, lectureExample):
        """
        Value 1 indicates the position of queen
        """
        self.numberOfRuns = numberOfRuns
        self.verbose = verbose
        self.lectureCase = [[]]
        if lectureExample:
            self.lectureCase = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ]
    def solve(self):
        solutionCounter = 0
        for i in range(self.numberOfRuns):
            if self.search(Board(self.lectureCase), self.verbose).getNumberOfAttacks() == 0:
                solutionCounter += 1
        print("Solved: %d/%d" % (solutionCounter, self.numberOfRuns))

    def search(self, board, verbose):
        """
        Hint: Modify the stop criterion in this function
        """
        newBoard = board
        i = 0
        while True:
            if verbose:
                print("iteration %d" % i)
                print(newBoard.toString())
                print("# attacks: %s" % str(newBoard.getNumberOfAttacks()))
                print(newBoard.getCostBoard().toString(True))
            currentNumberOfAttacks = newBoard.getNumberOfAttacks()
            # The algorithm should stop immediately if there is no attack between the queens
            if currentNumberOfAttacks == 0:
                break
            (newBoard, newNumberOfAttacks, newRow, newCol) = newBoard.getBetterBoard()
            i += 1
            if currentNumberOfAttacks <= newNumberOfAttacks:
                if i > 100:
                    # If the moves exceed 100, we then restart
                    i = 0
                    newBoard = Board([[]])
                    continue
        return newBoard

class Board:
    def __init__(self, squareArray = [[]]):
        if squareArray == [[]]:
            self.squareArray = self.initBoardWithRandomQueens()
        else:
            self.squareArray = squareArray

    @staticmethod
    def initBoardWithRandomQueens():
        tmpSquareArray = [[ 0 for i in range(8)] for j in range(8)]
        for i in range(8):
            tmpSquareArray[random.randint(0,7)][i] = 1
        return tmpSquareArray
          
    def toString(self, isCostBoard=False):
        """
        Transform the Array in Board or cost Board to printable string
        """
        s = ""
        for i in range(8):
            for j in range(8):
                if isCostBoard: # Cost board
                    cost = self.squareArray[i][j]
                    s = (s + "%3d" % cost) if cost < 9999 else (s + "  q")
                else: # Board
                    s = (s + ". ") if self.squareArray[i][j] == 0 else (s + "q ")
            s += "\n"
        return s 

    def getCostBoard(self):
        """
        First Initalize all the cost as 9999. 
        After filling, the position with 9999 cost indicating the position of queen.
        """
        costBoard = Board([[ 9999 for i in range(8)] for j in range(8)])
        for r in range(8):
            for c in range(8):
                if self.squareArray[r][c] == 1:
                    for rr in range(8):
                        if rr != r:
                            testboard = copy.deepcopy(self)
                            testboard.squareArray[r][c] = 0
                            testboard.squareArray[rr][c] = 1
                            costBoard.squareArray[rr][c] = testboard.getNumberOfAttacks()
        return costBoard

    def getBetterBoard(self):
        """
        "*** YOUR CODE HERE ***"
        This function should return a tuple containing containing four values
        the new Board object, the new number of attacks, 
        the Column and Row of the new queen  
        For exmaple: 
            return (betterBoard, minNumOfAttack, newRow, newCol)
        The datatype of minNumOfAttack, newRow and newCol should be int
        """
        # This is the current game board
        board = self.squareArray
        # This function should return a tuple containing containing four values
        betterBoard = []
        minNumOfAttack = 9999999999
        newRow = -1
        newCol = -1
        for x in range(len(board)):
            for y in range(len(board)):
                # If the value of the element at that position of the array is 1, it is a queen
                if board[x][y] == 1:
                    i = 0
                    while i < (len(board)):
                        tup1 = (i, y)
                        tup2 = (x, y)
                        if tup1 != tup2:
                            board[i][y] = 1
                            board[x][y] = 0
                            if self.getNumberOfAttacks() < minNumOfAttack:
                                betterBoard, minNumOfAttack, newRow, newCol = self.tuple_assign(i, y)
                            board[x][y] = 1
                            board[i][y] = 0
                        i = i + 1
        return betterBoard, minNumOfAttack, newRow, newCol
        # util.raiseNotDefined()

    def tuple_assign(self, i, y):
        betterboard = copy.deepcopy(self)
        minNumOfAttack = self.getNumberOfAttacks()
        newRow = i
        newCol = y
        return betterboard, minNumOfAttack, newRow, newCol

    def getNumberOfAttacks(self):
        """
        "*** YOUR CODE HERE ***"
        This function should return the number of attacks of the current board
        The datatype of the return value should be int
        """
        board = self.squareArray
        # We have the current game board but we also need to have a list of the positions of the queens
        # We can store only the rows for this purpose in a single dimensional array
        queens = []
        for y in range(len(board)):
            for x in range(len(board)):
                # If the value of the element at that position of the array is 1, it is a queen
                if board[x][y] == 1:
                    queens.append(x)
        # Calculating the number of attacks
        # count is a variable which will be used to store the number of attacks
        count = 0
        for row1 in range(len(queens)):
            for row2 in range(row1 + 1, len(queens)):
                if queens[row1] == queens[row2]:
                    count += 1
                if abs(queens[row1] - queens[row2]) == (row2 - row1):
                    count += 1
        return count
        # util.raiseNotDefined()

if __name__ == "__main__":
    #Enable the following line to generate the same random numbers (useful for debugging)
    random.seed(1)
    parser = OptionParser()
    parser.add_option("-q", dest="verbose", action="store_false", default=True)
    parser.add_option("-l", dest="lectureExample", action="store_true", default=False)
    parser.add_option("-n", dest="numberOfRuns", default=1, type="int")
    (options, args) = parser.parse_args()
    EightQueensAgent = SolveEightQueens(verbose=options.verbose, numberOfRuns=options.numberOfRuns, lectureExample=options.lectureExample)
    EightQueensAgent.solve()
