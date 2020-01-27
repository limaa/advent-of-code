import logging

INPUT = '05.txt'
INPUTFILE = INPUT

with open(INPUTFILE) as f:
    values = list(map(int, f.readline().split(',')))

def runProgram(mem):
    last_output = None
    pc = 0
    while(pc<len(mem)):
        instruction = str(mem[pc])
        opcode = int(instruction[-2:])
        mode = instruction[:-2]

        logging.debug(f'PC: {pc}')
        logging.debug(f'OPCODE: {opcode}')
        logging.debug(f'MODE: {mode}')

        if opcode == 1:
            pos1 = pc+1 if len(mode) > 0 and mode[-1] == '1' else mem[pc+1]
            pos2 = pc+2 if len(mode) > 1 and mode[-2] == '1' else mem[pc+2]
            pos3 = pc+3 if len(mode) > 2 and mode[-3] == '1' else mem[pc+3]
            mem[pos3] = mem[pos1] + mem[pos2]
            pc += 4

            logging.debug(f'Parameters mode: {mode}')
            logging.debug(f'pos1: {pos1}')
            logging.debug(f'pos2: {pos2}')
            logging.debug(f'pos3: {pos3}')
            logging.debug(f'operation: {mem[pos1]} + {mem[pos2]}')

        elif opcode == 2:
            pos1 = pc+1 if len(mode) > 0 and mode[-1] == '1' else mem[pc+1]
            pos2 = pc+2 if len(mode) > 1 and mode[-2] == '1' else mem[pc+2]
            pos3 = pc+3 if len(mode) > 2 and mode[-3] == '1' else mem[pc+3]
            mem[pos3] = mem[pos1] * mem[pos2]
            pc += 4

            logging.debug(f'Parameters mode: {mode}')
            logging.debug(f'pos1: {pos1}')
            logging.debug(f'pos2: {pos2}')
            logging.debug(f'pos3: {pos3}')
            logging.debug(f'operation: {mem[pos1]} * {mem[pos2]}')

        elif opcode == 3:
            print('Waiting for user input:')
            pos = mem[pc+1]
            mem[pos] = int(input())
            pc += 2

            logging.debug(f'pos: {pos}')

        elif opcode == 4:
            pos = pc+1 if len(mode) > 0 and mode[-1] == '1' else mem[pc+1]
            last_output = mem[pos]
            pc += 2

            logging.debug(f'OUTPUT: {mem[pos]}')

        elif opcode == 5:
            pos1 = pc+1 if len(mode) > 0 and mode[-1] == '1' else mem[pc+1]
            pos2 = pc+2 if len(mode) > 1 and mode[-2] == '1' else mem[pc+2]
            pc = mem[pos2] if mem[pos1] != 0 else pc+3
            
            logging.debug(f'Parameters mode: {mode}')
            logging.debug(f'pos1: {pos1}')
            logging.debug(f'pos2: {pos2}')
            logging.debug(f'PC = {mem[pos2]} if {mem[pos1]} != 0 else {pc+3}')
    
        elif opcode == 6:
            pos1 = pc+1 if len(mode) > 0 and mode[-1] == '1' else mem[pc+1]
            pos2 = pc+2 if len(mode) > 1 and mode[-2] == '1' else mem[pc+2]
            pc = mem[pos2] if mem[pos1] == 0 else pc+3
            
            logging.debug(f'Parameters mode: {mode}')
            logging.debug(f'pos1: {pos1}')
            logging.debug(f'pos2: {pos2}')
            logging.debug(f'PC = {mem[pos2]} if {mem[pos1]} == 0 else {pc+3}')

        elif opcode == 7:
            pos1 = pc+1 if len(mode) > 0 and mode[-1] == '1' else mem[pc+1]
            pos2 = pc+2 if len(mode) > 1 and mode[-2] == '1' else mem[pc+2]
            pos3 = pc+3 if len(mode) > 2 and mode[-3] == '1' else mem[pc+3]
            mem[pos3] = 1 if mem[pos1] < mem[pos2] else 0
            pc += 4
            
            logging.debug(f'Parameters mode: {mode}')
            logging.debug(f'pos1: {pos1}')
            logging.debug(f'pos2: {pos2}')
            logging.debug(f'pos3: {pos3}')
            logging.debug(f'output = 1 if {mem[pos1]} < {mem[pos2]} else 0')

        elif opcode == 8:
            pos1 = pc+1 if len(mode) > 0 and mode[-1] == '1' else mem[pc+1]
            pos2 = pc+2 if len(mode) > 1 and mode[-2] == '1' else mem[pc+2]
            pos3 = pc+3 if len(mode) > 2 and mode[-3] == '1' else mem[pc+3]
            mem[pos3] = 1 if mem[pos1] == mem[pos2] else 0
            pc += 4
            
            logging.debug(f'Parameters mode: {mode}')
            logging.debug(f'pos1: {pos1}')
            logging.debug(f'pos2: {pos2}')
            logging.debug(f'pos3: {pos3}')
            logging.debug(f'output = 1 if {mem[pos1]} == {mem[pos2]} else 0')

        elif opcode == 99:
            logging.debug(f'Program execution halted.')
            break
        else:
            raise Exception('Error')
    return last_output

# logging.basicConfig(level=logging.DEBUG)
print(f'Part 1 (use input=1):')
print(runProgram(values.copy()))
print(f'Part 2 (use input=5):')
print(runProgram(values.copy()))
