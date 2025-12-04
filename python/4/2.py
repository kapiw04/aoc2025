from copy import deepcopy

with open("/dev/stdin") as f:
    rows = f.readlines()

width = len(rows[0].strip()) 
height = len(rows)

grid = [list(r.strip()) for r in rows]

def count_rolls():
    return "".join("".join(r) for r in grid).count("@")

def get_surr(x, y):
    surr = ""
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            cx = dx+x
            cy = dy+y
            if 0 <= cx < width and 0 <= cy < height: 
                surr += grid[cy][cx]
    
    return surr.count("@") < 4

count = 0
start_count_rolls = count_rolls()
prev_count_rolls = 0
while True:
    new_grid = deepcopy(grid)

    for x in range(width):
        for y in range(height):
            if grid[y][x] == "@" and get_surr(x, y):
                count += 1
                new_grid[y][x] = "."
    grid = new_grid
    def print_grid(g):
        for r in g:
            print("".join(r))
    if prev_count_rolls == count_rolls():
        break
    prev_count_rolls = count_rolls()

print(start_count_rolls - prev_count_rolls)
