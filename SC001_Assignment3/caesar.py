"""
File: caesar.py
Name: Andrew Chao
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The Caesar decipher program can help users to decipher the secret sequence.
    Users need to input a number that will help the alphabet shift in a different order.
    Then, when users enter the secret sequence, this program can base on the shifted amount
    and translate the ciphered string into the correct string in an alphabet order.
    """
    secret_num = int(input('Secret number: '))
    ciphered_string = input('What\'s the ciphered string? ')

    # Case-insensitive: reassign the ciphered string by making it to the upper-case one
    ciphered_string = ciphered_string.upper()

    ans = decode(secret_num, ALPHABET, ciphered_string)
    print('The deciphered string is: ' + ans)


def decode(num, sequence, input_text):
    """
    :param num: int, allow users to input a number that is used to offset the original order in the sequence.
    :param sequence: str, the sequence (ALPHABET) that users want to shift the order.
    :param input_text: str, allow users to input texts to be decoded.
    :return: str, return the decoded texts.
    """
    ori = sequence
    new = new_sequence(num, sequence)
    t = len(input_text)
    ans = ''
    for i in range(t):

        # When the character is not a space or a symbol
        if new.find(input_text[i]) != -1:

            # Find the index of this character in the new sequence
            pre = new.find(input_text[i])

            # Use the index to find the deciphered character
            post = sequence[pre]

            ans += post

        else:
            ans += input_text[i]

    return ans


def new_sequence(num, sequence):
    """
    :param num: int, allow users to input a number that is used to offset the original order in the sequence (ALPHABET).
    :param sequence: str, the sequence (ALPHABET) that users want to shift the order.
    :return: str, the new sequence (ALPHABET) with a new order.
    """
    s = len(sequence)
    first_half = sequence[:s-num]
    second_half = sequence[s-num:]
    new = second_half + first_half
    return new


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
