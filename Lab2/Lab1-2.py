#!/usr/local/bin/python3
from bitstring import BitArray

#Addend1, addend2 and summary
Addend1 = BitArray(float=9.75, length=32)
Addend2 = BitArray(float=0.5625, length=32)
Sum = BitArray(float=0, length=32)
print(Addend1.bin, Addend2.bin, '(', Addend1.float, '+', Addend2.float, ')')

# check if Addend1 < Addend2 , if yes - change
if abs(Addend1.float) < abs(Addend2.float):
    Addend1, Addend2 = Addend2, Addend1
Addend1_one_m = BitArray('0b1' + str(Addend1[9:].bin))
Addend2_one_m = BitArray('0b1' + str(Addend2[9:].bin))
mantissa_sum = 0

#initial exponent
Sum.overwrite(Addend1[1:9], 1)

#exponent's difference
exp_diff = Addend1[1:9].uint - Addend2[1:9].uint
print('Exponent difference:', exp_diff, '(', Addend1[1:9].uint, '-', Addend2[1:9].uint, ')')
if exp_diff != 0:
    #align mantissa
    print('Not aligned mantissa:', Addend2_one_m.bin)
    Addend2_one_m  >>= exp_diff
    print('aligned mantissa:    ', Addend2_one_m.bin)
#check if needs addition or subtraction
if Addend1[0:1].bin == Addend2[0:1].bin:
    Sum.overwrite(Addend1[0:1], 0)
    mantissa_sum = BitArray(uint=Addend1_one_m.uint + Addend2_one_m.uint, length = Addend1_one_m.len + 1 ) 
    print('Add significants:', mantissa_sum.bin)
elif Addend1[0:1].bin == '1':
    mantissa_sum = BitArray(uint=Addend1_one_m.uint - Addend2_one_m.uint, length = Addend1_one_m.len + 1 )
    Sum.overwrite('0b1',0 )
    print('Add significants:', mantissa_sum.bin)
elif Addend2[0:1].bin == '1':
    mantissa_sum = BitArray(uint=Addend1_one_m.uint - Addend2_one_m.uint, length = Addend1_one_m.len + 1 )
    Sum.overwrite('0b0', 0)
    print('Add significants:', mantissa_sum.bin)
test = Sum[1:9].uint 
if mantissa_sum[0:1].bin == '1':
    del mantissa_sum[-1]
    test += 1
else:
    del mantissa_sum[0:1]
print('Normalize result:', mantissa_sum.bin)
Sum.overwrite(bin(test), 1)
Sum.overwrite(mantissa_sum[1:], 9)
print(Sum.float)
print(Addend1.float + Addend2.float)       


#print(abs(Addend1.float), Addend1.bin, Sum.bin)

