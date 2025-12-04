with open("/dev/stdin") as f:
    rows = f.readlines()

width = len(rows[0].strip()) 
height = len(rows)

grid = [list(r.strip()) for r in rows]

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

for x in range(width):
    for y in range(height):
        if grid[y][x] == "@" and get_surr(x, y):
            count += 1

print(count)
def print_grid():
    for r in grid:
        print("".join(r))
