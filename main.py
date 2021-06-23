from inputGet import *
from adder import *
from conversion import *
def mainFunction():
    flag = False
    while(not flag):
        NumList = get_input()
        print()
        print("First input values")
        print("The decimal number is:", binaryToDecimal(NumList[0]))
        print("The binary number is :", NumList[0])
        print()
        print("Second input values")
        print("The decimal number is:", binaryToDecimal(NumList[1]))
        print("The binary number is :", NumList[1])

        


        sum = byteAdder(NumList)
        print()
        print("The final result is:")
        print("Binary Number                     Decimal Number")
        print(" " , NumList[0] ,"                ", binaryToDecimal(NumList[0]))
        print("+" , NumList[1] ,"                ", binaryToDecimal(NumList[1]))
        print("___________________            ____________________")
        
        print(sum ,"                          ", binaryToDecimal (NumList[0]) + binaryToDecimal(NumList[1]))
        
        
        CorrectInput = False
        print()
        print("____________________________________________________________________________________________________")
        print()
        while not CorrectInput:
            DoContinue = input("choose 1 if you want to continue or choose 2 if you want to exit")
            if DoContinue == "1":
                CorrectInput = True
            elif DoContinue == "2":
                CorrectInput = True
                flag = True
            else:
                print("Give correct input")
                CorrectInput = False
mainFunction()

