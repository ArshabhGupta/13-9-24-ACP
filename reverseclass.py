class StringReverser:
    def __init__(self, original_string):
        self.original_string = original_string

    def reverse_string(self):
        reversed_string = self.original_string[::-1]
        return reversed_string


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    reverser = StringReverser(input_string)
    reversed_result = reverser.reverse_string()
    print(f"Original String: {input_string}")
    print(f"Reversed String: {reversed_result}")