#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_bonus_pay_amount, test_config
from src.question_b.question_b import get_miles_per_hour

class Test_Config(unittest.TestCase):

    def test_question_b_config(self):
        self.assertEqual(True, test_config())


    def test_get_bonus_pay_amount1(self):
        #test that the function get_bonus_pay_amount with value -1 returns "Invalid Arguments"
        self.assertEqual(get_bonus_pay_amount(-1), "Invalid Arguments")
    def test_get_bonus_pay_amount2(self):
        #test that the function get_bonus_pay_amount with value 200 returns 10
        self.assertEqual(get_bonus_pay_amount(200), 10)
    def test_get_bonus_pay_amount3(self):
        #test that the function get_bonus_pay_amount with value 600 returns 36
        self.assertEqual(get_bonus_pay_amount(600), 36)
    def test_get_bonus_pay_amount4(self):
        #test that the function get_bonus_pay_amount with value 1000 returns 70
        self.assertEqual(get_bonus_pay_amount(1000), 70)
    def test_get_bonus_pay_amount5(self):
        #test that the function get_bonus_pay_amount with value 1500 returns 120
        self.assertEqual(get_bonus_pay_amount(1500), 120)
    def test_get_bonus_pay_amount6(self):
        #test that the function get_bonus_pay_amount with value 2000 returns "Invalid Arguments"
        self.assertEqual(get_bonus_pay_amount(2000), "Invalid Arguments")


    def test_get_miles_per_hour1(self):
        #test that the function get_miles_per_hour with values 32 and 60 returns 19.883872
        self.assertEqual(get_miles_per_hour(32, 60), 19.883872)