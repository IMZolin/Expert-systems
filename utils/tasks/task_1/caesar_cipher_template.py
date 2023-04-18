# here is a template of a function decodes caesar cipher with definite shift
def caesar_decode(encoded_s: str, shift: int):
    # encoded_s is an encoded word which was given by tg-bot

    decoded_s = ''  # here is your decoded word
    ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    # input your solution here
    # tip: there is a reverse indexing in python (ex: ru_alphabet[-1] = 'я')

    return decoded_s


if __name__ == '__main__':
    # prints all the variants of decoded_word. You need to choose the right.
    for i in range(1, 33):
        print(caesar_decode('', i))
