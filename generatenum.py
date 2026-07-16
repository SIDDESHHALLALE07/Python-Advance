class sequencegenerator:

    def num_generator(self, start, end):
        for i in range(start, end + 1):
            print(i, end=' ')

    
    def input_start(self):
        Start = int(input("Enter the starting number: "))
        End = int(input("Enter the ending number: "))
        self.num_generator(start = Start, end = End)


if __name__ == "__main__":
    obj = sequencegenerator()
    obj.num_generator(321, 499)