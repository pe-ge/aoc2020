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

bc = BootCode(data)
executed = set()
while True:
    if bc.ip in executed:
        print(bc.acc)
        break
    executed.add(bc.ip)
    bc.step()
