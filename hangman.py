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

correct_letters_guessed = []

player_word_board = ''

for char in range(0, chars_in_random_word):
    if char == chars_in_random_word - 1:
        player_word_board += '_'
    else:
        player_word_board += '_ '

empty_space_check = player_word_board.find('_')

empty_space_count = player_word_board.count('_')

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
        print('\nWELCOME TO A NEW GAME OF HANGMAN!\n\nYour random word has been chosen and the game board is below.\n\n' + player_word_board + '\n\nIt looks like your word has ' + str(chars_in_random_word) + ' letters.\n\nGood luck!\n\n')
        print('Alright let\'s get started.\n\nYou have seven chances to spell out this mystery word.\n\n')

        user_letter_choice = input('Please enter your first letter: ')

        user_letter_choice_check = random_word.find(user_letter_choice)

        if user_letter_choice_check == -1:
            player_lives -= 1

            print('\nSorry. Keep guessing.\n\nYou have ' + str(player_lives) + ' lives left')
            print(hangman_six_lives)
        else:
            player_word_board_list = player_word_board.split()

            correct_letters_guessed.append(user_letter_choice)

            for char_count in range(0, chars_in_random_word):
                if char_count == user_letter_choice_check:
                    player_word_board_list[char_count] = user_letter_choice
                    player_word_board = ' '.join(player_word_board_list)

            empty_space_count = player_word_board.count('_')

            print('\n' + player_word_board)
    else:
        user_letter_choice = input('\nPlease enter another letter: ')

        user_letter_choice_check = random_word.find(user_letter_choice)

        if user_letter_choice_check == -1:
            player_lives -= 1

            if player_lives == 5:
                print('\nSorry. Keep guessing.\n\nYou have ' + str(player_lives) + ' lives left')
                print(hangman_five_lives)
            elif player_lives == 4:
                print('\nSorry. Keep guessing.\n\nYou have ' + str(player_lives) + ' lives left')
                print(hangman_four_lives)
            elif player_lives == 3:
                print('\nSorry. Keep guessing.\n\nYou have ' + str(player_lives) + ' lives left')
                print(hangman_three_lives)
            elif player_lives == 2:
                print('\nSorry. Keep guessing.\n\nYou have ' + str(player_lives) + ' lives left')
                print(hangman_two_lives)
            elif player_lives == 1:
                print('You only have one more life. Choose wisely!')
                print(hangman_one_life)
            elif player_lives == 0:
                print('Gameover.')

                print(hangman_zero_lives)

                replay = input('Do you want to play again? Enter YES or NO: ')

                if replay == 'YES':
                    player_lives = 7
                    correct_letters_guessed = []
                    player_word_board = ''

                    for char in range(0, chars_in_random_word):
                        if char == chars_in_random_word - 1:
                            player_word_board += '_'
                        else:
                            player_word_board += '_ '

                    random_word = random.choice(words_list)

                    empty_space_check = player_word_board.find('_')

                    empty_space_count = player_word_board.count('_')
        else:
            player_word_board_list = player_word_board.split()

            if user_letter_choice in correct_letters_guessed:
                print('\nSorry. You already guessed that and got it right! Pick another letter')
            else:
                correct_letters_guessed.append(user_letter_choice)

                for char_count in range(0, chars_in_random_word):
                    if char_count == user_letter_choice_check:
                        player_word_board_list[char_count] = user_letter_choice
                        player_word_board = ' '.join(player_word_board_list)

                        empty_space_count = player_word_board.count('_')

                        print('\n' + player_word_board)
