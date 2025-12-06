with open("/dev/stdin") as f:
    ranges, ids = f.read().split("\n\n")
    
def is_valid(i: int) -> bool:
    for r in ranges.split("\n"):
        start, end = r.split("-")
        if int(start) <= i <= int(end):
            return True
    return False

    
count = 0
for i in ids.split("\n")[:-1]:
    if is_valid(int(i)):
        count += 1

print(count)
