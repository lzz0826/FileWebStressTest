

import http.client
import json


from login import login
from uploadFile import uploadFile

def versionAdd(token,appId,versionName,subappId,subappName,filename,fileMd5):

    # HTTPConnection HTTPSConnection *注意本地是HTTPConnection
    conn = http.client.HTTPConnection("127.0.0.1", 8052)
    payload = json.dumps({
        "appId": appId,
        "versionName": versionName,
        "subappId": subappId,
        "subappName": subappName,
        "filename": filename,
        "fileMd5": fileMd5
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/admin/version/add", payload, headers)
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


if __name__ == '__main__':
    login = login()
    login_data = login.json()
    print(login_data)
    token = login_data['data']['token']

    #  token  檔名 檔案路徑
    response = uploadFile(token,"test99.zip","/Users/sai/Desktop/test99.zip")
    print(response)
    response_obj = json.loads(response)
    data = response_obj["data"]
    msg = response_obj["msg"]
    statusCode = response_obj["statusCode"]

    if msg == "成功" and statusCode == 0:
        print("上傳成功 執行Version Add")
        # token
        # "appId":
        # "versionName":
        # "subappId":
        # "subappName":
        # "filename":
        # "fileMd5":
        versionAdd = versionAdd(token,"2756525249164616572","1.02","2756525249232073047","test99922999","test99.zip","39c7598d0d6d79ac89f14d948619c0e1")
        print(versionAdd)
    else:
        print("上傳失敗")