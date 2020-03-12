"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # frontier is a Stack imported from util in this case
    frontier = util.Stack()
    # frontier contains the nodes which contain startingNode, action, cost
    print("Start:", problem.getStartState())
    starting_state = problem.getStartState()
    path_actions = []
    frontier.push((starting_state, path_actions, 0))
    # visited is a list for storing nodes which have been visited
    visited = set()

    while not frontier.isEmpty():
        # Popping the topmost node
        top_node = frontier.pop()
        state = top_node[0]
        actions = top_node[1]
        cost = top_node[2]
        # On reaching goal state, we need to return a list of valid actions from start to goal
        if problem.isGoalState(state):
            return actions
        # If it is a state other than goal state, we push unvisited successors to the frontier
        if state not in visited:
            visited.add(state)
            # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
            for successor in problem.getSuccessors(state):
                x = successor[0]
                if x not in visited:
                    y = successor[1]
                    z = successor[2]
                    # successor[1] stored in y has to be concatenated with list actions
                    # Hence, while pushing the successor into the frontier, we take care of this
                    frontier.push((x, actions + [y], cost + z))
                else:
                    continue
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    # frontier is a Queue imported from util in this case
    frontier = util.Queue()
    # frontier contains the nodes which contain startingNode, action, cost
    print("Start:", problem.getStartState())
    starting_state = problem.getStartState()
    path_actions = []
    frontier.push((starting_state, path_actions, 0))
    # visited is a list for storing nodes which have been visited
    visited = set()

    while not frontier.isEmpty():
        # Popping the node at the front
        front_node = frontier.pop()
        state = front_node[0]
        actions = front_node[1]
        cost = front_node[2]
        # On reaching goal state, we need to return a list of valid actions from start to goal
        if problem.isGoalState(state):
            return actions
        # If it is a state other than goal state, we push unvisited successors to the frontier
        if state not in visited:
            visited.add(state)
            # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
            for successor in problem.getSuccessors(state):
                if successor[0] not in visited:
                    x = successor[0]
                    y = successor[1]
                    z = successor[2]
                    # successor[1] stored in y has to be concatenated with list actions
                    # Hence, while pushing the successor into the frontier, we take care of this
                    frontier.push((x, actions + [y], cost + z))
                else:
                    continue
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    # frontier is a PriorityQueue imported from util in this case
    frontier = util.PriorityQueue()
    # frontier contains the nodes which contain startingNode, action, cost
    print("Start:", problem.getStartState())
    starting_state = problem.getStartState()
    path_actions = []
    frontier.push((starting_state, path_actions, 0), 0)
    # visited is a list for storing nodes which have been visited
    visited = set()

    while not frontier.isEmpty():
        # Popping a node
        start_node = frontier.pop()
        state = start_node[0]
        actions = start_node[1]
        cost = start_node[2]
        # On reaching goal state, we need to return a list of valid actions from start to goal
        if problem.isGoalState(state):
            return actions
        # If it is a state other than goal state, we push unvisited successors to the frontier
        if state not in visited:
            visited.add(state)
            # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
            for successor in problem.getSuccessors(state):
                if successor[0] not in visited:
                    x = successor[0]
                    y = successor[1]
                    z = successor[2]
                    # successor[1] stored in y has to be concatenated with list actions
                    # Hence, while pushing the successor into the frontier, we take care of this
                    # For UCS, we need to push the cost of every action as well
                    frontier.push((x, actions + [y], cost + z), cost + z)
                else:
                    continue
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    # frontier is a PriorityQueue imported from util in this case
    frontier = util.PriorityQueue()
    # frontier contains the nodes which contain startingNode, action, cost
    print("Start:", problem.getStartState())
    starting_state = problem.getStartState()
    path_actions = []
    frontier.push((starting_state, path_actions, 0), 0)
    # visited is a list for storing nodes which have been visited
    visited = set()

    while not frontier.isEmpty():
        # Popping a node
        start_node = frontier.pop()
        state = start_node[0]
        actions = start_node[1]
        cost = start_node[2]
        # On reaching goal state, we need to return a list of valid actions from start to goal
        if problem.isGoalState(state):
            return actions
        # If it is a state other than goal state, we push unvisited successors to the frontier
        if state not in visited:
            visited.add(state)
            # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
            for successor in problem.getSuccessors(state):
                if successor[0] not in visited:
                    x = successor[0]
                    y = successor[1]
                    z = successor[2]
                    # successor[1] stored in y has to be concatenated with list actions
                    # Hence, while pushing the successor into the frontier, we take care of this
                    # For A* search, we need to add heuristic value while pushing the cost of every action
                    frontier.push((x, actions + [y], cost + z), cost + z + heuristic(x, problem))
                else:
                    continue
    # util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
