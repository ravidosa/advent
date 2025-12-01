from utils import *
import hashlib
inp = input_file(2016, 14).strip()

def consec(s, n):
    res = re.search(r"(.)\1{" + str(n - 1) + r"}", s)
    if res:
        return res.group()[0]
    return None

consec_match = lambda s, c, n: (c * n) in s

def stretched_hash(salt, n):
    res = hashlib.md5(salt.encode()).hexdigest()
    for i in range(n):
        res = hashlib.md5(res.encode()).hexdigest()
    return res

def key_search(ind, stretch):
    memo = {}
    i = -1
    key = 0
    while key < ind:
        i += 1
        res = memo[i] if i in memo else stretched_hash(inp + str(i), stretch)
        memo[i] = res
        c = consec(res, 3)
        if c:
            for j in range(i + 1, i + 1001):
                res_ahead = memo[j] if j in memo else stretched_hash(inp + str(j), stretch)
                memo[j] = res_ahead
                if consec_match(res_ahead, c, 5):
                    key += 1
                    break
    return i

p1 = key_search(64, 0)

p2 = key_search(64, 2016)

output(p1, p2)