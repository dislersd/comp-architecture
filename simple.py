import sys

PRINT_DYL = 1
HALT = 2
PRINT_NUM = 3

memory = [
    PRINT_DYL,
    PRINT_DYL,
    PRINT_NUM,  # opcode == instruction
    12,        # operand == argument
    HALT
]

pc = 0  # Program counter, points to currently-executing instruction

running = True

while running:
    command = memory[pc]

    if command == PRINT_DYL:
        print("Dyl!")
        pc += 1

    elif command == PRINT_NUM:
        operand = memory[pc + 1]
        print(operand)
        pc += 2

    elif command == HALT:
        running = False
        pc += 1

    else:
        print(f"unknown instruction {command}")
        sys.exit(1)
