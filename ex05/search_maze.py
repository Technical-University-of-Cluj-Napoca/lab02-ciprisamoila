import sys
from collections import deque

def read_maze(filename: str) -> list[list[str]]:
    """Reads a maze from a file and returns it as a list of lists (i.e. a matrix).

    Args:
        filename (str): The name of the file containing the maze.
    Returns:
        list: A 2D list (matrix) representing the maze.
    """

    mat = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                mat.append(list(line[:len(line) - 1]))
            else:
                mat.append(list(line))
    return mat



def find_start_and_target(maze: list[list[str]]) -> list[tuple[int, int]]:
    """Finds the coordinates of start ('S') and target ('T') in the maze, i.e. the row and the column
    where they appear.

    Args:
        maze (list[list[str]): A 2D list (matrix) representing the maze.
    Returns:
        list[tuple[int, int]]: A tuple containing the coordinates of the start and target positions.
        Each position is represented as a tuple (row, column).
    """

    res = []
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value in ['S', 'T']:
                res.append((i, j))

    return res 



def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:
    """Given a position in the maze, returns a list of valid neighboring positions: (up, down, left, right)
    where the player can be moved to. A neighbor is considered valid if (1) it is within the bounds of the maze
    and (2) not a wall ('#').

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        position (tuple[int, int]): The current position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of valid neighboring positions.
    """
    # construct the direction array: list[tuple[int, int]] (up, down, left, right)
    # test the position in each direction
    n = len(maze)
    m = len(maze[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = []
    for dir in dirs:
        xnew = position[0] + dir[0]
        ynew = position[1] + dir[1]

        if xnew < 0 or xnew >= n or ynew < 0 or ynew >= m or maze[xnew][ynew] == '#':
            pass
        else:
            neighbours.append((xnew, ynew))
    
    return neighbours



def bfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a breadth-first search (BFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # from collections you can import deque for using a queue.
    q = deque([(start, [start])])
    visited = {start}
    while q:
        node, path = q.popleft()
        if node == target:
            return path
        for neigh in get_neighbors(maze, node):
            if neigh not in visited:
                visited.add(neigh)
                new_path = path + [neigh]
                q.append((neigh, new_path))
            
    return None



def dfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a depth-first search (DFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # you can use a list as a stack in Python.
    s = [(start, [start])]
    visited = {start}
    while s:
        node, path = s.pop()
        if node == target:
            return path
        for neigh in get_neighbors(maze, node):
            if neigh not in visited:
                visited.add(neigh)
                new_path = path + [neigh]
                s.append((neigh, new_path))
            
    return None



def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    """Prints the maze to the console, marking the path with '.' characters.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        path (list[tuple[int, int]]): A list of positions representing the path to be marked.
    Returns:
        None
    """
    # # ANSI escape code for red
    RED = "\033[91m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    RESET = "\033[0m"
    # encode a character with red color: RED + char + RESET

    maze_copy = maze.copy()

    for x, y in path:
        if maze_copy[x][y] not in ('S', 'T'):
            maze_copy[x][y] = f"{RED}x{RESET}"
        elif maze_copy[x][y] == 'S':
            maze_copy[x][y] = f"{GREEN}S{RESET}"
        else:
            maze_copy[x][y] = f"{YELLOW}T{RESET}"

    for row in maze_copy:
        print(''.join(row))



if __name__ == "__main__":
    # Example usage: py maze_search.py dfs/bfs maze.txt
    if len(sys.argv) != 3:
        print("Usage: py search_maze.py dfs/bfs maze.txt")
    method = sys.argv[1]
    filename = sys.argv[2]
    maze = read_maze(filename)
    s, t = find_start_and_target(maze)
    path = []
    if method == "bfs":
        path = bfs(maze, s, t)
    elif method == "dfs":
        path = dfs(maze, s, t)

    if path is None:
        print("No solution")
    else:
        print_maze_with_path(maze, path)