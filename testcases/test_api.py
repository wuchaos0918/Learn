# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2023-9-21 15:27
# @Project : Learn.py
# @File    : test_api.py
# ______________________________
import requests

class Testapi:
    def test_get_token(self):
        url = "https://www.zhibo8.com"
        datas = {

        }
        res = requests.get(url, params=datas)
        print(res.text)
        # print(res.json())
        print(res.status_code)
        print(res.cookies)


if __name__ == '__main__':
    Testapi().test_get_token()



# requests.get(url, params=None, **kwargs)
# requests.post(url, data=None, json=None, **kwargs)
# requests.put(url, data=None, **kwargs)
# requests.delete(url, **kwargs)
# requests.request(method, url, **kwargs)
# requests.session()
