
INPUT = '02.txt'
TEST_INPUT = '02_test.txt'
INPUTFILE = INPUT

with open(INPUTFILE) as f:
    values = list(map(int, f.readline().split(',')))

def runProgram(program):
    for i in range(len(program)//4):
        opcode = program[i*4]
        pos1 = program[i*4+1]
        pos2 = program[i*4+2]
        pos3 = program[i*4+3]
        if opcode == 1:
            program[pos3] = program[pos1] + program[pos2]
        elif opcode == 2:
            program[pos3] = program[pos1] * program[pos2]
        elif opcode == 99:
            break
        else:
            raise Exception('Error')

    return program[0]

for noun in range(100):
    for verb in range(100):
        memory = values.copy()
        memory[1] = noun
        memory[2] = verb
        try:
            answer = runProgram(memory)
        except Exception:
            continue

        if answer == 19690720:
            part2 = 100*noun + verb
            break

print(f'Part 1: {runProgram(values)}')
print(f'Part 2: {part2}')

