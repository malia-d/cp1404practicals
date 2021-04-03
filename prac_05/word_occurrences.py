word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
word_list = list(word_to_count.keys())
word_list.sort()
longest_word = max(len(word) for word in word_list)
for word in word_list:
    print("{:{}} : {}".format(word, longest_word, word_to_count[word]))
