from utils import *
inp = open("2022/input-11.txt", "r").read()

parsed_input = parser(inp, ["\n\n", "\n", "Monkey |  Starting items: |  Operation: new = old |  Test: divisible by |    If true: throw to monkey |    If false: throw to monkey|:| |, "])
oper = lambda old, op: old ** 2 if op == ["*", "old"] else old * op[1] if op[0] == "*" else old + op[1]

monkeys = {inp[0][0]: {"it": inp[1].copy(), "op": inp[2], "div": inp[3][0], "thr": [inp[5][0], inp[4][0]], "ins": 0} for inp in parsed_input}
for r in range(20):
    for mkey, mval in monkeys.items():
        mval["it"] = list(map(lambda old: oper(old, mval["op"]) // 3, mval["it"]))
        mval["ins"] += len(mval["it"])
        while len(mval["it"]) > 0:
            check = mval["it"].pop(0)
            monkeys[mval["thr"][check % mval["div"] == 0]]["it"].append(check)
print(prod(sorted(map(lambda m: m["ins"], monkeys.values()))[-2:]))

monkeys = {inp[0][0]: {"it": inp[1], "op": inp[2], "div": inp[3][0], "thr": [inp[5][0], inp[4][0]], "ins": 0} for inp in parsed_input}
divvy = math.lcm(*map(lambda m: m["div"], monkeys.values()))
for r in range(10000):
    for mkey, mval in monkeys.items():
        mval["it"] = list(map(lambda old: oper(old, mval["op"]) % divvy, mval["it"]))
        mval["ins"] += len(mval["it"])
        while len(mval["it"]) > 0:
            check = mval["it"].pop(0)
            monkeys[mval["thr"][check % mval["div"] == 0]]["it"].append(check)
print(prod(sorted(map(lambda m: m["ins"], monkeys.values()))[-2:]))