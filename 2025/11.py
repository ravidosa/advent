from utils import *
inp = input_file(2025, 11).strip()

parsed_input = parser(inp, "{{s}}: {{ls }}")

edges = {v[0]: v[1] for v in parsed_input}
@functools.cache
def paths(start, stop):
    if start == stop:
        return 1
    return sum(paths(step, stop) for step in edges.get(start, []))

p1 = paths("you", "out")

p2 = paths("svr", "dac") * paths("dac", "fft") * paths("fft", "out") + paths("svr", "fft") * paths("fft", "dac") * paths("dac", "out")

output(p1, p2)