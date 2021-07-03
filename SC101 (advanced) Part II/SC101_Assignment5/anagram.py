"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary = []               # It's a global variable that stores all words in the dictionary.txt file


def main():
    """
    This function allows user to enter a word and find its anagram.
    """
    start = time.time()
    ####################
    read_dictionary()
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')

    while True:
        word = str(input('Find anagrams for: '))
        if word == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(word)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    This function is used to read the dictionary file and consolidate all the words into a list.
    :return: No turn value
    """
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line.strip())


def find_anagrams(s):
    """
    :param s: str, allow users to enter a word
    :return: it will return all format of the anagram for input word
    """
    global dictionary
    new_dictionary = []
    # Create a filter for the dictionary
    for element in dictionary:
        if len(element) == len(s):
            new_dictionary.append(element)

    # Break down all the characters into a dictionary
    character_dict = {}
    for i in range(len(s)):
        character_dict[i] = s[i]

    word = ''
    combination_lst = helper(character_dict, {}, len(s), word, [])

    answer = []
    for combination in combination_lst:
        if combination in new_dictionary:
            print(f'Found: {combination}')
            print('Searching...')
            answer.append(combination)

    num_answer = len(answer)
    print(f'{num_answer} anagrams:', answer)


def helper(character_dict, current_dict, word_length, word, word_lst):
    """
    :param character_dict: dict, a dictionary that accommodates all the characters from a word
    :param current_dict: dict, users should input an empty dictionary
    :param word_length: int, the length of the word
    :param word: str, the word that users input
    :param word_lst: list, a list that accommodates all the combination of rebuilt words
    :return: list, it will return word_lst
    """
    global dictionary, switch
    if len(current_dict) == word_length:
        for key, value in current_dict.items():
            word += value

        if len(word) == word_length:
            if word not in word_lst:
                word_lst.append(word)

        return word_lst

    else:
        for key, value in character_dict.items():
            if key not in current_dict:
                # Choose
                current_dict[key] = value

                # Explore
                word_lst = helper(character_dict, current_dict, word_length, word, word_lst)

                # Un-choose
                current_dict.pop(key)

        return word_lst


def has_prefix(sub_s):
    """
    :param sub_s: str, a segment of a word that users input
    :return: boolean, tt will return True or False
    """
    global dictionary
    new_dictionary = []
    for element in dictionary:
        if len(element) >= len(sub_s):
            new_dictionary.append(element)
    count = 0
    for word in new_dictionary:
        if word.startswith(sub_s):
            count += 1
            if count > 0:
                break
    if count == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
