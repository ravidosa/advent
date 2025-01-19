from utils import *
inp = input_file(2015, 17).strip()

parsed_input = parser(inp, ["\n"])

container_count = {}
def combos(eggnog, containers, used):
    if eggnog < 0 or (eggnog > 0 and len(containers) == 0):
        return 0
    elif eggnog == 0:
        container_count[used] = container_count.get(used, 0) + 1
        return 1
    else:
        return combos(eggnog - containers[0], containers[1:], used + 1) + combos(eggnog, containers[1:], used)

EGGNOG = 150
print(combos(EGGNOG, tuple(parsed_input), 0))

print(container_count[min(container_count.keys())])