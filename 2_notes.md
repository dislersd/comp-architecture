# Bitwise Operators

A B   A AND B
-------------
0 0      0
0 1      0
1 0      0
1 1      1

  1101011
& 1010010
---------
  1000010


    Boolean   Bitwise
OR     or       |
AND    and      &
XOR    N/A      ^
NOT    not      ~


And Masking
  101010101
& 111100000 <- AND mask
-----------
  101000000


Mask and Shift to run ADD command
## Shifting Bits

LEFT SHIFT <<
RIGHT SHIFT >>

10100000
11000000
--------
10000000 (128 in decimal)
^^
 1000000
  100000     <- Shifting right 6 places
   10000
    1000
      10
 0000010 (2 in decimal)

ir = 0b10100000 ADD
num_operands = (ir & 0b11000000) >> 6
dist_to_move_pc = num_operands + 1

## Subnet Mask
255.255.255.0

11111111.11111111.11111111.00000000

ip_add AND subnet_mask == network_number

192.168.2.4
255.255.255.0
(1) (1) (1) (0) <- mask
192.168.2.0




