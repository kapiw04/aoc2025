with open("/dev/stdin") as f:
    rows = f.readlines()

splitter_positions: list[list[int]] = []
splits = [0  if c != 'S' else 1 for c in rows[0]]

for row in rows:
    splitter_positions.append([i for i, x in enumerate(row) if x == "^"])

for sp in splitter_positions:
    new_splits = splits.copy()
    for i, s in enumerate(splits):
        if i in sp:
            new_splits[i-1] += new_splits[i]
            new_splits[i+1] += new_splits[i]
            new_splits[i] = 0

    splits = new_splits


print(sum(splits))
