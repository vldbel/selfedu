class Person:
    def __init__(self, fio:str, job:str, old:int, salary:float|int, year_job:int):
        self._fio = fio
        self._job = job
        self._old = old
        self._salary = salary
        self._year_job = year_job
    

p = Person():

