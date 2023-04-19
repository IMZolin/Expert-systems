from enum import IntEnum


class QuestionEnum(IntEnum):
    LVL = 0
    LANG = 1
    DEGREE = 2
    OS = 3
    HIRE = 4
    DECLINE = 5


class Candidate:
    level: str = None
    lang: str = None
    degree: str = None
    OS: str = None


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

    # do not hire
    return QuestionEnum.DECLINE
