from ast import Num
from tkinter import CENTER


def linha(num=42):
    print('—' * num)


def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()


def rodape(txt):
    linha()
    print(txt.center(42))
    linha()
