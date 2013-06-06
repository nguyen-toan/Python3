'''
Created on Jun 4, 2013

@author: tnguyen7
'''
import unittest
from datetime import datetime
from mathquiz import *

class TestMathQuiz(unittest.TestCase):
    
    def test_get_random_number_from_1_to_10(self):
        """Test to ensure that the random number generated in math quiz is between 1 and 10 inclusive"""
        random_number = get_random_number()
        self.assertTrue(random_number >= 1 and random_number <= 10, 
                        "The random number id expected to be between 1 and 10 inclusive")
    
    def test_time_difference(self):
        """Test to ensure time difference in seconds is calculated correctly"""
        time1 = datetime(2013,6,4,10,5,15)
        time2 = datetime(2013,6,4,10,5,30)
        self.assertEqual(time_difference(time1, time2), 15,
                        "Time difference between %s and %s is expected to be 15 seconds" % (str(time1), str(time2)))

    def test_get_answer(self):
        """Test to assure if addition result is right or wrong"""
        self.assertEqual(get_answer(1,1,2), "right", "'2 is right!' is expected")
        self.assertEqual(get_answer(1,1,3), "wrong", "'3 is wrong!' is expected")
        
    def test_math_quiz_result(self):
        """Test to assure quiz result to be printed out correctly"""
        quiz = MathQuiz()
        quiz.quiz_time = [1, 2, 3, 2, 1]
        quiz.quiz_ans  = ['right', 'right', 'wrong', 'wrong', 'wrong']
        
        expected_output  = "Question #1 took about 1 seconds to complete and was right.\n"
        expected_output += "Question #2 took about 2 seconds to complete and was right.\n"
        expected_output += "Question #3 took about 3 seconds to complete and was wrong.\n"
        expected_output += "Question #4 took about 2 seconds to complete and was wrong.\n"
        expected_output += "Question #5 took about 1 seconds to complete and was wrong.\n"
        expected_output += "You took 9 seconds to finish the quiz\n"
        expected_output += "Your average time was 1.8 seconds per question\n"
        
        self.assertEqual(str(quiz), expected_output, "The following output is expected:\n%s" % expected_output)
        
if __name__ == "__main__":
    unittest.main()
