from utils import *
inp = input_file(2025, 10).strip()

parsed_input = parser(inp, "[{{s}}] {{le }}")
parsed_input = [[i[0], [parser(p[1:-1], "{{li,}}") for p in i[1][:-1]], parser(i[1][-1][1:-1], "{{li,}}")] for i in parsed_input]

tot = 0
for i in parsed_input:
    button, press, jolt = i
    x = [z3.Int('x%s' % i) for i in range(len(press))]
    opt = z3.Optimize()
    opt.minimize(sum(x))
    for j in range(len(button)):
        opt.add(sum(x[k] * (j in press[k]) for k in range(len(press))) % 2 == (1 if button[j] == "#" else 0))
    for k in range(len(press)):
        opt.add(x[k] >= 0)
    opt.check()
    tot += int(str(opt.model().evaluate(opt.objectives()[0])))
p1 = tot

tot = 0
for i in parsed_input:
    button, press, jolt = i
    x = [z3.Int('x%s' % i) for i in range(len(press))]
    opt = z3.Optimize()
    opt.minimize(sum(x))
    for j in range(len(button)):
        opt.add(sum(x[k] * (j in press[k]) for k in range(len(press))) == jolt[j])
    for k in range(len(press)):
        opt.add(x[k] >= 0)
    opt.check()
    tot += int(str(opt.model().evaluate(opt.objectives()[0])))
p2 = tot


output(p1, p2)