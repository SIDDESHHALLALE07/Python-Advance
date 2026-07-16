class SimpleConstructor:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print('Name:', self.name)

if __name__ == "__main__":
    obj = SimpleConstructor('Siddesh')
    obj.display_name()