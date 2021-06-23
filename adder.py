from gates import *

def byteAdder (binaryNumberList):
    BinaryNumber1 = binaryNumberList[0]
    BinaryNumber2 = binaryNumberList[1]

    BinarySum = ""

    Carry_On = 0
    print("Adding in binary number system")

    for i in BinaryNumber1:
        print(i,end="")
    print()
    print("+")
    
    for i in BinaryNumber2:
        print(i,end="")
    print()

    for i in range(len(BinaryNumber1)-1,-1,-1):
        FirstBit = int(BinaryNumber1[i])
        SecondBit = int(BinaryNumber2[i])
        xor_Value = xorGate(FirstBit, SecondBit)
        Sum_Value = xorGate(xor_Value, Carry_On)
        Carry_Out = orGate(andGate(FirstBit,SecondBit),andGate(xor_Value, Sum_Value))
        Carry_On = Carry_Out
        BinarySum = str(Sum_Value)+BinarySum
    return BinarySum


    
