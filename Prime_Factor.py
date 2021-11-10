"""
   * Author - Deepak Kumar
   * Date -  04-NOV-2021
   * Time -  17:45
   * Title - Factors of Numbers
"""

class Factors:
    def Calculation(self):
        try:
            inputNumber = int(input("Enter Number to calculate Factor::"))
            if inputNumber<=0:
                raise ValueError
            else:
                i = 2
                print("Factors of",inputNumber,"are::")
                while(inputNumber != 2):
                    reminder = inputNumber % i
                    if(reminder==0):
                        inputNumber = inputNumber/i
                        print(i)
                    else:
                        i = i+1
        except ValueError:
            print("Number",inputNumber,"is Not valid")

factors = Factors()
factors.Calculation()