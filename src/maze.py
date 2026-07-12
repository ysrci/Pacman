from mazegenerator import MazeGenerator


def make_maze(size_screen):

    TILE_SIZE = 32
    cols = size_screen[0] // TILE_SIZE - 5
    rows = size_screen[1] // TILE_SIZE
    # create a simpel 20x20 maze
    maze_gen = MazeGenerator(size=(cols, rows))
    
    # get the maze structure
    maze_grid = maze_gen.maze
    
    #shortest path
    shortest_path = maze_gen.shortest_path
    
    # enrty exit
    entry = maze_gen.maze_entry
    exit = maze_gen.maze_exit
    print(f"Entry: {maze_gen.maze_entry}, Exit: {maze_gen.maze_exit}")
    
    # x y
    x, y = len(maze_grid[0]), len(maze_grid)
    
    
    return TILE_SIZE, maze_grid, (x, y), entry, exit


if __name__ == "__main__":
    make_maze()