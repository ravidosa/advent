from utils import *
inp = input_file(2015, 11).strip()

def increment(password):
    i = len(password) - 1
    while password[i] == "z" and i >= 0:
        password = password[:i] + "a" * (len(password) - i)
        i -= 1
    if i >= 0:
        password = password[:i] + lower[lower.index(password[i]) + 1] + password[i + 1:]
    return password
secure = lambda password: len(re.findall("|".join(lower[i:i + 3] for i in range(24)), password)) >= 1 and not re.findall(r'i|o|l', password) and re.findall(r'(.)\1', password) and len(set(re.findall(r'(.)\1', password))) >= 2

if all(rep not in inp for rep in "iol"):
    password = increment(inp)
else:
    password = inp
    for rep in "iol":
        if rep in password:
            password = password[:password.index(rep)] + lower[lower.index(rep) + 1]  + "a" * (len(password) - password.index(rep) - 1)
while not secure(password):
    password = increment(password)
p1 = password

password = increment(password)
while not secure(password):
    password = increment(password)
p2 = password

output(p1, p2)