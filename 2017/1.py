from utils import *
inp = input_file(2017, 1).strip()

parsed_input = parser(inp, "{{li|}}", split=False)

captcha = parsed_input[0]

p1 = sum(captcha[i] * (captcha[i] == captcha[(i + 1) % len(captcha)]) for i in range(len(captcha)))

p2 = sum(captcha[i] * (captcha[i] == captcha[(i + len(captcha) // 2) % len(captcha)]) for i in range(len(captcha)))

output(p1, p2)