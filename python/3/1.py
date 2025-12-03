with open("/dev/stdin") as f:
    banks = f.readlines()

def solve(bank):
    for r in range(9, 0, -1):
        i = bank[:-2].find(str(r))
        if i >= 0:
            for r in range(9, 0, -1):
                j = bank[i+1:].find(str(r))
                if j >= 0:
                    return bank[i] + bank[i+1+j]

    return ""


print(sum(int(solve(bank)) for bank in banks))
