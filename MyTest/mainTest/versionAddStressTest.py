import json
import time
import sys
sys.path.append('/Users/sai/PycharmProjects/pythonProject/MyTest/testURL')
from login import login
from uploadFile import uploadFile
from versionAdd import versionAdd



if __name__ == '__main__':
    login = login()
    login_data = login.json()
    print(login_data)
    token = login_data['data']['token']

    #  token  檔名 檔案路徑
    response = uploadFile(token, "test99.zip", "/Users/sai/Desktop/test99.zip")
    print(response)
    response_obj = json.loads(response)
    data = response_obj["data"]
    msg = response_obj["msg"]
    statusCode = response_obj["statusCode"]

    if msg == "成功" and statusCode == 0:
        print("上傳成功 執行Version Add")
        versionName = "1.02"
        while True:
            # token
            # "appId":
            # "versionName":
            # "subappId":
            # "subappName":
            # "filename":
            # "fileMd5":
            versionAdd_func = versionAdd
            response = versionAdd_func(token, "2756525249164616572", versionName, "2756525249232073047", "test99922999",
                                       "test99.zip", "39c7598d0d6d79ac89f14d948619c0e1")
            print(response)
            versionAdd_data = json.loads(response)
            statusCode = versionAdd_data["statusCode"]
            msg = versionAdd_data["msg"]
            print(statusCode)
            print(msg)
            versionName = str(float(versionName) + 0.01)
            time.sleep(60)
    else:
        print("上傳失敗")