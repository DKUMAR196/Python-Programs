"""
   @ Author - Deepak Kumar
   @ Date - 05-NOV-2021
   @ Time - 10:16
   @ Title - Print 2D Array.
"""
from array import *
from typing import Type


class TwoDimentionalArray:
    def TwoDimentionalCalculation(self):
        i=0
        matrix = []
        arr = []
        flag = True
        while flag == True:
            try:
                row = int(input("Please Enter Number of Rows:"))
                colum = int(input("Please Enter Number of Coloums:"))
                if (row and colum) ==0:
                    flag = False
                    raise ValueError()
                else:
                    for i in range(row):
                        for j in range(colum):
                            print("Enter value for",j,"Coloum &",i,"Row:")
                            inputNumber = int(input())
                            arr.append(inputNumber)
                        matrix.append(arr)
                flag = False
            except ValueError:
                print('Invalid Number..!!')
        print(arr)
        inputCheck = matrix
        for x in inputCheck:
            for y in x:
                print(y, end=" ")
            print()
twoDimentionalArray = TwoDimentionalArray()
twoDimentionalArray.TwoDimentionalCalculation()