"""
File: hangman.py
Name: Andrew
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The hangman game includes 3 parts:
    1. Initial setting section: We will get a final answer and its counterpart, the dash-disguised answer.
    2. Welcome section: Tell the user the rule, including how many letters the word is and how many times
    they can guess wrongly.
    3. Hangman Game section: Allow users to guess the component of the final answer. If users consumed
    over the times given by the initial setting, they will be hung.
    """

    # Initial setting
    answer = random_word()
    dash_answer = dash_transfer(answer)  # Remove the visibility of the answer

    # Welcome section
    print('The word looks like: ' + dash_answer)
    print('You have ' + str(N_TURNS) + ' guesses left.')

    # The hangman Game begins from here
    first_guess = input('Your guess: ')
    game_hangman(first_guess, answer, N_TURNS)


def game_hangman(initial_guess, final_answer, lives):
    """
    :param initial_guess: str, allow users to enter an initial guessing letter to
    trigger the hangman game.
    :param final_answer: str, allow users to input the final answer so that this
    function can help to match the guessing result.
    :param lives: str, allow users to restrict how many guesses for this game.
    :return: Nothing is necessary to return in this function.
    """
    # First guessing
    successful_guess = verification(initial_guess)
    ver_result = match(successful_guess, final_answer)
    print('The word looks like: ' + ver_result)

    # Only when the first guessing is wrong, the total_lives will be deducted by one
    if ver_result.find(successful_guess) == -1:
        lives -= 1
    print('You have ' + str(lives) + ' guesses left.')

    # Save the hint that already shown to users
    latest_guess_result = ver_result

    # 2nd - 7th guessing
    a = len(final_answer)
    while True:

        # When total lives have been consumed, the game is over
        if lives == 0:
            print('You are completely hung : (')
            print('The word was: ' + final_answer)
            break

        # When the latest guessing result contains no dash, it means the user win the game
        elif latest_guess_result.find('-') == -1:
            print('You win!!')
            print('The word was: ' + final_answer)
            break

        # The guessing game will continue if total lives haven't been cost down to zero
        else:
            guess = input('Your guess: ')
            successful_guess = verification(guess)
            ver_result = match(successful_guess, final_answer)

            # The variable, update_result, is used to combine the previous guessing result and the next one
            updated_result = ''

            # This for loop is used to combine 2 different guessing result
            for i in range(a):
                if ver_result[i].isalpha():
                    updated_result += ver_result[i]
                else:
                    if latest_guess_result[i].isalpha():
                        updated_result += latest_guess_result[i]
                    else:
                        updated_result += '-'

            # Save the hint that already shown to users
            latest_guess_result = updated_result

            # Only when the first guessing is wrong, the total_lives will be deducted by one
            if ver_result.find(successful_guess) == -1:
                lives -= 1

            # When lives >= 1 let users know the hint of the answer and how many lives left
            if lives >= 1 and latest_guess_result.find('-') != -1:
                print('The word looks like: ' + updated_result)
                print('You have ' + str(lives) + ' guesses left.')


def match(input_character, final_answer):
    """
    :param input_character: str, allow users to input a string that will be verified whether
    there are any matches with the final answer.
    :param final_answer: str, the final answer.
    :return: str, return the matching result that could consist of '-' and letters.
    """
    result = ""
    for f in final_answer:
        if f == input_character:
            result += input_character
        else:
            result += '-'
    if final_answer.find(input_character) != -1:
        print('You are correct!')
    else:
        print('There is no ' + input_character + '\'s in the word.')

    return result


def verification(character):
    """
    :param character: str, allow users to input a string that will be confirmed whether
    it qualifies for a successful guessing.
    :return: str, when a successful guessing has been made, this function will return
    a qualified guessing character in upper case.
    """
    character = character.upper()  # Prevent lower case
    while True:
        # Prevent users from entering a number or a symbol

        if len(character) > 1:
            print('illegal format.')
            character = input('Your guess: ').upper()  # Prevent lower case
        else:
            if not character.isalpha():
                print('illegal format.')
                character = input('Your guess: ').upper()  # Prevent lower case
            else:
                break

    return character


def dash_transfer(word):
    """
    :param word: str, allow users to enter a word that is going to be disguised.
    :return: str, return a all-dash sequence with the same length.
    """
    r = len(word)
    dash_word = ''
    for i in range(r):
        dash_word += '-'

    return dash_word


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
