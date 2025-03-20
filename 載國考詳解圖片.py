import requests

# 目標圖片的 URL
for i in range(3500):
    i=i+1
    url = "https://cougarbot.cc/api/get-image/{}/".format(i)

    # 向伺服器發出 GET 請求
    response = requests.get(url)

    # 檢查請求是否成功
    if response.status_code == 200:
        # 將圖片寫入本地檔案
        with open("圖片/{}.png".format(i), "wb") as f:
            f.write(response.content)
        print("{}圖片下載成功！".format(i))
    else:
        print(f"下載失敗，狀態碼：{response.status_code}")