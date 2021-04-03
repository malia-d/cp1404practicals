word_to_count = {}
text = input("Text: ")
words = text.split()
# If the word is in the dictionary then '1' is added to its count, and if not, it's added as a key with a count of '1'.
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
word_list = list(word_to_count.keys())  # Creating a list of the dictionary
word_list.sort()  # Sorting the list into alphabetical order
longest_word = max(len(word) for word in word_list)
for word in word_list:
    # Using string formatting and the number of characters in the longest word to align the values.
    print("{:{}} : {}".format(word, longest_word, word_to_count[word]))
