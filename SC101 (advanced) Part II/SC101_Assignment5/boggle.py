"""
File: boggle.py
Name: Andrew Chao
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = {}


def main():

    start = time.time()
    ####################
    lst = []
    read_dictionary()

    # Ask the user to in put 4 letters (each has a space in between) for 4 times
    for i in range(4):
        letters = input(f'{i + 1} row of letters: ')
        if not check_format(letters):
            print('Illegal input')
            break
        # Make a list with all the single letters
        for j in range(4):
            lst.append(letters.lower()[j * 2])

    # Create a dictionary for the 1st choice in the boggle game
    original_dict = {}
    for i in range(len(lst)):
        original_dict[i] = lst[i]

    # Create a dictionary for the rest of choices in the boggle game
    boggle_dict = {
        0: {1: lst[1], 4: lst[4], 5: lst[5]},
        1: {0: lst[0], 2: lst[2], 4: lst[4], 5: lst[5], 6: lst[6]},
        2: {1: lst[1], 3: lst[3], 5: lst[5], 6: lst[6], 7: lst[7]},
        3: {2: lst[2], 6: lst[6], 7: lst[7]},

        4: {0: lst[0], 1: lst[1], 5: lst[5], 8: lst[8], 9: lst[9]},
        5: {0: lst[0], 1: lst[1], 2: lst[2], 4: lst[4], 6: lst[6], 8: lst[8], 9: lst[9], 10: lst[10]},
        6: {1: lst[1], 2: lst[2], 3: lst[3], 5: lst[5], 7: lst[7], 9: lst[9], 10: lst[10], 11: lst[11]},
        7: {2: lst[2], 3: lst[3], 6: lst[6], 10: lst[10], 11: lst[11]},

        8: {4: lst[4], 5: lst[5], 9: lst[9], 12: lst[12], 13: lst[13]},
        9: {4: lst[4], 5: lst[5], 6: lst[6], 8: lst[8], 10: lst[10], 12: lst[12], 13: lst[13], 14: lst[14]},
        10: {5: lst[5], 6: lst[6], 7: lst[7], 9: lst[9], 11: lst[11], 13: lst[13], 14: lst[14], 15: lst[15]},
        11: {6: lst[6], 7: lst[7], 10: lst[10], 14: lst[14], 15: lst[15]},

        12: {8: lst[8], 9: lst[9], 13: lst[13]},
        13: {8: lst[8], 9: lst[9], 10: lst[10], 12: lst[12], 14: lst[14]},
        14: {9: lst[9], 10: lst[10], 11: lst[11], 13: lst[13], 15: lst[15]},
        15: {10: lst[10], 11: lst[11], 14: lst[14]}
    }

    boggle_game(original_dict, boggle_dict)

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle_game(original_dict, boggle_dict):
    """
    :param original_dict: dict, a dictionary for the 1st choice in the boggle game
    :param boggle_dict: dict, a dictionary for the rest of choices in the boggle game
    :return: list, a list with all the words that makes sense
    """
    result = boggle_helper(original_dict, boggle_dict, {}, '', [], boggle_dict)
    num_result = len(result)
    print(f'There are {num_result} words in total.')


def boggle_helper(original_dict, boggle_dict, current_d, word, word_lst, boggle_dict_fixed):
    """
    :param original_dict: dict, a dictionary for the 1st choice in the boggle game
    :param boggle_dict: dict, a dictionary for the rest of choices in the boggle game
    :param current_d: dict, an empty dictionary that is used to store elements while running the recursion
    :param word: str, an empty string that is used to create a word
    :param word_lst: list, an empty list that is used to store all the words that makes sense
    :param boggle_dict_fixed: dict, a dictionary that never change while running recursion with elements from boggle_dict
    :return: list, a list with all the words that makes sense
    """
    # Base case: when the recursion collects at least 4 characters, it will examine whether the combination is a real word
    if len(current_d) > 3 and word not in word_lst:
        for key, value in current_d.items():
            word += value
        if search(word) and word not in word_lst:
            word_lst.append(word)
            print(f'Found: {word}')
            # Even when a word has been identified as the real word, it will check if it has other opportunities to become a longer word
            if has_prefix(word):
                boggle_helper(original_dict, boggle_dict, current_d, word, word_lst, boggle_dict_fixed)
        return word_lst

    # First Choice: Choose any character in the original_dict
    elif len(current_d) == 0:
        for key, value in original_dict.items():
            if key not in current_d:
                current_d[key] = value

                boggle_helper(original_dict, boggle_dict_fixed[key], current_d, word, word_lst, boggle_dict_fixed)

                current_d.pop(key)
        return word_lst
    # Other Choices: Choose any character in the given boggle_dict
    else:
        for key, value in boggle_dict.items():
            if key not in current_d:
                current_d[key] = value

                # Creating an empty word to pass the base case even if the recursion has already found a real word
                word = ''
                boggle_helper(original_dict, boggle_dict_fixed[key], current_d, word, word_lst, boggle_dict_fixed)

                current_d.pop(key)
        return word_lst


def check_format(word):
    """
    :param word: str, allow the user to enter a string
    :return: bool, return True or False depending on the format
    """
    if len(word) > 7:
        return False
    else:
        for i in range(len(word)):
            if i % 2 == 0:
                if not word[i].isalpha():
                    return False
            else:
                if word[i] != ' ':
                    return False
        return True


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python dictionary
    """
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            if len(line.strip()) >= 4:
                dictionary[line.strip()] = line.strip()[0]


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    global dictionary
    count = 0
    for key, value in dictionary.items():
        if key.startswith(sub_s):
            count += 1
            break
    if count >= 1:
        return True
    else:
        return False


def search(word):
    """
    :param word: str, allow the user to enter a word
    :return: bool, return True or False depending on whether this word is in the dictionary
    """
    global dictionary
    count = 0
    for key, value in dictionary.items():
        if key == word:
            count += 1
            break
    if count >= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
