# WORD-COUNT-TOOL
In this project, we'll create a program that counts the number of words in a given text file. The program will read in a file, count the number of words, and display the result to the user.


def word_count(filename):

    with open(filename, "r") as file:
    
    
    text = file.read()
    
    words = text.split()
    
    num_words = len(words)
    
    print(f"The file '{filename}' contains {num_words} words.")


filename = input("Enter the name of the file: ")

word_count(filename)



# Description:

We define a function called word_count that takes in a filename as an argument.

We open the file using the with statement, which ensures that the file is properly closed when we're done with it.

We read the contents of the file using the read method and store it in the variable text.

We split the text into words using the split method and store it in the variable words.

We count the number of words using the len function and store it in the variable num_words.

We display the result to the user using the print function.

Finally, we prompt the user to enter the name of the file and call the word_count function with the filename as an argument.


Example Output:

Suppose we have a file called example.txt with the following contents:


This is an example file. It contains some text that we can count the words in.

When we run the program and enter example.txt as the filename, we should see the following output:


The file 'example.txt' contains 14 words.

This tells us that the file contains 14 words.
