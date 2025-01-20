from utils import *
inp = input_file(2016, 7).strip()

parsed_input = parser(inp, ["\n"], lambda i: (" ".join((spl := re.split(r'\[([^\]]+)\]', i))[::2]), " ".join(spl[1::2]))
)

abba = r"([a-z])(?!\1)([a-z])\2\1"
p1 = sum(len(re.findall(abba, i[0])) >= 1 and not len(re.findall(abba, i[1])) >= 1 for i in parsed_input)

aba = r"([a-z])(?=(?!\1)([a-z])(\1))"
p2 = sum((len(arba := re.findall(aba, i[0])) >= 1 and any((ab[1] + ab[0] + ab[1]) in i[1] for ab in arba)) for i in parsed_input)

output(p1, p2)