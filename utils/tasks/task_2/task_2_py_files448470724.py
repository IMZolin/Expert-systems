class Candidate:
    level: str = None
    lang: str = None
    degree: str = None
    OS: str = None


def select(c: Candidate):
    if c.level is None: return 0 #ask level
    elif c.lang is None: return 1 #ask lang

    if c.level == 'junior':
        if c.lang == 'python':
            if c.degree is None: return 2 #ask degree
            elif c.degree == 'yes': return 4 #hire
            else:
                if c.OS is None: return 3 #ask OS
                elif c.OS == 'macos': return 4 #hire
        elif c.lang == 'c++':
            if c.degree is None: return 2 #ask degree
            elif c.degree == 'yes': return 4 #hire
        elif c.lang == 'java':
            if c.OS is None: return 3 #ask OS
            elif c.OS == 'linux': return 4 #hire
        elif c.lang == 'r':
            if c.degree is None: return 2 #ask degree
            elif c.OS is None: return 3 #ask OS
            elif c.degree == 'yes' and c.OS == 'macos': return 4 #hire

    if c.level == 'middle':
        if c.lang == 'c++':
            if c.OS is None: return 3 #ask os
            elif c.OS == 'windows': return 4 #hire
        elif c.lang == 'r':
            if c.OS is None: return 3 #ask OS
            elif c.OS == 'linux': return 4 #hire

    if c.level == 'senior':
        if c.lang == 'python':
            if c.OS is None: return 3 #ask OS
            elif c.OS == 'windows': return 4 #hire
        elif c.lang == 'c++': return 4 #hire
        elif c.lang == 'java':
            if c.OS is None: return 3 #ask OS
            elif c.OS == 'windows': return 4 #hire
    #can not hire
    return 5
