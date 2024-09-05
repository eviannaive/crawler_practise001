from http.client import responses

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.ptt.cc/bbs/Drama-Ticket/index.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

response =  requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")

articles = soup.find_all("div", class_="r-ent")
data_list = []
for d in articles:
    data = {}
    title = d.find("div", class_="title")
    popular = d.find("div", class_="nrec")
    date = d.find("div", class_="date")
    if title and title.a:
        # print(title.a.text)
        data['title'] = title.a.text
    if popular and popular.span:
        # print("人氣"+popular.span.text)
        data['popular'] = popular.span.text
    else:
        data['popular'] = "0"
    if date:
        # print("日期"+date.text)
        data['date'] = date.text
    data_list.append(data)
# print(data_list)

# 儲存成json－－－－－－－
# with open("ptt_ticket.json","w",encoding="utf-8") as file:
#     # json 轉換
#     json.dump(data_list, file, ensure_ascii=False, indent=4)
# print('資料已成功儲存成json')

# 轉成excel－－－－－－－
df = pd.DataFrame(data_list)
df.to_excel("ptt_ticket.xlsx", index=False, engine="openpyxl")


# 基本獲取網頁
# if response.status_code == 200:
#     with open('output.html','w',encoding='utf-8') as f:
#         f.write(response.text)
#     print('寫入成功')
# else:
#     print('寫入失敗')