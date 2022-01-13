#!/usr/bin/python3
'''centurion class'''

Pleb = __import__('plebeian').Basic_Plebeian


class Centurion(Pleb):
    '''an advanced plebeian'''

    def __init__(self, ht, wt, age, horse=False, armor=1):
        print('in Cent init')
        super().__init__(ht, wt, age)
        self.horse = horse
        self.armor = self.validator('armor', armor)
