# sampl test 


from django.test import SimpleTestCase
from . import calc

class CalcTest(SimpleTestCase):
    
    def test_add_numbers(self):
        res = calc.add(4,3)
        
        self.assertEqual(res , 7)
        
        
    def test_sub(self):
        res = calc.substract(10,7)
        
        self.assertEqual(res , 3)
        
