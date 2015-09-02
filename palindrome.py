def is_palindrome(sentence):
    # Check if the len of the sentence is greater than 1
    # import pdb; pdb.set_trace()
    if len(sentence) <= 1:
        return True

    # Create an empty list to hold our sentence broken up
    new_word = []

    # Looping through the sentence, and removing anything that is not a
    # lowercase alpa character
    for c in sentence:
        if c.isalpha():
            new_word.append(c.lower())

    # Check if the first and last characters of the sentence are the
    # same. If they are, pass the remaining characters back to func.
    if new_word[0] == new_word[-1]:
        is_palindrome(''.join(new_word[1:-1]))
    else:
        return False

    return True


def main():
    user_input = input("What are we testing today: ")
    print(is_palindrome(user_input))


if __name__ == '__main__':
    main()
