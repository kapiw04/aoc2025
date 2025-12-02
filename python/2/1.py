with open("/dev/stdin") as f:
    ranges = f.read().split(',')

ids = set()

def is_invalid_id(i: int) -> bool:
    sid = str(i)
    if len(sid) % 2 != 0:
        return False
    return sid[:len(sid)//2] == sid[len(sid)//2:]

        

for r in ranges:
    start, end = r.split('-')
    start = int(start)
    end = int(end)
    ids |= set(i for i in range(start, end+1) if is_invalid_id(i))
    
print(sum(ids))
