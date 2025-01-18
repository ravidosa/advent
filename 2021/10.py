from utils import *
inp = open("2021/input-10.txt", "r").read()

parsed_input = parser(inp, ["\n"])

def score(chunk):
    stack = []
    for ch in chunk:
        if ch in "({[<":
            stack.append(ch)
        else:
            if stack and stack[-1] + ch in ["()", "{}", "[]", "<>"]:
                stack.pop()
            else:
                return (3 if ch == ")" else 57 if ch == "]" else 1197 if ch == "}" else 25137, stack)
    return (0, stack)
def autocomplete(chunk):
    sc, stack = score(chunk)
    if sc == 0:
        comp_sc = 0
        for s in stack[::-1]:
            comp_sc *= 5
            comp_sc += (1 if s == "(" else 2 if s == "[" else 3 if s == "{" else 4)
        return comp_sc
    return 0

print(sum(map(lambda i: score(i)[0], parsed_input)))

auto = sorted(filter(lambda cs: cs != 0, map(autocomplete, parsed_input)))
print(auto[len(auto) // 2])