import collections

POSITION = 0
IMMEDIATE = 1
RELATIVE = 2

ADD = 1
MUL = 2
IN = 3
OUT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADD_RELATIVE_BASE = 9
HALT = 99

READ = 0
WRITE = 1

OPS = {
    ADD:                (READ, READ, WRITE,),
    MUL:                (READ, READ, WRITE,),
    IN:                 (WRITE,),
    OUT:                (READ,),
    JUMP_TRUE:          (READ, READ),
    JUMP_FALSE:         (READ, READ),
    LESS_THAN:          (READ, READ, WRITE,),
    EQUALS:             (READ, READ, WRITE,),
    ADD_RELATIVE_BASE:  (READ,)
}

class Computer:
    def __init__(self, program, inp=[]):
        self.reg = program
        self.inp = collections.deque(inp)
        self.out = []
        self.pointer = None
        self.relative_base = None
    def __getitem__(self, ind):
        if 0 <= ind < len(self.reg):
            return self.reg[ind]
    def __setitem__(self, ind, val):
        if 0 <= ind < len(self.reg):
            self.reg[ind] = val
    def params(self, param_type, modes):
        param_list = [None] * 4
        for i, typ in enumerate(param_type):
            r = self[self.pointer + 1 + i]
            modes, mode = divmod(modes, 10)
            if mode == RELATIVE:
                r += self.relative_base
            if mode in [POSITION, RELATIVE]:
                if r < 0:
                    raise Exception(f"Invalid negative index ({r})")
                elif r >= len(self.reg):
                    self.reg += [0] * (r + 1 - len(self.reg))
                if typ == READ:
                    r = self[r]
                elif typ != WRITE:
                    raise Exception(f"Invalid parameter type ({typ})")
            elif mode == IMMEDIATE:
                if typ == WRITE:
                    raise Exception(f"Writing in immediate mode")
            else:
                raise Exception(f"Invalid mode ({mode})")
            param_list[i] = r
        return param_list
    def push_in(self, inp):
        self.inp.extend(inp)
    def pop_out(self):
        out = self.out
        self.out = []
        return out
    def run(self):
        self.pointer = 0
        self.relative_base = 0
        while self[self.pointer] != HALT:
            instr = self[self.pointer]
            modes, opcode = divmod(instr, 100)
            if opcode not in OPS:
                raise Exception(f"Invalid operation {opcode}")
            param_type = OPS[opcode]
            p1, p2, p3, p4 = self.params(param_type, modes)
            self.pointer += 1 + len(param_type)
            if opcode == ADD:
                self[p3] = p1 + p2
            elif opcode == MUL:
                self[p3] = p1 * p2
            elif opcode == IN:
                while len(self.inp) == 0:
                    yield
                self[p1] = self.inp.popleft()
            elif opcode == OUT:
                self.out.append(p1)
            elif opcode == JUMP_TRUE:
                if p1 != 0:
                    self.pointer = p2
            elif opcode == JUMP_FALSE:
                if p1 == 0:
                    self.pointer = p2
            elif opcode == LESS_THAN:
                self[p3] = 1 if p1 < p2 else 0
            elif opcode == EQUALS:
                self[p3] = 1 if p1 == p2 else 0
            elif opcode == ADD_RELATIVE_BASE:
                self.relative_base += p1
            else:
                raise Exception(f"Unimplemented opcode {opcode}")
class System:
    OUT = object()
    def __init__(self, computers):
        self.computers = computers
        self.connections = [[] for _ in self.computers]
        self.paused = collections.deque(range(len(self.computers)))
        self.signals = [computer.run() for computer in self.computers]
        self.out = []
    def connect(self, inp, out):
        self.connections[inp].append(out)
    def run(self):
        while self.paused:
            currc = self.paused.popleft()
            try:
                next(self.signals[currc])
                self.paused.append(currc)
            except StopIteration:
                pass
            out = self.computers[currc].pop_out()
            for conn in self.connections[currc]:
                if conn is System.OUT:
                    self.out.extend(out)
                else:
                    self.computers[conn].push_in(out)
        return self.out