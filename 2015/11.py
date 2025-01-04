from utils import *
inp = open("2015/input-11.txt", "r").read()

def increment(password):
    i = len(password) - 1
    while password[i] == "z" and i >= 0:
        password = password[:i] + "a" * (len(password) - i)
        i -= 1
    if i >= 0:
        password = password[:i] + lower[lower.index(password[i]) + 1] + password[i + 1:]
    return password

if all(map(lambda rep: rep not in inp, "iol")):
    password = increment(inp)
else:
    password = inp
    for rep in "iol":
        if rep in password:
            password = password[:password.index(rep)] + lower[lower.index(rep) + 1]  + "a" * (len(password) - password.index(rep) - 1)

secure = lambda inp: len(re.findall("|".join(map(lambda i: lower[i:i + 3], range(24))), inp)) >= 1 and not re.findall(r'i|o|l', inp) and re.findall(r'(.)\1', inp) and len(set(re.findall(r'(.)\1', inp))) >= 2

while not secure(password):
    password = increment(password)
print(password)

password = increment(password)
while not secure(password):
    password = increment(password)
print(password)