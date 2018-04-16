import random

# open and read word_list.txt, store words in a list, and select a random word from the list

words_file = open('word_list.txt', 'r')

words = words_file.read()

words_list = words.split(',')

random_word = random.choice(words_list)

print(random_word)

chars_in_random_word = len(random_word)

# create player board

player_lives = 7

player_word_board = ''

for char in range(0, chars_in_random_word):
    if char == chars_in_random_word - 1:
        player_word_board += '_'
    else:
        player_word_board += '_ '

empty_space_check = player_word_board.find('_')

empty_space_count = player_word_board.count('_')

# intro

print('WELCOME TO A NEW GAME OF HANGMAN!\n\nYour random word has been chosen and the game board is below.\n\n' + player_word_board + '\n\nIt looks like your word has ' + str(chars_in_random_word) + ' letters.\n\nGood luck!')

# create hangman

hangman_six_lives = ' -----------\n|           |\n|\n|\n|\n|\n|\n|\n|\n---------------'
hangman_five_lives = ' -----------\n|           |\n|           O\n|\n|\n|\n|\n|\n|\n---------------'
hangman_four_lives = ' -----------\n|           |\n|           O\n|           |\n|           |\n|\n|\n|\n|\n---------------'
hangman_three_lives = ' -----------\n|           |\n|           O\n|           |\ \n|           | \ \n|\n|\n|\n|\n---------------'
hangman_two_lives = ' -----------\n|           |\n|           O\n|          /|\ \n|         / | \ \n|\n|\n|\n|\n---------------'
hangman_one_life = ' -----------\n|           |\n|           O\n|          /|\ \n|         / | \ \n|            \ \n|             \ \n|\n|\n---------------'
hangman_zero_lives = ' -----------\n|           |\n|           O\n|          /|\ \n|         / | \ \n|          / \ \n|         /   \ \n|\n|\n---------------'

# main game loop

while player_lives > 0 and empty_space_check != -1:
    if player_lives == 7 and empty_space_count == chars_in_random_word:
        print('Alright let\'s get started.\n\nYou have seven chances to spell out this mystery word.\n\n')

        user_letter_choice = input('Please enter your first letter: ')

        user_letter_choice_check = random_word.find(user_letter_choice)

        print(user_letter_choice_check)

        if user_letter_choice_check == -1:
            player_lives -= 1

            print(hangman_six_lives)
        else:
            player_word_board_list = player_word_board.split()

            print(player_word_board_list)

            for char_count in range(0, chars_in_random_word):
                if char_count == user_letter_choice_check:
                    print(char_count)
                    player_word_board_list[char_count] = user_letter_choice
                    player_word_board = ' '.join(player_word_board_list)
            print(player_word_board)
    else:
        user_letter_choice = input('\nPlease enter another letter: ')

        user_letter_choice_check = random_word.find(user_letter_choice)

        print(user_letter_choice_check)

        if user_letter_choice_check == -1:
            player_lives -= 1

            print(hangman_six_lives)
        else:
            player_word_board_list = player_word_board.split()

            print(player_word_board_list)

            for char_count in range(0, chars_in_random_word):
                if char_count == user_letter_choice_check:
                    print(char_count)
                    player_word_board_list[char_count] = user_letter_choice
                    player_word_board = ' '.join(player_word_board_list)
            print(player_word_board)
