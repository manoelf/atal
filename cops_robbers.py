

def find_robbers(maze, x, y):
    '''
    That maze is a 5x5 matrix
    '''
    
    if (x == 4 and y == 4):
        return True
    if (is_safe(maze, x, y)) :
        if (find_robbers(maze, x + 1, y) == True):
            return True
        
        if (find_robbers(maze, x, y + 1) == True):
            return True
        return False
    return False
            



def is_safe(maze, x, y):
    if (x < 5 and y < 5):
        if (maze[x][y] == 0):
            return True
        else:
            return False
    else:
        return False
        
tests = int(input())
cont = 0

while (cont < tests):
    maze = []
    line = input()

    if (len(line.strip()) > 0):
        cont += 1
        maze.append(list(map(int, line.split())))
        for i in range(4):
            line = input()
            maze.append(list(map(int, line.split())))
        result = find_robbers(maze, 0, 0)
        if (result):
            print('COPS')
        else:
            print('ROBBERS')




