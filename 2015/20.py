from utils import *
inp = input_file(2015, 20).strip()

def first_house(n, stop=math.inf):
    target = math.ceil(int(inp) / n)
    presents = {}
    for i in range(1, target + 1):
        for j in range(1, min(stop, target // i) + 1):
            presents[i * j] = presents.get(i * j, 0) + i
            if i == 1 and presents[i * j] >= target:
                return min(presents, key=lambda i: i if presents[i] >= target else target)
    return min(presents, key=lambda i: i if presents[i] >= target else target)

p1 = first_house(10)

p2 = first_house(11, 50)

output(p1, p2)