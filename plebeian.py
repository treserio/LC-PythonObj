#!/usr/bin/python3
'''basic person class'''


class Basic_Plebeian:
    '''initial class for inheritance'''

    def validator(self, id, val):
        if type(val) != int:
            raise TypeError(f'{id} must be an integer!')
        elif val <= 0:
            raise TypeError(f'{id} must be greater than 0')
        else:
            return val

    def __init__(self, ht, wt, age):
        self.__ht = self.validator('height', ht)
        self.__wt = self.validator('weight', wt)
        self.__age = self.validator('age', age)

    @property
    def ht(self):
        return self.__ht

    @ht.setter
    def ht(self, val):
        self.__ht = self.validator('height', val)

    # def wt(self):
    #     return self.__wt

    # def set_wt(self, val):
    #     self.__wt = self.validator('wt', val)

    def __str__(self):
        '''return the str rep of the obj'''
        return f'ht: {self.__ht}, wt: {self.__wt}, age: {self.__age}'
