from utils import *
inp = open("2015/input-19.txt", "r").read().strip().split("\n\n")

parsed_input = parser(inp[0], ["\n", " => "])

@functools.cache
def replace(molecule, reps):
    if reps == 0:
        return set([molecule])
    else:
        mols = set()
        for inp in parsed_input:
            for ind in functools.reduce(lambda x, y: x + [y.start()], re.finditer(inp[0], molecule), []):
                mols.update(replace(molecule[:ind] + inp[1] + molecule[ind + len(inp[0]):], reps - 1))
        return mols
med_mol = inp[1].strip()
print(len(replace(med_mol, 1)))

def atomize(molecule):
    atoms = []
    at = ""
    for i in range(len(molecule)):
        if molecule[i] == molecule[i].upper():
            atoms.append(at)
            at = molecule[i]
        else:
            at += molecule[i]
    atoms.append(at)
    return atoms[1:]
at = atomize(med_mol)
print(len(at) - 2 * at.count("Rn") - 2 * at.count("Y") - 1)