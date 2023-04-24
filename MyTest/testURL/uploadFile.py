
import http.client
import mimetypes
import json


from login import login
from codecs import encode


def uploadFile(token,filename,filepath):
    # HTTPConnection HTTPSConnection *注意本地是HTTPConnection
    conn = http.client.HTTPConnection("127.0.0.1", 8052)
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format(filename)))

    fileType = mimetypes.guess_type(filepath)[0] or 'application/octet-stream'
    dataList.append(encode('Content-Type: {}'.format(fileType)))
    dataList.append(encode(''))

    with open(filepath, 'rb') as f:
        dataList.append(f.read())
    dataList.append(encode('--' + boundary + '--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'null',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Authorization': token,
        'appName': 'live',
        'versionName': 'gdsg',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/admin/upload/uploadFile", payload, headers)
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
    print(data)
    msg = response_obj["msg"]
    statusCode = response_obj["statusCode"]

    if msg == "成功" and statusCode == 0:
        print("上傳成功")
    else:
        print("上傳失敗")



