import requests
from common.sign import *
import unittest

data = {
    'appChannel': 'APP_CHANNEL',
    'appName': '用户中心',
    'appVersion': '2',
    'device': '0AE7E6222C770067B00B544661DA93B907654EB82845EA59BFF7C54E7521246CA7BF16862308C81D76671FAA9624B5109779C4AC42E2C2ED8BDE3AA64C19303FFB788F54D751497DAC52A0FF90F3188681A0F9E3C6F1ED7C53FDDE11C466F9AF',
    'mid': 'andloginSDK',
    'packageName': 'com.mobile2345.uc.sample',
    'sdkVersion': '3.0.3beta1-SNAPSHOT',
    'timestamp': "%s" % int(time.time()),
    # 'sign': 'c878a44b8264cb57390560c0a2eccd8d',
    # 'uuid': '869633042292837'
}
sign = test_sign(data)
data1 = copy.deepcopy(data)
data1['sign']= sign
data1['uuid']='A00000A1F17A14'
config = requests.post('http://passport.2345.com/clientapi/nLoginConfigCloud/index',data = data1)


def test_status_code():
    """接口是否200"""
    config_request = config.json()
    if config_request['code'] == 205:
        return True

class config_isused(unittest.TestCase):

    @unittest.skipUnless(test_status_code(),"接口请求则不通跳过此方法")
    def test_sqdl(self):
        config_request = config.json()
        if config_request['data']['isUnionLogin'] == True:
            return "授权登录打开"
        else:
            return "授权登录关闭"

    @unittest.skipUnless(test_status_code(), "接口请求则不通跳过此方法")
    def test_jmdl(self):
        config_request = config.json()
        if config_request['data']['isQuietLogin'] == True:
            return "静默登录打开"
        else:
            return "静默登录关闭"

    @unittest.skipUnless(test_status_code(), "接口请求则不通跳过此方法")
    def test_ali(self):
        config_request = config.json()
        if config_request['data']['isNeedShanyan'] == True:
            return "阿里云登录打开"
        else:
            return "阿里云登录关闭"

    @unittest.skipUnless(test_status_code(), "接口请求则不通跳过此方法")
    def test_yhxy(self):
        config_request = config.json()
        if config_request['data']['protocolStatus'] == True:
            return "用户协议默认打开"
        else:
            return "用户协议默认关闭"


if __name__ == '__main__':
    unittest.main(verbosity=2)






# sign=Des.get_sign(data,"&UCKey=ZjsRBzddDWF2HnyNCqCG2ltCsyiZQPCD")
# data['sign']=sign
# data['uuid']='A00000A1F17A14'
#
# print (sign)
# print (data)
# a = requests.post(url="http://passport.2345.com/clientapi/nLoginConfigCloud/index",data=data)
# print(a.json())