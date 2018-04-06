#!/usr/local/bin/python3
from bitstring import BitArray

#Addend1, addend2 and summary
Addend1 = BitArray(float=0, length=32)
Addend2 = BitArray(float=-5, length=32)
Sum = BitArray(float=0, length=32)


# check if Addend1 < Addend2 , if yes - change
if abs(Addend1.float) < abs(Addend2.float):
    Addend1 , Addend2 = Addend2 , Addend1    
Addend1_one_m = BitArray('0b1' + str(Addend1[9:].bin))
Addend2_one_m = BitArray('0b1' + str(Addend2[9:].bin))
mantissa_sum = 0

#initial exponent
Sum.overwrite(Addend1[1:9], 1)

#exponent's difference
exp_diff = Addend1[1:9].uint - Addend2[1:9].uint
if exp_diff != 0:
    #align mantissa
    Addend2_one_m  = BitArray('0b1' + str(Addend2[9:].bin))
    Addend2_one_m  >>= exp_diff

#check if needs addition or subtraction
if Addend1[0:1].bin == Addend2[0:1].bin:
    print('ravnu')
    #sum will be positive
    Sum.overwrite('0b0',0)
    mantissa_sum = BitArray(int=Addend1_one_m.int + Addend2_one_m.int, length = Addend1_one_m.len + 1 ) 
    del mantissa_sum[0:1]
elif Addend1.int < 0:
    #sum could be positive or negative
    #Addend2_one_m.invert()
    #Addend2_one_m.int += 1
    print('Addend1 menwe')
    mantissa_sum = BitArray(int=Addend2_one_m.int - Addend1_one_m.int, length = Addend1_one_m.len + 1 )
    del mantissa_sum[0:1]
elif Addend2.int < 0:
    print('Addend2 menwe')
    mantissa_sum = BitArray(int=Addend1_one_m.int - Addend2_one_m.int, length = Addend1_one_m.len + 1 )
    del mantissa_sum[0:1]
if Addend1.float + Addend1.float < 0:
    #normalization needed
    Sum.overwrite('0b1',0)
test = Sum[1:9].uint 
while mantissa_sum[0:1].bin != "1":
    mantissa_sum <<= 1
    test -= 1
    #test = bin(Sum[1:9].int - 1)
    #Sum.overwrite(test, 1)
Sum.overwrite(bin(test), 1)
print(mantissa_sum.bin)
Sum.overwrite(mantissa_sum[1:], 9)
print(Sum.bin)
print(Sum.float)
print(Addend1.float + Addend2.float)       



#print(abs(Addend1.float), Addend1.bin, Sum.bin)

