from utils import *
inp = input_file(2023, 7).strip()

parsed_input = parser(inp, ["\n", " "])

types = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]

strength = "23456789TJQKA"
def val(hand):
    typ = sorted(collections.Counter(hand).values())
    return types.index(typ) * 16 ** 5 + sum(16 ** (4 - i) * strength.index(hand[i]) for i in range(5))
p1 = sum((ind + 1) * hand[1] for ind, hand in enumerate(sorted(parsed_input, key=lambda i: val(str(i[0])))))

strength = "J23456789TQKA"
def val(hand):
    typhand = hand.replace(max(set(hand), key=lambda c: hand.count(c) if c != "J" else -1), "J") if "J" in hand and hand != "JJJJJ" else hand
    typ = sorted(collections.Counter(typhand).values())
    return types.index(typ) * 16 ** 5 + sum(16 ** (4 - i) * strength.index(hand[i]) for i in range(5))
p2 = sum((ind + 1) * hand[1] for ind, hand in enumerate(sorted(parsed_input, key=lambda i: val(str(i[0])))))

output(p1, p2)