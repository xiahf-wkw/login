import requests
import copy
from port_data.login_port import *
from testcase.sign import *
sign = test_sign(data)
data1 = copy.deepcopy(data)
data1['sign']= sign
data1['uuid']='A00000A1F17A14'
r = requests.post('http://passport.2345.com/clientapi/nLoginConfigCloud/index',data = data1)
print(r.json())


# sign=Des.get_sign(data,"&UCKey=ZjsRBzddDWF2HnyNCqCG2ltCsyiZQPCD")
# data['sign']=sign
# data['uuid']='A00000A1F17A14'
#
# print (sign)
# print (data)
# a = requests.post(url="http://passport.2345.com/clientapi/nLoginConfigCloud/index",data=data)
# print(a.json())