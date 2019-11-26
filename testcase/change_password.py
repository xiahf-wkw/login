import requests
import unittest
from ddt import ddt,file_data
from new_login.port_data.login_port import pw_headers
from new_login.port_data.login_port import cookiedata


@ddt
class change(unittest.TestCase):
    def tset_status_change(self):
        pass
    @file_data("../port_data/password.json")
    def test1_change_password(self,password,mid):
        value = {
                 'password' :password,
                 'mid':mid
                 }
        change_url = requests.post("http://passport.2345.com/clientapi/nPassword/index",data=value,cookies = cookiedata,headers = pw_headers)
        change_url_json = change_url.json()
        self.assertEqual(4001,change_url_json['code'])
    def test_change_msg(self):
        """ 测试修改密码返回信息"""
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
