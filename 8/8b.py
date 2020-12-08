data = open("input.txt").read().split("\n")

class BootCode:
    def __init__(self, program):
        self.program = program
        self.acc = 0
        self.ip = 0

    def step(self):
        if self.ip >= len(self.program):
            return True
        instruction, value = self.program[self.ip].split()
        value = int(value)
        if instruction == "acc":
            self.acc += value
            self.ip += 1
        elif instruction == "jmp":
            self.ip += value
        elif instruction == "nop":
            self.ip += 1

        return False

for i in range(len(data)):
    old_instruction, _ = data[i].split()
    new_instruction = old_instruction
    if "jmp" in old_instruction:
        new_instruction = "nop"
        data[i] = data[i].replace("jmp", new_instruction)
    elif "nop" in old_instruction:
        new_instruction = "jmp"
        data[i] = data[i].replace("nop", new_instruction)

    bc = BootCode(data)
    executed = set()
    while True:
        if bc.ip in executed:
            break
        executed.add(bc.ip)
        if bc.step():
            print(bc.acc)

    data[i] = data[i].replace(new_instruction, old_instruction)
