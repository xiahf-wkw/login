import requests
import unittest
from ddt import ddt,file_data
from common.login_port import pw_headers
from common.login_port import cookiedata


@ddt
class change(unittest.TestCase):
    def tset_status_change(self):
        pass
    # @file_data("../configs/password.json")
    def test1_change_password(self):
        value = {
                 'password' :'123456',
                 'mid':'andloginsdk'
                 }
        change_url = requests.post("http://passport.2345.com/clientapi/nPassword/index",data=value,cookies = cookiedata,headers = pw_headers)
        change_url_json = change_url.json()
        self.assertEqual(4001,change_url_json['code'])
    def test_change_msg(self):
        """ 测试修改密码返回信息"""
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
