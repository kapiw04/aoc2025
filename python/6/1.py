from operator import add, mul
from functools import reduce


with open("/dev/stdin") as f:
    rows = f.readlines()

grid = list(list(filter(lambda x: x != '', (r.strip().split(" ")))) for r in rows)
width = len(grid[0])

sol = 0

for i in range(width):
    op = add if grid[-1][i] == "+" else mul
    sol += reduce(lambda x, c: op(int(x), int(c)), (r[i] for r in grid[:-1]))

print(sol)
