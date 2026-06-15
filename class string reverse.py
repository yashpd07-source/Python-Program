class StringReverser:
    def __init__(self, text: str):
        self.__text = text
    def reverse_words(self) -> str:
        words = self.__text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)
    def __str__(self) -> str:
        return self.reverse_words()
    def __repr__(self) -> str:
        return f"StringReverser(text={repr(self.__text)})"
if __name__ == "__main__":
    original_string = "Python class to reverse a string word by word"
    reverser = StringReverser(original_string)
    result_method = reverser.reverse_words()
    print("Method output:  ", result_method)
    print("Special __str__:", reverser)