from utils import *
inp = input_file(2016, 8).strip()

parsed_input = parser(inp, "{{lerotate |x=|y=| by |x| }}")

W, H = 50, 6

pixels = {}
for i in parsed_input:
    new_pixels = pixels.copy()
    com = i[0]
    if com[0] == "rect":
        for c in range(com[1]):
            for r in range(com[2]):
                new_pixels[c + r * 1j] = 1
    elif com[0] == "row":
        for c in range(W):
            new_pixels[((c + com[2]) % W) + com[1] * 1j] = pixels.get(c + com[1] * 1j, 0)
    elif com[0] == "column":
        for r in range(H):
            new_pixels[com[1] + ((r + com[2]) % H) * 1j] = pixels.get(com[1] + r * 1j, 0)
    pixels = new_pixels
p1 = sum(pixels.values())

p2 = "\n".join("".join("##" if pixels.get(c + r * 1j, 0) == 1 else "  " for c in range(W)) for r in range(H))

output(p1, p2)