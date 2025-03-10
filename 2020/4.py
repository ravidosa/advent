from utils import *
inp = input_file(2020, 4).strip().replace("\n", " ").replace("  ", "\n")

parsed_input = parser(inp, "{{nls |:}}")

passports = [{f[0]: f[1] for f in i} for i in parsed_input]

valid = lambda p: len(p.keys()) == 8 or (len(p.keys()) == 7 and "cid" not in p.keys())
p1 = sum(map(valid, passports))

valid = lambda p: (len(p.keys()) == 8 or (len(p.keys()) == 7 and "cid" not in p.keys())) and 1920 <= int(p["byr"]) <= 2002 and 2010 <= int(p["iyr"]) <= 2020 and 2020 <= int(p["eyr"]) <= 2030 and ((p["hgt"][-2:] == "cm" and 150 <= int(p["hgt"][:-2]) <= 193) or (p["hgt"][-2:] == "in" and 59 <= int(p["hgt"][:-2]) <= 176)) and re.match(r'^#(?:[0-9a-f]{3}){2}$', p["hcl"]) != None and p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and p["pid"].isdigit() and len(p["pid"]) == 9
p2 = sum(map(valid, passports))

output(p1, p2)