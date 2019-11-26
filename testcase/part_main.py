import unittest
import requests
from new_login.testcase.change_password import change
from BeautifulReport import BeautifulReport

def all():
    # with open('./part_main_logs.txt','a',encoding='utf8')as f:
    all_user =unittest.TestLoader()
    test1 = all_user.loadTestsFromTestCase(change)
    test = unittest.TestSuite()
    test.addTests(test1)
    # a = unittest.TextTestRunner(stream=f,verbosity=2)
    # a.run(change())
    return test

if __name__ == '__main__':
    with open('../logs/part_main_logs.txt','a',encoding='utf8')as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(all())


