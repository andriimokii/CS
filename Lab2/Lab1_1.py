#!/usr/local/bin/python3
from bitstring import BitArray
import sys
REGSIZE = 3
counter = 0
MINUS = False

#dividend and divisor
idend = BitArray(int=3, length=3)
isor = BitArray(int=2, length=3)
print(idend.bin, '/', isor.bin, '(', idend.int, '/', isor.int, ')')
if isor.int == 0:
    print("division by zero")
    sys.exit()
elif idend.int < 0 and isor.int < 0:
    idend.int -= 1
    idend.invert()
    isor.int -= 1
    isor.invert()
elif idend.int < 0 and isor.int > 0:
    idend.int -= 1
    idend.invert()
    MINUS = True
elif idend.int > 0 and isor.int < 0:
    isor.int -= 1
    isor.invert()
    MINUS = True
#Start: Place Dividend in Remainder and add bit to Quotient
Rem = BitArray('0b' + '0' * REGSIZE + '0' * (REGSIZE - idend.length) + str(idend.bin))
Quotient = BitArray('0b' + '0' * (REGSIZE + 1))
Divisor = BitArray('0b' + '0' * (REGSIZE - isor.length) +  str(isor.bin))
print('place Dividend in Remainder and add bit to Quotient:\n', Rem.bin, '-',Quotient.bin,'-', Divisor.bin, sep="")
while counter < REGSIZE:
    #=Step-1=
    #Shift the Remainder register left 1 bit
    Rem.int <<= 1
    print('shift remainder register left 1 bit, setting the new least significant bit to 0:\n', Rem.bin, '-',Quotient.bin,'-', Divisor.bin, sep="")
    #=Step-2=
    #Subtract the Divisor register from the left half of the Remainder register, & place in the left half of the Remainder register
    overflow = BitArray(int=Rem[:REGSIZE].int - Divisor.int, length = REGSIZE + 1)
    del overflow[0:1]
    Rem.overwrite(overflow, 0)
    print('Subtract the Divisor register from the left half of the Remainder register:\n', Rem.bin, '-',Quotient.bin,'-', Divisor.bin, sep="")
    #Condition: test reminder
    if Rem.int < 0:
        print('Remainder is < 0:')
        #Restore original value
        overflow = BitArray(int=Rem[:REGSIZE].int + Divisor.int, length = REGSIZE + 1)
        del overflow[0:1]
        Rem.overwrite(overflow, 0)
        print('Restore original value. Restore original value by adding Divisor register to the left half of Remainder register:\n',  Rem.bin, '-',Quotient.bin,'-', Divisor.bin, sep="" )
        #shift the Quotient register to the left, setting the new least significant bit to 0
        Quotient <<= 1
        print('shift the Quotient register to the left, setting the new least significant bit to 0:\n',  Rem.bin, '-',Quotient.bin,'-', Divisor.bin, sep="")
    else:
        print('Remainder is >= 0:')
        Quotient <<= 1
        Quotient.overwrite('0b1', -1)
        print('Shift the Quotient register to the left setting the new rightmost bit to 1:\n',Rem.bin, '-',Quotient.bin,'-', Divisor.bin, sep="")
    counter+=1
print('Result of division w/o checking sign:\n',Rem.bin, Quotient.bin, Divisor.bin, sep="")
if MINUS:
    print('Result should be minus:')
    Quotient.invert()
    Quotient.int += 1
    Rem = BitArray(Rem[:REGSIZE])
    Rem.invert()
    Rem.int += 1
print('Result with checking sign:\nQuotient:', Quotient.int, '+ Remainder:', Rem[:REGSIZE].int)


