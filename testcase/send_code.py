import unittest
from new_login.port_data.login_port import send_code




class sendcode_user(unittest.TestCase):
    def test_status_cade(self):
        self.assertEqual(200,send_code.status_code,'接口请求不通，接口返回非200')


if __name__ == '__main__':
    unittest.main(verbosity=2)
