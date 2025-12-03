with open("/dev/stdin") as f:
    banks = f.readlines()
def solve(bank: str, t=12, out=None):
    bank = bank.strip()
    substr = bank[:-t+1]
    if len(bank) == t:
        return bank
    if t == 1:
        return max(bank)

    # print(f"substr={substr!s:<4} bank={bank!s:<16} t={t}")
    idx = bank.index(max(substr))
    return max(substr) + solve(bank[idx+1:], t-1)

for b in banks:
    print(solve(b))
    
print(sum(int(solve(b)) for b in banks))
