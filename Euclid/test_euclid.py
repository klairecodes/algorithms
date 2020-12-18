import unittest
import time

from euclid import euclid

class Test_euclid(unittest.TestCase):
    # Tests a couple interesting values and edge cases
    def test_nums(self):
        data = {
        'in_a': [1599, 3009, 40902, 14157, 2, 1],
        'in_b': [650, 884, 24140, 5950, 2, 0],
        'ans': [13, 17, 34, 1, 2, 1]}
        
        for i in range(len(data['ans'])):
            result = euclid(data['in_a'][i], data['in_b'][i])
            self.assertEqual(result, data['ans'][i])

if __name__ == '__main__':
    unittest.main()
