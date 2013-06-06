'''
Created on Jun 4, 2013

@author: tnguyen7
'''
import random
from datetime import datetime
   
def get_random_number():
    """Return a random integer between 1 and 10 inclusive"""
    return random.randrange(1, 10)

def input_answer(num1, num2):
    """
    Return the addition answer of two numbers from user
    """
    try:
        return int(input("What is the sum of %d and %d? " % (num1, num2)))
    except ValueError:
        print("Answer must be integer. Enter again!")
        return input_answer(num1, num2)

def time_difference(time1, time2):
    """
    Return the time difference in seconds between two datetime objects
    Requirement: time2 must be after time1 regarding time order
    """
    delta = time2 - time1
    return delta.seconds

def get_answer(num1, num2, answer):
    """
    Check if 'answer' is equal to the addition of 'num1' and 'num2'
    Return "right" if it is true and "wrong" otherwise
    """
    if (answer == num1 + num2):
        return "right"
    else:
        return "wrong"
 
def print_answer(num1, num2, answer):
    print("%d is %s!" % (answer, get_answer(num1, num2, answer)))
    
class MathQuiz:
    
    def __init__(self):
        self.quiz_num = 5
        self.quiz_time = []
        self.quiz_ans = []
            
    def run(self):
        """
        Print out the quizzes, get the user inputs and print out the answer 
        """
        for count in range(self.quiz_num):
            num1 = get_random_number()
            num2 = get_random_number()
            start_time = datetime.now()
            answer = input_answer(num1, num2)
            end_time = datetime.now()
            print_answer(num1, num2, answer)
            
            self.quiz_ans.append(get_answer(num1, num2, answer))
            self.quiz_time.append(time_difference(start_time, end_time)) 
     
    def __str__(self):
        """Return the summary output"""
        result = ""
        for count in range(self.quiz_num):
            result += "Question #%d took about %d seconds to complete and was %s.\n" % (count+1, self.quiz_time[count], self.quiz_ans[count])
        result += "You took %d seconds to finish the quiz\n" % sum(self.quiz_time)
        result += "Your average time was %0.1f seconds per question\n" % (sum(self.quiz_time) / self.quiz_num)
        return result
    
    def print_result(self):
        print(self)
    
if __name__ == "__main__":
    quiz = MathQuiz()
    quiz.run()
    quiz.print_result()
