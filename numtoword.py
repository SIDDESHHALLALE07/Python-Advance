numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
ls = input("Enter a number between 0 and 10: ")
for x in ls:
    print(numbers[int(x)], end=" ")
