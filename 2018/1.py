from utils import *
inp = input_file(2018, 1).strip()

parsed_input = parser(inp, ["\n"])

print(sum(parsed_input))

freq = 0
freqs = set()
i = 0
while freq not in freqs:
    freqs.add(freq)
    freq += parsed_input[i % len(parsed_input)]
    i += 1
print(freq)