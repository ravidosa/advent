from utils import *
inp = input_file(2016, 8).strip()

parsed_input = parser(inp, ["\n", r"rotate |x=|y=| by |x| "])

W, H = 50, 6

pixels = {}
for i in parsed_input:
    new_pixels = pixels.copy()
    if i[0] == "rect":
        for c in range(i[1]):
            for r in range(i[2]):
                new_pixels[c + r * 1j] = 1
    elif i[0] == "row":
        for c in range(W):
            new_pixels[((c + i[2]) % W) + i[1] * 1j] = pixels.get(c + i[1] * 1j, 0)
    elif i[0] == "column":
        for r in range(H):
            new_pixels[i[1] + ((r + i[2]) % H) * 1j] = pixels.get(i[1] + r * 1j, 0)
    pixels = new_pixels
p1 = sum(pixels.values())

p2 = "\n".join(map(lambda r: "".join(map(lambda c: "#" if pixels.get(c + r * 1j, 0) == 1 else " ", range(W))), range(H)))

output(p1, p2)