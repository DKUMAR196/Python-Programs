"""
   * Author - Deepak Kumar
   * Date -  04-NOV-2021
   * Time -  17:13
   * Title - Power of 2
"""
class PowerOfTwo:
    def CalculatePower(self):
        inputNumber = int(input("Enter Number to Calculate Table::"))
        try:
            if inputNumber>31:
                raise ValueError("Invalid  Input..!!")
            elif inputNumber<0:
                raise ValueError("Invalid Input..!!")
            else:
                for i in range(1,inputNumber+1):
                    table = 2*i
                    print("2 ^",i,":",table)
        except ValueError as e:
            print(e)
powerOfTwo = PowerOfTwo()
powerOfTwo.CalculatePower()