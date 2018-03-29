from bitstring import BitArray

try:
    with open('/Users/andriimokii/Documents/CS/Lab1/text/test/base64_info.txt', 'rb') as f, open('/Users/andriimokii/Documents/CS/Lab1/text/test/OUT.txt', 'wt', encoding='UTF-8') as out:
        pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        buff_b1 = [ ] 
        counter = -1
        num = 0
        for i in BitArray(f.read()).cut(8):
            counter+=1
            if counter == 0:
                out.write(pattern[i[ : 6].int])
            elif counter == 1:
                out.write(pattern[int(buff_b1[0][6:] + str(i[:4].bin), 2)])
            else:
                out.write(pattern[int(buff_b1[1][4:] + str(i[:2].bin), 2)])                    
                out.write(pattern[i[2:].int])
            buff_b1.append(str(i.bin))
            if counter == 2:
                del buff_b1[:]
                counter = -1
        if counter == 0:
            out.write(pattern[int(buff_b1[0][6:] + '0000', 2)] + '==')
        elif counter == 1:
            out.write(pattern[int(buff_b1[1][4:] + '00', 2)] + '=')
except Exception as ex:
    print("Error:", ex)


