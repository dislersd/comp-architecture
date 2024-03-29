"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Add 256 bytes of memory and
        # 8 general purpose registers
        # Also add properties for any internal registers you need, e.g. PC.

        self.PC = 0  # Program Counter, points to current executing instruction
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.HLT = 0b00000001
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.MUL = 0b10100010
        self.ADD = 0b10100000
        self.CMP = 0b10100111
        self.JMP = 0b01010100
        self.JEQ = 0b01010101
        self.JNE = 0b01010110
        self.FL = 0b00000000
        self.SP = 0b00000111
        self.PUSH = 0b01000101
        self.POP = 0b01000110
        self.CALL = 0b01010000
        self.RET = 0b00010001

        '''
        Internal Registers
        * PC: Program Counter, address of the currently executing instruction
        * IR: Instruction Register, contains a copy of the currently executing instruction
        * MAR: Memory Address Register, holds the memory address we're reading or writing
        * MDR: Memory Data Register, holds the value to write or the value just read
        * FL: Flags, see below

        8 general-purpose 8-bit numeric registers R0-R7
        * R5 is reserved as the interrupt mask (IM)
        * R6 is reserved as the interrupt status (IS)
        * R7 is reserved as the stack pointer (SP)
        '''

    # Memory Address Register
    # Memory Data Register
    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def load(self):
        """Load a program into memory."""

        self.PC = 0

        if len(sys.argv) != 2:
            print(f"usage: {sys.argv[0]} filename")
            sys.exit(1)

        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    num = line.split('#', 1)[0]

                    if num.strip() == '':  # ignore comment only lines
                        continue

                    num = int(num, 2)
                    self.ram[self.PC] = num
                    self.PC += 1

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] =  self.reg[reg_a] + self.reg[reg_b]

        elif op == "MUL":
            self.reg[reg_a] = self.reg[reg_a] * self.reg[reg_b]

        elif op == "CMP":
            # FL = 00000LGE
            if self.reg[reg_a] < self.reg[reg_b]:
                self.FL = 0b00000100 # "L" set to 1
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.FL = 0b00000010 # "G" set to 1
            elif self.reg[reg_a] == self.reg[reg_b]:
                self.FL = 0b00000001 # "E" set tp 1


        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            # self.fl,
            # self.ie,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        running = True
        self.PC = 0
        self.reg[self.SP] = 0b11111111

        while running:
            IR = self.ram[self.PC]

            if IR == self.HLT:
                running = False
                self.PC += 1

            elif IR == self.LDI:
                self.reg[self.ram_read(self.PC + 1)
                         ] = self.ram_read(self.PC + 2)
                self.PC += 3

            elif IR == self.PRN:
                print(self.reg[self.ram_read(self.PC + 1)])
                self.PC += 2

            elif IR == self.MUL:
                self.alu('MUL', self.ram_read(self.PC + 1),
                         self.ram_read(self.PC + 2))
                self.PC += 3

            elif IR == self.ADD:
                self.alu('ADD', self.ram_read(self.PC + 1),
                         self.ram_read(self.PC + 2))
                self.PC += 3

            elif IR == self.PUSH:
                self.reg[self.SP] -= 1
                regnum = self.ram[self.PC + 1]
                value = self.reg[regnum]
                self.ram[self.reg[self.SP]] = value
                self.PC += 2

            elif IR == self.POP:
                value = self.ram[self.reg[self.SP]]
                regnum = self.ram[self.PC + 1]
                self.reg[regnum] = value
                self.reg[self.SP] += 1
                self.PC += 2

            elif IR == self.CALL:
                return_addr = self.PC + 2
                self.reg[self.SP] -= 1
                self.ram[self.reg[self.SP]] = return_addr
                regnum = self.ram[self.PC + 1] # 1
                subroutine_addr = self.reg[regnum]
                self.PC = subroutine_addr

            elif IR == self.RET:
                return_addr = self.ram[self.reg[self.SP]]
                self.reg[self.SP] += 1
                self.PC = return_addr

            elif IR == self.CMP:
                self.alu("CMP", self.ram_read(self.PC + 1), self.ram_read(self.PC + 2))
                self.PC += 3

            elif IR == self.JMP:
                memory_addr = self.ram[self.PC + 1]
                self.PC = self.reg[memory_addr]

            elif IR == self.JEQ:
                if self.FL == 0b00000001:
                    memory_addr = self.ram[self.PC + 1]
                    self.PC = self.reg[memory_addr]
                else:
                    self.PC += 2

            elif IR == self.JNE:
                if self.FL != 0b00000001:
                    memory_addr = self.ram[self.PC + 1]
                    self.PC = self.reg[memory_addr]
                else:
                    self.PC += 2
                    
            else:
                print(f"unknown instruction {IR}")
                sys.exit(1)

                10100111


'''
0b10000010,  # LDI R0,8 opCode
0b00000000,
0b00001000,  # operand (8)
0b01000111,  # PRN R0
0b00000000,
0b00000001
'''