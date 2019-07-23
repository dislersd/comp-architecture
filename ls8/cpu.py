"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Add 256 bytes of memory and
        # 8 general purpose registers
        # Also add properties for any internal registers you need, e.g. PC.

        self.PC = 0 # Program Counter, points to current executing instruction
        # self.memory = [0] * 256
        self.ram = [0] * 256
        self.register = [0] * 8

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

    def ram_read(self, address):
        return address
        pass

    def ram_write(self):
        pass

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8 opcode
            0b00000000,
            0b00001000, # operand (8)
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass