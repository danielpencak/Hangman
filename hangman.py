import random

words_file = open('word_list.txt', 'r')

words = words_file.read()

words_list = words.split(',')

random_word = random.choice(words_list)
