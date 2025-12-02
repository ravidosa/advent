from utils import *
inp = input_file(2025, 2).strip()

parsed_input = parser(inp, "{{li-|,}}")

firsts = parsed_input[::2]
lasts = parsed_input[1::2]

def reppy(first, last, length):
    invalids = set()
    dig_first = len(str(first))
    dig_last = len(str(last))
    if dig_first % length == 0:
        div_first = int(str(first)[:dig_first // length])
    else:
        div_first = int("1" + "0" * (dig_first // length))
    if dig_last % length == 0:
        div_last = int(str(last)[:dig_last // length])
    else:
        div_last = int("9" * (dig_last // length))
    for i in range(div_first, div_last + 1):
            chk = int(str(i) * length)
            if chk >= first and chk <= last:
                invalids.add(chk)
    return invalids

invalids = set()
for first, last in zip(firsts, lasts):
    invalids.update(reppy(first, last, 2))
p1 = sum(invalids)

invalids = set()
for first, last in zip(firsts, lasts):
    for l in range(2, len(str(last)) + 1):
        invalids.update(reppy(first, last, l))
p2 = sum(invalids)

output(p1, p2)