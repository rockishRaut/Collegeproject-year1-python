def decimalToBinary(decimalNum):
    c = ""
    i = 7
    while (decimalNum>0):
        t = decimalNum%2
        c = str(t) + c       
        decimalNum = int(decimalNum/2)
    eightBit = binaryToEightBit(c)    
    return eightBit

def binaryToDecimal(binaryNum):
    total = 0
    i = 0
    for v in range(len(binaryNum)-1,-1,-1):
       total += int(binaryNum[v])*2**i
       i = i+1
        
    return total

def binaryToEightBit(binaryNum):
    eightBit = binaryNum
    if(len(binaryNum) !=8):
        for i in range(len(binaryNum),8):
            eightBit = "0" + eightBit
        return eightBit
    else:
        return eightBit
