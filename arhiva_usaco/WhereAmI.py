def longest_repeated_substring(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    mod = (1 << 61) - 1
    base = 131

    prefix_hash = [0] * (n + 1)
    power = [1] * (n + 1)
    for i in range(n):
        prefix_hash[i + 1] = (prefix_hash[i] * base + ord(s[i])) % mod
        power[i + 1] = (power[i] * base) % mod

    def get_hash(l: int, r: int) -> int:
        # hash of s[l:r]
        return (prefix_hash[r] - prefix_hash[l] * power[r - l]) % mod

    def has_repeat(length: int) -> bool:
        if length == 0:
            return True
        seen = {}
        for i in range(n - length + 1):
            h = get_hash(i, i + length)
            if h in seen:
                return True
            seen[h] = i
        return False

    lo, hi, ans = 0, n - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if has_repeat(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

import sys

name = "whereami"

sys.stdin = open("{}.in".format(name), "r")
sys.stdout = open("{}.out".format(name), "w")

n = int(input())
s = input().strip()
print(longest_repeated_substring(s)+1)