from BeautifulReport import BeautifulReport
import unittest

# 执行testcase中的所有用例或部分用例并生成html格式的测试报告
if __name__ == '__main__':
    report =unittest.defaultTestLoader.discover('./testcase',pattern='**.py')
    result = BeautifulReport(report)
    result.report(filename='part测试报告', description='测试修改密码',report_dir='./logs' )
    # 构建测试报告，文件名为part测试报告，内部用例名：测试修改密码，存储路径为logs