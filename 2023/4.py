from utils import *
inp = input_file(2023, 4).strip()

parsed_input = parser(inp, "Card {{i}}: {{li }} \| {{li }}")

matching = lambda card: len(set(card[1]).intersection(card[2]))

p1 = sum(2 ** matching(c) // 2 for c in parsed_input)

cards = [1] * len(parsed_input)
for i in range(len(parsed_input)):
    m = matching(parsed_input[i])
    for c in range(i + 1, min(len(parsed_input), i + m + 1)):
        cards[c] += cards[i]
p2 = sum(cards)

output(p1, p2)