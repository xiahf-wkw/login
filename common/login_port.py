import requests
import datetime
import time

jar = requests.cookies.RequestsCookieJar()
cookiedata = {
    "i": "500034611", "u": "500034611", "n": "%CA%D6%BB%FA%D3%C3%BB%A7_9f2b94e726", "m": "200", "t": "1574327909.68098200", "s": "9c85f821eaa9dfdf3a8b55529f3bcb81", "v": "1.1"
}
jar.set('I', str(cookiedata), domain="passport.2345.com", path="/")

pw_headers = {
            # "Cookie":{
            #     "I":{
            #         "i":"500034611","u":"500034611","n":"%CA%D6%BB%FA%D3%C3%BB%A7_9f2b94e726","m":"200","t":"1574244681.1638100","s":"9c85f821eaa9dfdf3a8b55529f3bcb81","v":"1.1"
            #     }
            # },
            "Content-Type":"application/x-www-form-urlencoded",
            "Content-Length":"219",
            "Host":"passport.2345.com",
            "Connection":"Keep-Alive",
            "Accept-Encoding":"gzip",
            "User-Agent":"okhttp/3.12.0"
            }
password = requests.post(url= "http://passport.2345.com/clientapi/nUserLogin/index",headers = pw_headers,
                         data={'mid':'andloginSDK',
                               'password':'57D1E946B5A695AE43B9073628FB1254E83B145D4D1C59B9B0696113F9A6D68B6575C83DEA76F0938520E9CBFA4A30F4',
                               'flToken':'e9c67c75a2907891821483db69a7fa15',
                               '用户名字段':'C2C7D635E3991C5DCA5B904A0110D484'
                               }
                         )

# 密码登录

send_code = requests.post(url='http://passport.2345.com/clientapi/nPhone/sendBindCode',
                         data={'mid':'andloginSDK',
                               'sendType':'bindCode'
                               }
                         )

# 绑定手机发送验证码

change_password = requests.post(url='http://passport.2345.com/clientapi/nPassword/index',
                                data={'password':'b01bd951077462be379b59f01ff9ef23',
                                      'mid':'andloginSDK'
                                      }
                                )


data_time = datetime.datetime.now()
un_time = time.mktime(data_time.timetuple())

config_hicky = requests.post(url="http://passport.2345.com/clientapi/nLoginConfigCloud/index",
                      data = {
                        'appChannel': 'APP_CHANNEL',
                        'appName': '用户中心',
                        'appVersion': '2',
                        'device': '0AE7E6222C770067B00B544661DA93B907654EB82845EA59BFF7C54E7521246CA7BF16862308C81D76671FAA9624B5109779C4AC42E2C2ED8BDE3AA64C19303FFB788F54D751497DAC52A0FF90F3188681A0F9E3C6F1ED7C53FDDE11C466F9AF',
                        'mid': 'andloginSDK',
                        'packageName': 'com.mobile2345.uc.sample',
                        'sdkVersion': '3.0.3beta1-SNAPSHOT',
                        'timestamp': "%s" %int(time.time()),
                        # 'sign': 'c878a44b8264cb57390560c0a2eccd8d',
                        # 'uuid': '869633042292837'
                             }
                             )

# 获取配置接口

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
# 配置获取接口data参数








