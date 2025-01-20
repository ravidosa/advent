from utils import *
inp = input_file(2021, 3).strip()

parsed_input = parser(inp, ["\n"], str)

most_common = lambda bins, i: None if (bal := sum(map(lambda b: b[i] == "1", bins))) == len(bins) / 2 else ("1" if bal > len(bins) / 2 else "0")

bits = len(parsed_input[0])
gamma = int("".join(map(lambda i: most_common(parsed_input, i), range(bits))), 2)
epsilon = 2 ** bits - 1 - gamma
p1 = gamma * epsilon

match_oxy = parsed_input.copy()
i = 0
while len(match_oxy) > 1:
    m_com = most_common(match_oxy, i)
    match_oxy = [b for b in match_oxy if b[i] == ("1" if m_com == None else m_com)]
    i += 1
match_co2 = parsed_input.copy()
i = 0
while len(match_co2) > 1:
    m_com = most_common(match_co2, i)
    match_co2 = [b for b in match_co2 if b[i] != ("1" if m_com == None else m_com)]
    i += 1
p2 = int(match_oxy[0], 2) * int(match_co2[0], 2)

output(p1, p2)