from utils import *
inp = input_file(2024, 3).strip()

mul = re.findall(r'mul\([0-9]+,[0-9]+\)', inp)
p1 = sum(map(lambda x: prod(parser(x, [r"mul\(|,|\)"])), mul))

mul = re.findall(r'mul\([0-9]+,[0-9]+\)', "".join(map(lambda ff: ff.split("don't")[0], inp.split("do()"))))
p2 = sum(map(lambda x: prod(parser(x, [r"mul\(|,|\)"])), mul))

output(p1, p2)