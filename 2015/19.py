from utils import *
inp = input_file(2015, 19).strip().split("\n\n")

parsed_input = parser(inp[0], "{{s}} => {{s}}")
med_mol = inp[1].strip()

@functools.cache
def replace(molecule, reps):
    if reps == 0:
        return set([molecule])
    else:
        mols = set()
        for i in parsed_input:
            for ind in functools.reduce(lambda x, y: x + [y.start()], re.finditer(i[0], molecule), []):
                mols.update(replace(molecule[:ind] + i[1] + molecule[ind + len(i[0]):], reps - 1))
        return mols
p1 = len(replace(med_mol, 1))

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
p2 = len(at) - 2 * at.count("Rn") - 2 * at.count("Y") - 1

output(p1, p2)