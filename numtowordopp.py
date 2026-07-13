class numberto_word:
    """This class converts numbers to words.
    input: a number between 0 and 10
    output: the corresponding word for the number  
    created on : 2026-07-13 12:13
    Author : Siddesh Hallale
    """
   
    numbers = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    ls = []

    def input_number(self):
        self.ls = input("Enter a number between 0 and 10: ")
    
    def convert_number(self):
        for x in self.ls:
            print(self.numbers[int(x)], end=" ")

if __name__ == "__main__":
    obj = numberto_word()
    obj.input_number()
    obj.convert_number()
