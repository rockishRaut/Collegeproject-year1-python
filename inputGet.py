from conversion import *
def get_input():
    flag = False
    while(not flag):
        inputData = []
        choice =input("Please!, Enter 'd' for decimal and 'b' for binary : ")
        if choice=='b':
            correctInput = False
            while(not correctInput):            
                firstNCorrect =False
                while(not firstNCorrect):
                    firstNum=input("Please!, Enter First Binary Number : ")
                    if validation(firstNum):
                        print("thank you!! for the correct first number:")
                        firstNCorrect=True
                    else:
                        print("Error!! please enter the correct numbers")
                secondNCorrect =False
                while(not secondNCorrect):
                    secondNum= input("Please!, enter the second number : ")
                    if validation(secondNum):
                        print("thank you!! for the correct second number")
                        secondNCorrect=True
                    else:
                        print("!! please enter the correct numbers : ")
                if(binaryToDecimal(firstNum)+binaryToDecimal(secondNum)>255):
                    print("Please give number sum less than 255")
                else:
                    correctInput = True
            inputData.append(binaryToEightBit(firstNum))
            inputData.append(binaryToEightBit(secondNum))
            flag = True
            return inputData


        elif choice == 'd':
            
            correctInput = False
            while(not correctInput):            
                
                firstNCorrect= False
                while(not firstNCorrect):
                    firstNum= input("Please!, Enter first Decimal Number:")
                    if validationToDecimal(firstNum):
                        print("Thank you!! for the correct decimal Number")
                        firstNCorrect=True
                    else:
                        print("Error!! please enter the correct decimal numbers")

                secondNCorrect =False
                while(not secondNCorrect):          
                    secondNum= input("Please!, Enter the second decimal number")
                    if validationToDecimal(secondNum):
                        print("thank you!! for the correct decimal number")
                        secondNCorrect=True
                    else:
                        print("Error!! please enter the correct decimal numbers")
                if(int(firstNum)+int(secondNum)>255):
                    print("Please insert the number which sums less than 255")
   
                else:
                    correctInput = True
            
            inputData.append(decimalToBinary(int(firstNum))) 
            inputData.append(decimalToBinary(int(secondNum)))
            flag = True
            return inputData


        

def validation(num):
    if num == "":
        print("empty field found, please enter binary number")
        return False
    try:
        checkNum = int(num)
    except:
        print("No special character or alphabets allowed! please enter the correct binary number")
        return False
    for digit in num:
        if digit not in['0', '1']:
            print("error! Digits must be either 1 or 0")
            return False
    if binaryToDecimal(num)<0:
        print("negative number found, Negetive values are not allowed.")
        return False
    
    return True
def validationToDecimal(num):
    if num == "":
        print("empty field found, please enter decimal number")
        return False
    try:
        checkNum = int(num)
    except:
        print("No special character or alphabets allowed! please enter the correct decimal number")
        return False
    if int(num)<0:
        print("negative number found, Negetive values are not allowed.")
        return False
    for digit in num:
        if digit not in['0','1','2','3','4','5','6','7','8','9']:
            print("error! Digits must be 0 to 9")
            return False
    if(int(num) <0 or int(num) >255):
        print("The number must be between 0-255")
        return False
        
    return True
    

            
