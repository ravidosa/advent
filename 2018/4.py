from utils import *
inp = "\n".join(sorted(input_file(2018, 4).split("\n"))[1:])

parsed_input = parser(inp, "[{{i}}-{{i}}-{{i}} {{i}}:{{i}}] {{e}}")

sleep_dict = {}
for i in parsed_input:
    if "Guard" in i:
        id = int(i[6][1:])
        if id not in sleep_dict:
            sleep_dict[id] = [0] * 60
        curr_guard = id
        sleep = False
        minute = 0
    else:
        while minute < 60:
            if minute == i[4]:
                sleep = i[-1] == "asleep"
                break
            sleep_dict[curr_guard][minute] += sleep
            minute += 1

guard = max(sleep_dict.keys(), key=lambda k: sum(sleep_dict[k]))
minute = max(range(60), key=lambda m: sleep_dict[guard][m])
p1 = guard * minute

guard = max(sleep_dict.keys(), key=lambda k: max(sleep_dict[k]))
minute = max(range(60), key=lambda m: sleep_dict[guard][m])
p2 = guard * minute

output(p1, p2)