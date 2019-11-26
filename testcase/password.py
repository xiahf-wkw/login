import unittest
import requests
from new_login.port_data.login_port import password


class pw(unittest.TestCase):
    def test_pwstatus_code(self):
        self.assertEqual(200,password.status_code,'接口请求失败，返回值非200')


if __name__ == '__main__':
    unittest.main(verbosity=2)

