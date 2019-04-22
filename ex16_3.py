import unittest, my_math
from subprocess import Popen, PIPE
class ProductTestCase(unittest.TestCase):
    #在这里插入以前的测速
    def test_integers(self):
        for x in range(-10,10):
            for y in range(-10,10):
                p= my_math.product(x,y)
                self.assertEqual(p,x*y,'Integer multiplication failed')
    
    def test_floats(self):
        for x in range(-10,10):
            for y in range(-10,10):
                x = x/10
                y = y/10
                p = my_math.product(x,y)
                self.assertEqual(p,x*y,'Float multiplication failed')
    
    def test_with_PyChecker(self):
        cmd = 'pychecker', '-Q', my_math.__file__.rstrip('c')
        pychecker = Popen(cmd, stdout=PIPE, stderr = PIPE)
        self.assertEqual(pychecker.stdout.read(),'')

    def test_with_PyLint(self):
        cmd = 'pylint', '-rn', 'my_math'
        pylint = Popen(cmd, stdout= PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(),'')

    if __name__ == '__main__': 
        unittest.main()