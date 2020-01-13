import unittest
from BMI import *

class testbmi(unittest.TestCase):
    #tests of the function name-calculation_bmi(height,weight)
    def test_bmi_calc1(self):
        height=2
        weight=16
        expected=4.0
        result=calculation_bmi(height,weight)
        self.assertEqual(result,expected)


    def test_bmi_calc2(self):
        height=0
        weight=16
        expected="The height is Illegal"
        result=calculation_bmi(height,weight)
        self.assertEqual(result,expected)

    #tests of the function name-analysis_bmi(bmi_num)

    def test_bmi_analysis1(self):
        bmi=17
        expected="Underweight"
        result=analysis_bmi(bmi)
        self.assertEqual(result,expected)

    def test_bmi_analysis2(self):
        bmi=19
        expected="Normalweight"
        result=analysis_bmi(bmi)
        self.assertEqual(result,expected)

    def test_bmi_analysis3(self):
        bmi=25
        expected="Deadweight"
        result=analysis_bmi(bmi)
        self.assertEqual(result,expected)

    def test_bmi_analysis4(self):
        bmi=31
        expected="obesity level 1"
        result=analysis_bmi(bmi)
        self.assertEqual(result,expected)

    def test_bmi_analysis5(self):
        bmi=36
        expected="obesity level 2"
        result=analysis_bmi(bmi)
        self.assertEqual(result,expected)

    def test_bmi_analysis6(self):
        bmi=40
        expected="obesity level 3"
        result=analysis_bmi(bmi)
        self.assertEqual(result,expected)






