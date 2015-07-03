def load_grid():
    grid = [[0 for x in range(20)] for y in range(20)]
    with open("data.txt", "rb") as datafile:
        y = 0
        for line in datafile:
            x = 0
            for item in line.decode('utf-8').strip().split(' '):
                grid[x][y] = int(item)
                x += 1
            y += 1
    return grid

def check_neighbors(x, y, grid):

    max_val = 0
    #up
    if y >= 3:
        up_val = (grid[x][y]) * (grid[x][y - 1]) * (grid[x][y - 2]) * (grid[x][y - 3])
        if up_val > max_val:
            max_val = up_val

    #left
    if y <= 16:
        down_val = (grid[x][y]) * (grid[x][y + 1]) * (grid[x][y + 2]) * (grid[x][y + 3])
        if down_val > max_val:
            max_val = down_val

    #right
    if x <= 16:
        right_val = (grid[x][y]) * (grid[x + 1][y]) * (grid[x + 2][y]) * (grid[x + 3][y])
        if right_val > max_val:
            max_val = right_val

    #left
    if x >= 3:
        left_val = (grid[x][y]) * (grid[x - 1][y]) * (grid[x - 2][y]) * (grid[x - 3][y])
        if left_val > max_val:
            max_val = left_val

    #south-eastern diagonal
    if x <= 16 and y <= 16:
        se_val = (grid[x][y] * (grid[x+1][y+1]) * (grid[x+2][y+2]) * (grid[x+3][y+3]))
        if se_val > max_val:
            max_val = se_val

    #north-western diagonal
    if x >= 3 and y >= 3:
        nw_val = (grid[x][y] * (grid[x-1][y-1]) * (grid[x-2][y-2]) * (grid[x-3][y-3]))
        if nw_val > max_val:
            max_val = nw_val

    #south-western diagonal
    if x >= 3 and y <= 16:
        sw_val = (grid[x][y] * (grid[x-1][y+1]) * (grid[x-2][y+2]) * (grid[x-3][y+3]))
        if sw_val > max_val:
            max_val = sw_val

    #north-eastern diagonal
    if x >= 3 and y <= 16:
        ne_val = (grid[x][y] * grid[x-1][y+1] * grid[x-2][y+2] * grid[x-3][y+3])
        if ne_val > max_val:
            max_val = ne_val

    return max_val



def find_max_sequence():
    grid = load_grid()
    max_val = 0
    for x in range(20):
        for y in range(20):
            val = check_neighbors(x, y, grid)
            if val > max_val:
                max_val = val
    return max_val

print(find_max_sequence())
