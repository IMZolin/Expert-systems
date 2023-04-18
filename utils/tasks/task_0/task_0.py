symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
word = "эксперт".upper()


def get_task(shift: int) -> str:
    result = ""
    for i in range(len(word)):
        char = word[i]
        index = symbols.find(char)
        if index + shift < len(symbols):
            result += symbols[index + shift]
        else:
            result += symbols[(index + shift) % len(symbols)]
    return result


def get_answer() -> str:
    return word
