# Challenge 1 Sorting
def sorting():
    words = input("enter words separated with comma\n")
    words_list = words.split(',')
    words_list.sort()
    print(words_list)
sorting()


# Challenge 2 Longest Word
def longest_word_in_string():

    sentence = input("Enter your sentence \n")
    words = sentence.split()
    print(words)
    longest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    print("The longest word is:" ,  longest_word)

longest_word_in_string()
