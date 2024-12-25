# import requests
import pandas as pd

import requests
import json

# questions = input("Salom! Sizga qanday yordam bera olaman? :: ")
# url = "https://chatgpt-42.p.rapidapi.com/chatbotapi"
#
# payload = {
#  "bot_id": "85ca73a9cfmsh764ba42f098f83dp1d9877jsnee1682ad5635",
#  "messages": [
#   {
#    "role": "user",
#    "content": f"{questions}"
#   }
#  ],
#  "user_id": "",
#  "temperature": 0.9,
#  "top_k": 5,
#  "top_p": 0.9,
#  "max_tokens": 256,
#  "model": "gpt 3.5"
# }
# headers = {
#  "x-rapidapi-key": "85ca73a9cfmsh764ba42f098f83dp1d9877jsnee1682ad5635",
#  "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
#  "Content-Type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(json.dumps(response.json()))

# Example 1       <<<<EXCEL TO DICT>>>>
# xls_file = 'D:/PYTHON-BACKEND/1111.xlsx'
#
# df = pd.read_excel(xls_file)
#
# subject = df['Mavzular nomi'].tolist()
#
# print(subject)


# Example of     <<<<DICT TO EXCEL>>>>
# Dictionary ma'lumotlari
# data_dict = [
#     {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
#     {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
#     {'Name': 'Charlie', 'Age': 35, 'City': 'London'}
# ]
#
# # Dictionary-ni DataFrame-ga aylantirish
# df = pd.DataFrame(data_dict)
#
# # DataFrame-ni Excel fayliga saqlash
# df.to_excel('1111.xlsx', index=False)  # 'output.xlsx' ni fayl nomi bilan almashtiring
#
# print("Ma'lumotlar muvaffaqiyatli Excel fayliga saqlandi!")

import requests
user = input("So'zni kiriting ::")
url = "https://google-translate113.p.rapidapi.com/api/v1/translator/html"

payload = {
	"from": "en",
	"to": "uz",
	"html": user
}
headers = {
	"x-rapidapi-key": "85ca73a9cfmsh764ba42f098f83dp1d9877jsnee1682ad5635",
	"x-rapidapi-host": "google-translate113.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())