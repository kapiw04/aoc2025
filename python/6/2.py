from operator import add, mul
from functools import reduce

with open("/dev/stdin") as f:
    rows = f.readlines()

grid = list(r for r in rows)
width = len(grid[0])
height = len(grid)
i = 0

sols = []

while i < width:
    op_str = ''
    nums = []
    col = [r[i] for r in grid]
    num = "".join(col[:-1]).strip()
    while i < width and num != '':
        col = [r[i] for r in grid]
        op_str = col[-1] if col[-1] != ' ' and col[-1] != '\n' else op_str
        num = "".join(col[:-1]).strip()
        nums.append(num)
        i += 1

    nums.remove('')
    op = add if op_str == "+" else mul
    sols.append(reduce(lambda x, c: op(int(x), int(c)), nums))

print(sum(sols))

