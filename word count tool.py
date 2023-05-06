def word_count(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        num_words = len(words)
        print(f"The file '{filename}' contains {num_words} words.")

filename = input("Enter the name of the file: ")
word_count(filename)
