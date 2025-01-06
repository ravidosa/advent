from utils import *
inp = "\n".join(sorted(open("2018/input-4.txt", "r").readlines()))

parsed_input = parser(inp, ["\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}\] Guard #", r"\n|\[[0-9]{4}-[0-9]{2}-[0-9]{2} 00:| begins shift", r"\]"])
sleep_dict = {}
for i in parsed_input:
    if i[0][0] not in sleep_dict:
        sleep_dict[i[0][0]] = [0] * 60
    sleep = False
    inst = 1
    minute = 0
    while minute < 60:
        if inst < len(i) and minute == i[inst][0]:
            sleep = i[inst][1] == "falls asleep"
            inst += 1
        sleep_dict[i[0][0]][minute] += sleep
        minute += 1

guard = max(sleep_dict.keys(), key=lambda k: sum(sleep_dict[k]))
minute = max(range(60), key=lambda m: sleep_dict[guard][m])
print(guard * minute)

guard = max(sleep_dict.keys(), key=lambda k: max(sleep_dict[k]))
minute = max(range(60), key=lambda m: sleep_dict[guard][m])
print(guard * minute)