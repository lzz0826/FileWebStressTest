import datetime
import time

import requests
import json

# 設定登入帳號
USERNAME = "admin"
PASSWORD = "12345678"
VALIDATION = "666666"
LOGINURL = "http://127.0.0.1:8052/admin/user/login"


def login():
    # 登录信息
    url = LOGINURL
    payload = json.dumps({
        "username": USERNAME,
        "password": PASSWORD,
        "validation": VALIDATION
    })
    headers = {
        'Content-Type': 'application/json'
    }
    login = requests.request("POST", url, headers=headers, data=payload)

    return login


def testUrl(requst, authorization, url):
    payload = ""
    headers = {
        'Authorization': authorization
    }

    print("使用的 Token:"+authorization)
    testUrl = requests.request(requst, url, headers=headers, data=payload)

    return testUrl


if __name__ == '__main__':
    login = login()
    print(login.text)
    response_data = login.json()
    token = response_data['data']['token']

    while True:
        testurldate01 = testUrl("GET", token, "http://127.0.0.1:8052/admin/app/list?appId=2669907272537366808&page=1&pageSize=5")
        print(testurldate01.text)
        time.sleep(1)
        testurldate02 = testUrl("GET", token, "http://127.0.0.1:8052/admin/subApp/list?page=1&pageSize=5")
        print(testurldate02.text)
        now = datetime.datetime.now()
        print("當前時間 =", now.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(3)
