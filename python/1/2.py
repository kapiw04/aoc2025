with open("/dev/stdin") as f:
    rotations = f.readlines()

cur_rot = 50
count = 0

for rot in rotations:
    rot = rot.strip()
    dir, n = rot[0], int(rot[1:])
    d = n * (1 if dir == "R" else -1)
    for _ in range(n):
        cur_rot += 1 if dir == "R" else -1
        cur_rot %= 100
        if cur_rot == 0:
            count += 1


print(count)
