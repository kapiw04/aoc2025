with open("/dev/stdin") as f:
    rows = f.readlines()

splitter_positions: list[list[int]] = []
splits = {rows.pop(0).find('S')}

for row in rows:
    splitter_positions.append([i for i, x in enumerate(row) if x == "^"])
    

new_splits = splits.copy()

count = 0

for row in splitter_positions:
    new_splits = splits.copy()
    for split in splits:
        if split in row:
            new_splits.remove(split)
            new_splits.update({split-1, split+1})
            count += 1

    splits = new_splits
print(count)
