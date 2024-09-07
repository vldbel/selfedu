from typing import Any


class WordString:
    def __init__(self, string=''):
        self.__string = string
    
    @property
    def string(self):
        return self.__string
    
    @string.setter
    def string(self, value):
        self.__string = value
        
    def __len__(self):
        """len(words) - должно возвращаться число слов в переданной строке 
            (слова разделяются одним или несколькими пробелами);"""
        return len(self.__string.split())
    
    def words(self, indx):
        """должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0)."""
        return self.__string.split()[indx]
    
    def __call__(self, idx):
        return self.words(idx)
    
words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")