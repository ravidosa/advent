from utils import *
import re
inp = open("2015/input-12.txt", "r").read()

print(sum(map(int, re.findall(r'-?[0-9]+', inp))))

parsed_input = eval(inp)
def red_sum(obj):
    if type(obj) == int:
        return int(obj)
    elif type(obj) == list:
        return sum(map(red_sum, obj))
    elif type(obj) == dict:
        if "red" in obj.values():
            return 0
        else:
            return sum(map(red_sum, obj.values()))
    return 0
print(red_sum(parsed_input))