import unittest
import json
import datetime
import time
import hashlib
import copy



# class times_sign(unittest.TestCase):
def test_times():
    """输出当前时间戳"""
    t = datetime.datetime.now()
    tence_times = json.dumps(int((time.mktime((t.timetuple())))))
    return tence_times
def test_sign(dic):
    """给上报参数加签并返回sign"""
    dic1 = copy.deepcopy(dic)
    list = []
    #dic1.pop('sign')
    # dic1.pop('uuid')
    for i in dic1.items():
        list.append("{}={}".format(i[0], i[1]))
    sign_str = "&".join(list)
    a = sign_str+'&UCKey=ZjsRBzddDWF2HnyNCqCG2ltCsyiZQPCD'
    md5 = hashlib.md5()
    md5.update(a.encode('utf8'))
    sign = md5.hexdigest()
    return sign
# test_times()


# if __name__ == '__main__':
#     unittest.main()

# test_sign(dic):
#     """给上报参数加签并返回sign"""
#     dic1 = copy.deepcopy(dic)
#     list = []
#     #dic1.pop('sign')
#     dic1.pop('uuid')
#     for i in dic1.items():
#         list.append("{}={}".format(i[0], i[1]))
#     sign_str = "&".join(list)
#     a = sign_str+'&UCKey=x16dUyVlpJHcUvlPP0qWgr9XGj3cgWv3'
#     print(a)
#     md5 = hashlib.md5()
#     md5.update(a.encode('utf8'))
#     sign = md5.hexdigest()
#     return sign
# # test_times()
