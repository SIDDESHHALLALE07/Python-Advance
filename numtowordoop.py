class numberto_word:
    numbers = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    ls = []
    def input_number (self):
        self.ls = input("Enter a number between 0 and 10: ")
    def convert_number(self):
        for x in self.ls:
            print(self.numbers[int(x)], end=" ")
        
if __name__ == "__main__":
        obj = numberto_word()
        obj.input_number()      
        obj.convert_number()
    