from utils import *
inp = input_file(2024, 3).strip()

mul = re.findall(r'mul\([0-9]+,[0-9]+\)', inp)
print(sum(map(lambda x: int(x[4:x.index(',')]) * int(x[x.index(',') + 1:-1]), mul)))

mul = re.findall(r'mul\([0-9]+,[0-9]+\)', "".join(map(lambda ff: ff.split("don't")[0], inp.split("do()"))))
print(sum(map(lambda x: int(x[4:x.index(',')]) * int(x[x.index(',') + 1:-1]), mul)))