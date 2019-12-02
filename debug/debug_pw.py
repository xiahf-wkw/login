import requests
import time
import copy
import hashlib
from common.sign import *
url = "http://passport.2345.com/clientapi/check/faction"
dic = {
   "clientVer": "3",
   "mid": "andbs",
    "timestamp":int(time.time()),
    "v":"1.0.2"

   # "sign": "b1d839eb05a48390ae090e33eca483e6"
}
# #
dic1 = copy.deepcopy(dic)
list = []
# dic1.pop('sign')
# dic1.pop('uuid')
for i in dic1.items():
    list.append("{}={}".format(i[0], i[1]))
sign_str = "&".join(list)
a = sign_str + '&UCKey=ZjsRBzddDWF2HnyNCqCG2ltCsyiZQPCD'
md5 = hashlib.md5()
md5.update(a.encode('utf8'))
sign = md5.hexdigest()
dic["sign"] = sign
print(sign)
# #
r = requests.post(url=url,data=dic)
print(r.json())



