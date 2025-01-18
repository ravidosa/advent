from utils import *
inp = open("2020/input-3.txt", "r").read().strip()

parsed_input = inp.replace(".", "0").replace("#", "1")

grid = Grid(parsed_input)
print(sum(map(lambda r: grid.get_pos((r, 3 * r % grid.cols)), range(grid.rows))))

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
print(prod(map(lambda pair: sum(map(lambda r: grid.get_pos((pair[0] * r, pair[1] * r % grid.cols)), range(grid.rows // pair[0]))), slopes)))