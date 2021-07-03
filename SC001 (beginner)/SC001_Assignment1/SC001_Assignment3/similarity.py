"""
File: similarity.py
Name: Andrew Chao
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The user is allowed to input a long sequence and a short sequence.
    Then, this program will help the user to identify which part of the long sequence
    is the most similar to the short one.
    That is to say, the user will get a sequence that is the closest to the short one
    from the long one.
    """

    # Allow user to input 2 different sequences with different lengths
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match? ')

    # Case-insensitive: reassign each sequence by making them to upper-case ones
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()

    match_result = examine(long_sequence, short_sequence)
    print('The best match is '+match_result)


def examine(long, short):
    """
    :param long: str, users can input a long sequence.
    :param short: str, users can input a short sequence.
    :return: str, The small part of long sequence that has the highest similarity to the short one.
    """
    l = len(long)
    s = len(short)
    maximum = 0
    best_sequence = ''

    # how many steps that short sequence should move to match the long one
    for i in range(l - s + 1):

        # The part of long sequence that is used to be matched with the short one each time
        p = long[i:i + s]

        c = short

        # Leverage match function to find similarity percent
        result = match(p, c)

        # The first result must be the maximum in the first round
        if i == 0:
            maximum = result
            best_sequence = p

        # After the first round, it should compare which sequence has the higher similarity
        else:
            if result > maximum:
                maximum = result
                best_sequence = p

    return best_sequence


def match(parent, child):
    """
    :param parent: str, user can input a sequence that is going to be matched.
    :param child: str, user can input a sequence that is going to match with parent.
    :return: float, the ratio of how similar the child is to the parent.
    """
    c = len(child)
    numerator = 0
    denominator = 0

    for i in range(c):
        if child[i] == parent[i]:
            numerator += 1
            denominator += 1
        else:
            denominator += 1
    similarity_percent = numerator / denominator
    return similarity_percent


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
