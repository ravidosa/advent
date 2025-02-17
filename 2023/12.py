from utils import *
inp = input_file(2023, 12).strip()

parsed_input = parser(inp, "{{s}} {{li,}}")

@functools.cache
def possible(string, run, groups):
    if len(string) == 0:
        return (run == 0 and len(groups) == 0) or (len(groups) == 1 and run != 0 and run == groups[0])
    else:
        if run != 0 and (len(string) - string.count(".") + run < sum(groups) or len(groups) == 0 or (string[0] == "." and run != groups[0])):
            return 0
        else:
            poss = 0
            if run != 0 and (string[0] == "." or (string[0] == "?" and run == groups[0])):
                poss += possible(string[1:], 0, groups[1:])
            if (string[0] == "#" or string[0] == "?"):
                poss += possible(string[1:], run + 1, groups)
            if (string[0] == "." or string[0] == "?") and run == 0:
                poss += possible(string[1:], 0, groups)
            return poss

p1 = sum(possible(string, 0, tuple(groups)) for string, groups in parsed_input)

p2 = sum(possible("?".join([string] * 5), 0, tuple(groups * 5)) for string, groups in parsed_input)

output(p1, p2)