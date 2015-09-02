def is_palindrome(sentence):
    new_word = []
    for c in sentence:
        if c.isalpha():
            new_word.append(c.lower())
    return new_word == new_word[::-1]


def main():
    user_input = input("What are we testing today: ")
    is_palindrome(user_input)


if __name__ == '__main__':
    main()
