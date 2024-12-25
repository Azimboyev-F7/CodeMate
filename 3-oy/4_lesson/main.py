# Fibonoci
# def fibonacci(n):
#     if n <= 0:
#         return "Fibonacci sonlari faqat musbat bo'lishi kerak!"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#
#     prev, curr = 0, 1
#     for _ in range(2, n):
#         prev, curr = curr, prev + curr
#     return curr
#
# print(fibonacci(2))
import json
import pandas as pd

import requests

url = 'https://dummyjson.com/users/1'

response = requests.get(url)

if response.status_code == 200:
    dictionary = response.json()
    # print(dictionary)
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")


df = pd.DataFrame(dictionary)
df.to_excel("11112.xlsx", index=False)
print("Ma'lumotlar muvaffaqiyatli Excel fayliga saqlandi!")