from utils import *
inp = input_file(2016, 6).strip()

parsed_input = parser(inp, ["\n"])

char_freq = [{} for _ in range(len(parsed_input[0]))]
for i in parsed_input:
    for ind in range(len(i)):
        char_freq[ind][i[ind]] = char_freq[ind].get(i[ind], 0) + 1

print("".join(map(lambda i: max(char_freq[i], key=lambda k: char_freq[i][k]), range(len(parsed_input[0])))))

print("".join(map(lambda i: min(char_freq[i], key=lambda k: char_freq[i][k]), range(len(parsed_input[0])))))