def count_words(input_string):
    words_list = input_string.split()
    word_count = len(words_list)
    return word_count

input_string = input("Enter a sentence or words: ")
word_count = count_words(input_string)
print("Number of words:", word_count)
