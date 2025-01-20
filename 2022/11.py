from utils import *
inp = input_file(2022, 11).strip()

parsed_input = parser(inp, ["\n\n", "\n", "Monkey |  Starting items: |  Operation: new = old |  Test: divisible by |    If true: throw to monkey |    If false: throw to monkey|:| |, "])

oper = lambda old, op: old ** 2 if op == ["*", "old"] else old * op[1] if op[0] == "*" else old + op[1]
def monkeying(rounds, worry):
    monkeys = {i[0][0]: {"it": i[1].copy(), "op": i[2], "div": i[3][0], "thr": [i[5][0], i[4][0]], "ins": 0} for i in parsed_input}
    for _ in range(rounds):
        for __, mval in monkeys.items():
            mval["it"] = [worry(oper(old, mval["op"])) for old in mval["it"]]
            mval["ins"] += len(mval["it"])
            while len(mval["it"]) > 0:
                check = mval["it"].pop(0)
                monkeys[mval["thr"][check % mval["div"] == 0]]["it"].append(check)
    return monkeys

p1 = prod(sorted(map(lambda m: m["ins"], monkeying(20, lambda i: i // 3).values()))[-2:])

divvy = math.lcm(*map(lambda i: i[3][0], parsed_input))
p2 = prod(sorted(map(lambda m: m["ins"], monkeying(10000, lambda i: i % divvy).values()))[-2:])

output(p1, p2)