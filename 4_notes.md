1. When is the ALU activated in the CPU?

    The ALU or Arithmetic Logic Unit is activated whenever math or logic occurs in a program. The ALU is responsible for performing arithmetic and comparisons on  

2. Why is a CPU stack useful in assembly language?

    It's useful because it provides extra space to store information and leaves room for registers to keep working. The stack allows for subroutines and local variables making programs a lot more dynamic in what they can do. The stack can hold return adresses and let you jump around the code and return the PC back to where it was before a subroutine occured. Memory is allocated on the stack for local variables and when your return from the function the local variables pop off the stack. 

3. Convert the 8-bit binary number 0bXXXXXXXX (PM's choice) to hex.

    To convert binary to hex split the binary into nibbles (4 bits), convert the nibbles to hex and put the hex units together

    0b 0101 1001  = 809 decimal and 59 hex
        5   9