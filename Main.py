#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)



    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()  # получаем наш текст
        txt1 = text.upper()
        txt = txt1.split()


        print(txt)

        def freq(word):    ## Функция для посимвольного разделения слова,ибо чреез sorted не работает
            freq_dict = {}
            for char in word:
                freq_dict[char] = freq_dict.get(char, 0) + 1
            return freq_dict


        anagram_list = []
        for word_1 in txt:  ## цикл для определния похожих симвлов в словах,
            for word_2 in txt:
                if word_1 != word_2 and (freq(word_1) == freq(word_2)):
                    anagram_list.append(word_1)
        print(sorted(anagram_list))
        if (len(anagram_list)) == 0:
            self.textEdit_words.insertPlainText('В данном словаре нет анаграмм')
        else:
             for kone4 in anagram_list:

                 self.textEdit_words.insertPlainText(kone4+"\n")

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
