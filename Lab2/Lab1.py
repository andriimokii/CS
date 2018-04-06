#!/usr/local/bin/python3
from bitstring import BitArray
count = 0

#Multiplicand and Multiplier
M = BitArray(int=-20, length=11)
Q = BitArray(int=7, length=11)
print(Q.bin, '*', M.bin, '(', Q.int, '*', M.int, ')')
#initialization
A = BitArray('0b' + '0' * M.length + str(Q.bin) + '0')

while count < M.length:
    if str(A[2 * M.length - 1:].bin) == '00' or str(A[2*M.length - 1:].bin) == '11' :
        print('Register:', A.bin, '--> 00 or 11-NOP -->', end=' ')
        A.int >>= 1
        print('shift right -->',A.bin)
    elif str(A[2*M.length - 1:].bin) == '01' :
        print('Register:', A.bin, '--> 01-ADD -->', end=' ')
        lol = BitArray(int=A[:M.length].int + M.int, length = M.length + 1)
        del lol[0:1]
        A.overwrite(lol, 0)
        print('ADDED:', A.bin, '-->', end=' ')
        A.int >>= 1
        print('shift right -->',A.bin)
    else:
        print('Register:', A.bin, '--> 10-SUB -->', end=' ')
        heh = BitArray(int=A[:M.length].int - M.int, length = M.length + 1)
        del heh[0:1]
        A.overwrite(heh, 0)
        print('SUBTRACTED:', A.bin, '-->', end= ' ')
        A.int >>= 1
        print('shift right -->', A.bin)
    count+=1
del A[-1]
print('Binary register: ', A.bin)
print('Decimal register: ', A.int)

