"""
Ask the user to input a string of text and iterate through it. Add each word to the dictionary, as a key, and the number
of occurrences of each word, as a value. Print the each word and it's number of occurrences. Determine the length of the
longest word in the dictionary and use it to print the words and align the counts in one column using string formatting.

Word Occurrences. Created by Malia, April 2021.
"""

word_to_count = {}
text = input("Text: ")
words = text.split()

for word in words:
    # Add '1' to word value.
    if word in word_to_count:
        word_to_count[word] += 1
    # Add word as a key with a value of '1'.
    else:
        word_to_count[word] = 1
word_list = list(word_to_count.keys())  # create a list from the dictionary
word_list.sort()  # sort the list into alphabetical order
longest_word = max(len(word) for word in word_list)  # determine the number of characters in the longest word
for word in word_list:
    # Use string formatting and the number of characters in the longest word to align the values.
    print("{:{}} : {}".format(word, longest_word, word_to_count[word]))
