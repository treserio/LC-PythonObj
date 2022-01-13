#!/usr/bin/python3
'''basic HolbertonStudent class'''


class Holbey:
    '''our Holberton Student class'''

    def __init__(
        self,
        *args,
        **kwargs
        # nm,
        # ch,
        # sp,
        # ht,
        # wbs=0,
        # bt=None
    ):
        '''initializes my Holbey class'''
        if args:
            for i in range(len(args)):
                setattr(self, str(i), args[i])
        if kwargs:
            print(kwargs)
            for (key, val) in kwargs.items():
                print(key, "=", val)
                setattr(self, key, val)

        # self._name = nm
        # self._cohort = ch
        # self._spec = sp
        # self._height = ht
        # self._white_board_skills = wbs
        # self._blood = bt
