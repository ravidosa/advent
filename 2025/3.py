from utils import *
inp = input_file(2025, 3).strip()

parsed_input = parser(inp, "{{li|}}")

def joltage(batteries, count):
    dp = [[0 for _ in range(len(batteries) + 1)] for _ in range(count)]
    for i in range(1, len(batteries) + 1):
        dp[0][i] = max(batteries[:i])
    for j in range(1, count):
        for i in range(1, len(batteries) + 1):
            dp[j][i] = max(dp[j][i - 1], dp[j - 1][i - 1] * 10 + batteries[i - 1])
    return dp[count - 1][len(batteries)]


p1 = sum([joltage(batteries, 2) for batteries in parsed_input])

p2 = sum([joltage(batteries, 12) for batteries in parsed_input])

output(p1, p2)