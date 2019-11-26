import hashlib
import urllib


class Des:
    @classmethod
    def get_md5(self, str):
        m = hashlib.md5()
        m.update(str.encode('utf-8'))
        # print(m.hexdigest())
        return m.hexdigest()

    @classmethod
    def get_sign_str(self,dic):
        list=[]
        for i in dic.keys():
            list.append(i)
        list.sort()
        list2=[]
        # print("xxxx:"+str(list))
        for i in list:
            # value=urllib.parse.quote(dic[i])
            list2.append(str(i)+"="+dic[i])
        sign_str=('&').join(list2)
        # print (sign_str)
        return sign_str

    @classmethod
    def get_sign(self,dic,salt):
        sign_str=Des.get_sign_str(dic)
        sign_str=sign_str+salt
        print (sign_str)
        return Des.get_md5(sign_str)