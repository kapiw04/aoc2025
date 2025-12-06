with open("/dev/stdin") as f:
    intervals_string, ids = f.read().split("\n\n")

intervals = []
for r in intervals_string.split("\n"):
    start, end = r.split("-")
    intervals.append((int(start), int(end)))
intervals.sort()


def is_overlapping(s1, e1, s2, e2):
    return not (e1 < s2 or e2 < s1)


def merge_overlapping(s1, e1, s2, e2) -> tuple[int, int]:
    return min(s1, s2), max(e1, e2)

normalized = set()

    
for i1 in intervals:
    to_remove = set()
    to_add = set()
    flag = False
    for i2 in normalized:
        if is_overlapping(*i1, *i2):
            to_add.add(merge_overlapping(*i1, *i2))    
            to_remove.add(i2)
            flag = True
    normalized -= to_remove
    normalized |= to_add
    if not flag:
        normalized.add(i1)

count = 0
for i in normalized:
    count += i[1] - i[0] + 1

print(count)

