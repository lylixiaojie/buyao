#!bin/python
# -*- coding: utf-8 -*-

#author:lixiaojie
#date:18.8.17
#this is test api for fist pages
#APP启动的广告页面

import requests

url_api_first_page = 'http://www.buyao.tv/appapi/by_ads.php?appkey=BYMUSICOFFVN0DtKGcebowgEPLtASJfBBn6iOTQ'

def api_test_fist_page():
    request = requests.get(url_api_first_page)
    return request

test = api_test_fist_page()
print(test.text)
