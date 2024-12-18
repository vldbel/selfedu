"""Подвиг 7 (на повторение). Необходимо в программе объявить класс VideoItem для представления одного видео"""

class VideoItem:
    def __init__(self, title:str, descr:str, path:str):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()

class VideoRating:
    _rating_range = (0, 6)
    def __init__(self, rating=0):
        self.__rating = rating
    
    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, val):
        if val not in range(*self._rating_range):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = val
    

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
# v.rating.rating = 6  # ValueError