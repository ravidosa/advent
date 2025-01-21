from utils import *
inp = input_file(2019, 8).strip()

w, h = 25, 6

layers = [inp[i:i + w * h] for i in range(0, len(inp), w * h)]
corr_check = min(layers, key=lambda l: l.count("0"))
p1 = corr_check.count("1") * corr_check.count("2")

image = ["2"] * w * h
for l in layers:
    image = [l[i] if image[i] == "2" else image[i] for i in range(w * h)]
print(image)
image = "".join(image).replace("0", " ").replace("1", "#")
p2 = "\n".join(image[i:i + w] for i in range(0, w * h, w))

output(p1, p2)