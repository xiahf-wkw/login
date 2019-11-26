import copy
import hashlib
import urllib
import datetime
import json
import time


def test_sign(dic):
    """给上报参数加签并返回sign"""
    dic1 = copy.deepcopy(dic)
    list = []
    #dic1.pop('sign')
    dic1.pop('uuid')
    for i in dic1.items():
        list.append("{}={}".format(i[0], i[1]))
    sign_str = "&".join(list)
    a = sign_str+'&UCKey=x16dUyVlpJHcUvlPP0qWgr9XGj3cgWv3'
    md5 = hashlib.md5()
    md5.update(a.encode('utf8'))
    sign = md5.hexdigest()
    return sign
# test_times()

