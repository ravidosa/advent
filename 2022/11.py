from utils import *
inp = open("2022/input-11.txt", "r").read()

parsed_input = parser(inp, ["\n\n", "\n", "Monkey |  Starting items: |  Operation: new = old |  Test: divisible by |    If true: throw to monkey |    If false: throw to monkey|:| |, "])

oper = lambda old, op: old ** 2 if op == ["*", "old"] else old * op[1] if op[0] == "*" else old + op[1]

monkeys = {i[0][0]: {"it": i[1].copy(), "op": i[2], "div": i[3][0], "thr": [i[5][0], i[4][0]], "ins": 0} for i in parsed_input}
for r in range(20):
    for mkey, mval in monkeys.items():
        mval["it"] = list(map(lambda old: oper(old, mval["op"]) // 3, mval["it"]))
        mval["ins"] += len(mval["it"])
        while len(mval["it"]) > 0:
            check = mval["it"].pop(0)
            monkeys[mval["thr"][check % mval["div"] == 0]]["it"].append(check)
print(prod(sorted(map(lambda m: m["ins"], monkeys.values()))[-2:]))

monkeys = {i[0][0]: {"it": i[1], "op": i[2], "div": i[3][0], "thr": [i[5][0], i[4][0]], "ins": 0} for i in parsed_input}
divvy = math.lcm(*map(lambda m: m["div"], monkeys.values()))
for r in range(10000):
    for mkey, mval in monkeys.items():
        mval["it"] = list(map(lambda old: oper(old, mval["op"]) % divvy, mval["it"]))
        mval["ins"] += len(mval["it"])
        while len(mval["it"]) > 0:
            check = mval["it"].pop(0)
            monkeys[mval["thr"][check % mval["div"] == 0]]["it"].append(check)
print(prod(sorted(map(lambda m: m["ins"], monkeys.values()))[-2:]))