with open("/dev/stdin") as f:
    ranges = f.read().split(',')

ids = set()

def is_invalid_id(sid: str) -> bool:
    for i in range(1, len(sid)):
        if sid == sid[:i] * (len(sid) // i):
            return True
    
    return False



for r in ranges:
    start, end = r.split('-')
    start = int(start)
    end = int(end)
    ids |= set(i for i in range(start, end+1) if is_invalid_id(str(i)))

print(sum(ids))
