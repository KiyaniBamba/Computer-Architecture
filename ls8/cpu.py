"""CPU functionality."""

import sys

HLT = 0b00000001
PRN = 0b01000111
LDI = 0b10000010
ADD = 0b10100000
MUL = 0b10100010


class CPU:
    """Main CPU class."""

    def load(self):
        """Load a program into memory."""

        try:
            address = 0
            with open(filename) as f:
                for line in f:
                    # split line before and after comment symbol
                    comment_split = line.split("#")

        # For now, we've just hardcoded a program:
                    # extract our number
                    num = comment_split[0].strip()  # trim whitespace
            if num == '':
                continue  # ignore blank lines

                # convert our binary string to a number
                val = int(num, 2)

                # store val at address in memory
                self.ram_write(val, address)

                address += 1

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {filename} not found")
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

            self.reg[operand_a] = operand_b
            inc_size = 3

            elif cmd == ADD:
                self.alu("ADD", operand_a, operand_b)
                inc_size = 3

            elif cmd == MUL:
                self.alu("MUL", operand_a, operand_b)
                inc_size = 3

            self.pc += inc_size
