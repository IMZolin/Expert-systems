import random
from enum import IntEnum


class Candidate:
    level: str = None
    lang: str = None
    degree: str = None
    OS: str = None

    def get_by(self, attr: str) -> str:
        if attr == 'level':
            return self.level
        if attr == 'lang':
            return self.lang
        if attr == 'degree':
            return self.degree
        if attr == 'OS':
            return self.OS

class QuestionEnum(IntEnum):
    LVL = 0
    LANG = 1
    DEGREE = 2
    OS = 3
    HIRE = 4
    DECLINE = 5


def select(c: Candidate) -> QuestionEnum:
    """
    Функция реализует стратегию управления

    Параметры:
        с (Candidate): текущее состояние кандидата. Все поля Candidate представляют собой строки из маленьких букв
                       не меняйте состояние кандидата!

    Возвращаемое значение:
        (QuestionEnum) - элемент из енама

    Возвращайте код QuestionEnum согласно желаемому вопросу или принятому решению

    Если хотите спросить про уровень (level), верните QuestionEnum.LVL
    Если хотите спросить про язык (lang), верните QuestionEnum.LANG
    Если хотите спросить про высшее образование (degree), верните QuestionEnum.DEGREE
    Если хотите спросить про ОС (OS), верните QuestionEnum.OS

    Если хотите принять человека на работу, верните QuestionEnum.HIRE
    Если хотите отказать человеку, верните QuestionEnum.DECLINE

    В программе уже реализована часть функциональности для большего понимания
    """

    if c.level is None:
        return QuestionEnum.LVL
    elif c.lang is None:
        return QuestionEnum.LANG

    if c.level == 'junior':
        if c.lang == 'python':
            if c.degree is None:
                return QuestionEnum.DEGREE
            elif c.degree == 'yes':
                return QuestionEnum.HIRE
            else:
                if c.OS is None:
                    return QuestionEnum.OS
                elif c.OS == 'macos':
                    return QuestionEnum.HIRE

        elif c.lang == 'c++':
            if c.degree is None:
                return QuestionEnum.DEGREE
            elif c.degree == 'yes':
                return QuestionEnum.HIRE

        elif c.lang == 'java':
            if c.OS is None:
                return QuestionEnum.OS
            elif c.OS == 'linux':
                return QuestionEnum.HIRE

        elif c.lang == 'r':
            if c.degree is None:
                return QuestionEnum.DEGREE
            elif c.degree == 'yes':
                if c.OS is None:
                    return QuestionEnum.OS
                elif c.OS == 'macos':
                    return QuestionEnum.HIRE

    elif c.level == 'middle':
        if c.lang == 'c++':
            if c.OS is None:
                return QuestionEnum.OS
            elif c.OS == 'windows':
                return QuestionEnum.HIRE
        elif c.lang == 'r':
            if c.OS is None:
                return QuestionEnum.OS
            elif c.OS == 'linux':
                return QuestionEnum.HIRE

    elif c.level == 'senior':
        if c.lang == 'python':
            if c.OS is None:
                return QuestionEnum.OS
            elif c.OS == 'windows':
                return QuestionEnum.HIRE

        elif c.lang == 'c++':
            return QuestionEnum.HIRE

        elif c.lang == 'java':
            if c.OS is None:
                return QuestionEnum.OS
            elif c.OS == 'windows':
                return QuestionEnum.HIRE

    # do not hire
    return QuestionEnum.DECLINE





class Test:
    c: Candidate
    decision: int

    def __init__(self, c: Candidate, decision: int):
        self.c = c
        self.decision = decision


questions = ['- What is your level?',  # 0
             '- What is your programming language?',  # 1
             '- Do you have a university degree?[y/n]',  # 2
             '- What is your favourite OS?',  # 3
             '- You are hired!',  # 4
             '- We can not hire you'  # 5
             ]


def CheckAnswer(q: int, a: str) -> bool:
    if q == 0:
        if a == 'junior' or a == 'jun' \
                or a == 'middle' or a == 'mid' \
                or a == 'senior' or a == 'sen':
            return True

    elif q == 1:
        if a == 'python' or a == 'py' \
                or a == 'c++' \
                or a == 'java' \
                or a == 'r':
            return True

    elif q == 2:
        if a == 'yes' or a == 'y' \
                or a == 'no' or a == 'n':
            return True


    elif q == 3:
        if a == 'linux' \
                or a == 'windows' or a == 'win' \
                or a == 'macos':
            return True

    return False


def Update(c: Candidate, q: int, a: str):
    if q == 0:
        if a == 'jun':
            c.level = 'junior'
        elif a == 'mid':
            c.level = 'middle'
        elif a == 'sen':
            c.level = 'senior'
        else:
            c.level = a

    elif q == 1:
        if a == 'py':
            c.lang = 'python'
        else:
            c.lang = a

    elif q == 2:
        if a == 'y':
            c.degree = 'yes'
        elif a == 'n':
            c.degree = 'no'
        else:
            c.degree = a

    elif q == 3:
        if a == 'win':
            c.OS = 'windows'
        else:
            c.OS = a


def main():
    score = 0
    size = 20
    fine = 10
    guesses = 0
    arr = []

    for i in range(10):
        arr.append(Test(Candidate(), 4))  # must hire
    for i in range(10):
        arr.append(Test(Candidate(), 5))  # must decline

    arr[0].c.level = 'junior'
    arr[0].c.lang = 'python'
    arr[0].c.degree = 'no'
    arr[0].c.OS = 'macos'
    arr[1].c.level = 'junior'
    arr[1].c.lang = 'python'
    arr[1].c.degree = 'yes'
    arr[1].c.OS = 'windows'
    arr[2].c.level = 'senior'
    arr[2].c.lang = 'python'
    arr[2].c.degree = 'yes'
    arr[2].c.OS = 'windows'
    arr[3].c.level = 'junior'
    arr[3].c.lang = 'c++'
    arr[3].c.degree = 'yes'
    arr[3].c.OS = 'linux'
    arr[4].c.level = 'middle'
    arr[4].c.lang = 'c++'
    arr[4].c.degree = 'no'
    arr[4].c.OS = 'windows'
    arr[5].c.level = 'senior'
    arr[5].c.lang = 'c++'
    arr[5].c.degree = 'no'
    arr[5].c.OS = 'macos'
    arr[6].c.level = 'junior'
    arr[6].c.lang = 'java'
    arr[6].c.degree = 'yes'
    arr[6].c.OS = 'linux'
    arr[7].c.level = 'senior'
    arr[7].c.lang = 'java'
    arr[7].c.degree = 'no'
    arr[7].c.OS = 'windows'
    arr[8].c.level = 'junior'
    arr[8].c.lang = 'r'
    arr[8].c.degree = 'yes'
    arr[8].c.OS = 'macos'
    arr[9].c.level = 'middle'
    arr[9].c.lang = 'r'
    arr[9].c.degree = 'no'
    arr[9].c.OS = 'linux'

    arr[10].c.level = 'junior'
    arr[10].c.lang = 'python'
    arr[10].c.degree = 'no'
    arr[10].c.OS = 'windows'
    arr[11].c.level = 'senior'
    arr[11].c.lang = 'python'
    arr[11].c.degree = 'yes'
    arr[11].c.OS = 'linux'
    arr[12].c.level = 'middle'
    arr[12].c.lang = 'python'
    arr[12].c.degree = 'yes'
    arr[12].c.OS = 'macos'
    arr[13].c.level = 'junior'
    arr[13].c.lang = 'c++'
    arr[13].c.degree = 'no'
    arr[13].c.OS = 'windows'
    arr[14].c.level = 'middle'
    arr[14].c.lang = 'c++'
    arr[14].c.degree = 'yes'
    arr[14].c.OS = 'linux'
    arr[15].c.level = 'junior'
    arr[15].c.lang = 'java'
    arr[15].c.degree = 'yes'
    arr[15].c.OS = 'windows'
    arr[16].c.level = 'middle'
    arr[16].c.lang = 'java'
    arr[16].c.degree = 'yes'
    arr[16].c.OS = 'macos'
    arr[17].c.level = 'senior'
    arr[17].c.lang = 'r'
    arr[17].c.degree = 'no'
    arr[17].c.OS = 'windows'
    arr[18].c.level = 'senior'
    arr[18].c.lang = 'java'
    arr[18].c.degree = 'yes'
    arr[18].c.OS = 'macos'
    arr[19].c.level = 'junior'
    arr[19].c.lang = 'r'
    arr[19].c.degree = 'no'
    arr[19].c.OS = 'macos'

    c = Candidate()
    arr = random.sample(arr, k=len(arr))
    for i in range(size):

        points = 5

        while (True):
            index = select(c)

            # question
            if index >= 0 and index <= 3:
                points = points - 1  # more questions == less points
                if index == 0:
                    ans = arr[i].c.level
                elif index == 1:
                    ans = arr[i].c.lang
                elif index == 2:
                    ans = arr[i].c.degree
                elif index == 3:
                    ans = arr[i].c.OS

                Update(c, index, ans)

            # decision
            elif index == 4 or index == 5:
                if index == arr[i].decision:
                    score = score + points
                    guesses = guesses + 1
                else:
                    score -= fine
                c = Candidate()
                break

    print(guesses)
    print(score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()