import os
from math import log
try:
    alph = { }
    summ = 0
    FilePath = '/Users/andriimokii/Documents/CS/Lab1/text/test/OUT.txt'
    stream = open(FilePath, 'rt', encoding='UTF-8')
    Text = stream.read()
    for ch in Text:
        #if ch.isalpha():
            if ch in alph.keys():
                alph[ch]+=1
            else:
                alph[ch]=1
    #text_cnt = open('/Users/andriimokii/Documents/text/CS-TextCounter.txt', 'wt', encoding='UTF-8')
    for key in sorted(alph.keys()):
        summ+=alph[key]
        print(key, '->', alph[key])
    for el in sorted(alph.keys()):
        print('Probability:', el, '->', alph[el] / summ)
    m = 1
    H = 0
    for key in sorted(alph.keys()):
        H += (alph[key] / summ) * log(1/(alph[key] / summ),2)
    print('Entropii:', H)
    print('Amount of info:', (summ * H) / 8 )
    print('Real size:', os.stat(FilePath).st_size)
    print('amount of letters',summ)       
    stream.close()
except Exception as ex:
    print("error is:", os.strerror(ex.errno))
    
