import unittest
from new_login.testcase.password import *
from new_login.testcase.change_password import *
from new_login.testcase.send_code import *



def all_case():
    loader = unittest.TestLoader()
    suit = unittest.TestSuite()
    suit.addTests([loader.loadTestsFromTestCase(change),loader.loadTestsFromTestCase(pw),loader.loadTestsFromTestCase(sendcode_user)])
    return suit

if __name__ == '__main__':
    with open('./logs/all_logs.txt',mode='a',encoding='utf8')as file:
        runner = unittest.TextTestRunner(stream=file,verbosity=2)
        runner.run(all_case())