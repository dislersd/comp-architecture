base 10 0-9

base 2 (binary) 0-1
2 is 10

base 16 0-9, A-F

base 64 A-Z, a-z, 0-9, +, /

representring 132
in binary => 10000100
in hexidecimal => 84

* Python assumes base 10 unless specified otherwise
* putting "0b" before number tells Python to use binary

x = 0b101011 -> 43
y = x + 10 -> 53

print(x, y)

* to print out in binary
    print("{:b} {}".format(x, y))
            |    |
            |    print default (base 10)
            :b means print in binary


in decimal (base 10)

1000s place
|100s
||10s
|||1s
||||
1234

in binary (base 2)
8s
| 4s
| | 2s
| | | 1s
1 1 0 1

1000s (8)
| 100s (4)
| | 10s (2)
| | | 1s (1)
1 1 0 1

0b1101 = ?? decimal
8 + 4 + 1 = 13

0b10101011 = ?? decimal

128 + 32 + 8 + 2 + 1 = 171

17 decimal
  16   +    1
  |         |      
0b10000 + 0b1 = 0b10001


0b1111 = 15 in decimal
1 + 2 + 4 + 8

0x means hex

0xF = 15 in hexidecimal

To convert binary to hex split up binary into "nibbles" (4 digits)

0b 1010 0100
0x  A    4

0b10100100 = 0xA4

0x  C     8
0b 1100 1000

0b11111111 always a power of 2 minus 1

2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 256
256 - 1 = 0b11111111 


0b 1111 1111 = 255  (largest number you can fit in a byte)
0x  F    F

