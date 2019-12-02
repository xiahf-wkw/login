import unittest
from testcase.password import *
from testcase.change_password import *
from testcase.send_code import *
from testcase.config import *
from BeautifulReport import BeautifulReport
import datetime




def all_case():
    loader = unittest.TestLoader()
    suit = unittest.TestSuite()
    suit.addTests([loader.loadTestsFromTestCase(change),
                   loader.loadTestsFromTestCase(pw),
                   loader.loadTestsFromTestCase(sendcode_user),
                   loader.loadTestsFromTestCase(config_isused)])
    return suit

if __name__ == '__main__':
    with open(f'./logs/{str(datetime.date.today())+ "logs"}.txt',mode='a',encoding='utf8')as file:
        runner = unittest.TextTestRunner(stream=file,verbosity=2)
        runner.run(all_case())
    # 执行testcase中的所有用例或部分用例并生成html格式的测试报告
    report = unittest.defaultTestLoader.discover('./testcase', pattern='**.py')
    result = BeautifulReport(report)
    result.report(filename=f'{datetime.date.today()}测试报告', description='测试修改密码', report_dir='./reports')
    # 构建测试报告，文件名为part测试报告，内部用例名：测试修改密码，存储路径为logs

