#!/usr/bin/python3
'''praefectus class'''

Cent = __import__('centurion').Centurion


class Praefectus(Cent):
    '''above Centurion'''

    def __init__(
        self,
        ht,
        wt,
        age,
        horse=True,
        armor=10,
        aids=2
    ):
        super().__init__(ht, wt, age, horse, armor)
        self.aids = aids
