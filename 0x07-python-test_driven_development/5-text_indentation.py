#!/usr/bin/python3
"""
performs operations on text
this module helps writters with their indentations
it also serves as help to bloggers
it can also be a very useful module for programmers
Just use it right else see the consequence of great power
"""


def text_indentation(text):
    """
    a text indentation function
    this is the only function in this while fil and module
    and even in the whole package hahha
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    prev = ""
    for i in text:
        if i in ['.', '?', ':']:
            print("{0}\n\n".format(i), end='')
        else:
            if prev in ['.', '?', ':']:
                if i != ' ':
                    print(i, end='')
            else:
                print(i, end='')
        prev = i


sample_text = """doing this todnfjdk \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres
"""
