#Make a class Charactercount in python which has two functions  and  
#One variable;  
#function1: take a value of type string and set that value in a variable(note if the integer is given function should stop and print that input is invalid )    
#function2: get the string value from the variable and count the characters and return the count of characters

class Charactercount:
    str_=""
    def setVariable(self, input_):
        if type(input_)==str:
            self.str_=input_
        else:
            print("invalid input")
    
    def countOfChars(self):
        return len(self.str_)
    
obj = Charactercount()
obj.setVariable("hello world!")
print("no of characters in string: ", obj.countOfChars())
