#!/usr/local/bin/python3
from bitstring import BitArray

def NOP_00_11()
#Interation counter and Size of registers
count = 0
REGSIZE = 5


#Multiplicand and Multiplier
Multiplicand = BitArray(int=15, length=REGSIZE)
Multiplier = BitArray(int=-4, length=REGSIZE)
print(Multiplicand.bin, '*', Multiplier.bin, '(', Multiplicand.int, '*', Multiplier.int, ')')

#initialization
Line = BitArray('0b' + '0' * Multiplicand.length + str(Multiplier.bin) + '0')
print('Initialization:', Line.bin)

while count < Multiplicand.length:
    if str(Line[2 * Multiplicand.length - 1:].bin) == '00' or str(Line[2*Multiplicand.length - 1:].bin) == '11' :
        print('Register:', Line.bin, '--> 00 or 11-NOP -->', end=' ')
        Line.int >>= 1
        print('shift right -->',Line.bin)
    elif str(Line[2*Multiplicand.length - 1:].bin) == '01' :
        print('Register:', Line.bin, '--> 01-ADD -->', end=' ')
        extra_bit = BitArray(int=Line[:Multiplicand.length].int + Multiplicand.int, length = Multiplicand.length + 1)
        del extra_bit[0:1]
        Line.overwrite(extra_bit, 0)
        print('ADDED:', Line.bin, '-->', end=' ')
        Line.int >>= 1
        print('shift right -->',Line.bin)
    else:
        print('Register:', Line.bin, '--> 10-SUB -->', end=' ')
        extra_bit = BitArray(int=Line[:Multiplicand.length].int - Multiplicand.int, length = Multiplicand.length + 1)
        del extra_bit[0:1]
        Line.overwrite(extra_bit, 0)
        print('SUBTRACTED:', Line.bin, '-->', end= ' ')
        Line.int >>= 1
        print('shift right -->', Line.bin)
    count+=1
del Line[-1]
print('Binary register: ', Line.bin)
print('Decimal register: ', Line.int)

