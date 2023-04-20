from enum import IntEnum


class Candidate:
    level: str = None
    lang: str = None
    degree: str = None
    os: str = None

    def __init__(self, _level=None, _lang=None, _degree=None, _os=None):
        self.level = _level
        self.lang = _lang
        self.degree = _degree
        self.os = _os


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

    В программе уже реализована часть функциональности для большего понимания, но в рамках
    поставленной задачи, этот код будет неверным, поэтому вам нужно его переписать
    """

    # perf_candidate = [junior, python/cpp/java, yes, windows/linux]
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
                if c.os is None:
                    return QuestionEnum.OS
                elif c.os == 'macos':
                    return QuestionEnum.HIRE
    # do not hire
    return QuestionEnum.DECLINE


if __name__ == '__main__':
    candidates: list[Candidate] = list()
    candidates.append(Candidate(_level=None, _lang='python', _degree='yes', _os=None))
    candidates.append(Candidate(_level='middle', _lang='cpp', _degree='no', _os='linux'))
    candidates.append(Candidate(_level='middle', _lang='python', _degree='yes', _os='windows'))
    candidates.append(Candidate(_level='senior', _lang='python', _degree='yes', _os='linux'))
    candidates.append(Candidate(_level='junior', _lang='java', _degree='yes', _os='macos'))
    candidates.append(Candidate(_level='junior', _lang='java', _degree='no', _os='macos'))
    candidates.append(Candidate(_level=None, _lang='R', _degree=None, _os=None))
    candidates.append(Candidate(_level='senior', _lang=None, _degree='yes', _os=None))
    candidates.append(Candidate(_level='junior', _lang=None, _degree='no', _os=None))
    candidates.append(Candidate(_level='senior', _lang='cpp', _degree='yes', _os='windows'))
    candidates.append(Candidate(_level='junior', _lang='python', _degree='yes', _os='linux'))
    questions: list[QuestionEnum] = list()
    for candidate in candidates:
        questions.append(select(candidate))
    print(*questions)
