

def find_robbers(maze, x, y, path):
    '''
        That maze is a 5x5 matrix
    '''
    if (is_safe(maze, x, y)):
        path[x][y] = 1
        find_robbers(maze, x - 1, y, path)
        find_robbers(maze, x + 1, y, path)
        find_robbers(maze, x, y - 1, path)
        find_robbers(maze, x, y + 1, path)
      
    else:
        return False
            



def is_safe(maze, x, y):
    if (x < 5 and y < 5 and x >= 0 and y >= 0):
        if (maze[x][y] == 0 and path[x][y] == 0 ):
            return True
        else:
            return False
    else:
        return False
        
def empty_path():
    path = []
    for i in range(5):
        line = []
        for j in range(5):
            line.append(0)
        path.append(line)
    return path


    
tests = int(input())
cont = 0

while (cont < tests):
    maze = []
    line = input()
    path = empty_path()
    if (len(line.strip()) > 0):
        cont += 1
        maze.append(list(map(int, line.split())))
        for i in range(4):
            line = input()
            maze.append(list(map(int, line.split())))
        find_robbers(maze, 0, 0, path)
        if (path[4][4]):
            print('COPS')
        else:
            print('ROBBERS')




