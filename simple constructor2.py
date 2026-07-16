class SimpleConstructor:
	def __init__(self, name="Default"):  # constructor
		self.name = name

	def show_name(self):
		print("Name:", self.name)

	def __del__(self):
		print("I am deleting class")

	def run(self):
		self.show_name()


if __name__ == "__main__":
	obj = SimpleConstructor()
	obj.run()