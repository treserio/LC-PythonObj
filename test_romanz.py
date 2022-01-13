import unittest
from plebeian import Basic_Plebeian


class Test_Romanz(unittest.TestCase):

    argz = [100, 101, 102]

    def test_pleb(self):
        with self.assertRaises(TypeError):
            john = Basic_Plebeian(-1, 0, 20)
        with self.assertRaises(TypeError):
            john2 = Basic_Plebeian("thangs", 0, 20)
        john3 = Basic_Plebeian(*self.argz)
        self.assertEqual(john3.ht, 100)
        with self.assertRaises(AttributeError):
            self.assertEqual(john3.wt(), 101)
