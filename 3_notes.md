# ALU and STACK

### ALU
* Can do integer math and comparisons
* Does math

### Stack
* push
* pop
* size/count
* peek at top
* resize
* stack pointer
* A pointer is an index to the memory array

### How does CPU stack work?
* Where is the data stored?
	* In RAM
* Why does stack grow down?
	* Program starts at bottom and grows up
	* Stack starts at top and goes down
	* This allows both to use the most amount of memory they need without collisions
	
## Why Stack?
* Extra storage
* Temporarily store information
* Clears up space on the registers for them to keep working
* Stores local variables
* Keeping track of numbers you need later but you ran out of registers to hold them in
* 

## Registers

* What can general purpose register do that internal register cannot do?
    - They can hold varied data like operands and allow you to write extra functionality
    - Theres no instruction that can change the PC directly
    - Special Purpose registers have one task like pointing to the program, but you don't
