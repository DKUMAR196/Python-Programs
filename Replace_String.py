'''
   @Author - Deepak Kumar
   @Date - 04-NOV-2021
   @Time - 11:50
   @Title - User Input and Replace String
'''
class String:
    def getString(self):
        try:
                inputName = input("Enter Name (Length should be grater than 0)::")
                inputNameLen = len(inputName)
                if inputNameLen != 0:
                    print("Hello " + inputName + ",How are you?")
                else:
                    raise NameError()
        except NameError:
                print("Name is not valid..!!")
string = String()
string.getString()