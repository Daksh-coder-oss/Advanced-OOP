class IOstring:
    def __init__(self):
        self.str1=""

   
    def get_str1(self):
        self.str1=input("Enter anything that is a string")
    def print_str1(self):
        print("Your string is:",self.str1.upper())
obj=IOstring()

obj.get_str1()
obj.print_str1()




