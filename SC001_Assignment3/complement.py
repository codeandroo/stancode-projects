 """
File: complement.py
Name: Andrew Chao
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program allows users to transfer the original sequence to its complement one.
    """
    sequence = input('Please give me a DNA strand and I\'ll find the complement: ')

    # Case-insensitive: reassign the sequence by making it to the upper-case one
    upper_sequence = sequence.upper()

    ans = build_complement(upper_sequence)
    print('The complement of ' + sequence + ' is ' + ans)


def build_complement(input_sequence):
    """
    :param input_sequence: str, allow users to input a sequence that is going to
    be built complement.
    :return: str, this function will return a sequence that is the complement of
    the input sequence.
    """
    output_sequence = ''
    for s in input_sequence:
        if s == 'A':
            output_sequence += 'T'
        elif s == 'T':
            output_sequence += 'A'
        elif s == 'G':
            output_sequence += 'C'
        else:
            output_sequence += 'G'

    return output_sequence


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
