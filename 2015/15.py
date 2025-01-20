from utils import *
inp = input_file(2015, 15).strip()

parsed_input = parser(inp, ["\n", r": capacity |, durability |, flavor |, texture |, calories"])

x = [z3.Int('x%s' % i) for i in range(len(parsed_input))]
opt = z3.Optimize()
opt.add(sum(x) == 100)
for j in range(5):
    opt.add(sum([x[i] * parsed_input[i][j + 1] for i in range(len(parsed_input))]) >= 0)
opt.maximize(prod(map(lambda j: sum([x[i] * parsed_input[i][j + 1] for i in range(len(parsed_input))]), range(4))))
opt.check()
p1 = str(opt.model().evaluate(opt.objectives()[0]))[1:]

opt.add(sum([x[i] * parsed_input[i][5] for i in range(len(parsed_input))]) == 500)
opt.maximize(prod(map(lambda j: sum([x[i] * parsed_input[i][j + 1] for i in range(len(parsed_input))]), range(4))))
opt.check()
p2 = str(opt.model().evaluate(opt.objectives()[0]))[1:]

output(p1, p2)