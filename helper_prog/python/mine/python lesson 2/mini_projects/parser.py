# import requests
# import json
# import time
# import random
# from bs4 import BeautifulSoup as bs

from telepot import Bot
bot = Bot(token="6032965732:AAHfwCFNYXl0pAvEUy8tgWcYFAzRRXRtTDw")

g_id = 1621522181

i = 0
while True:
    i += 1
    bot.sendMessage(g_id , f"qale{i}")
    print(i)
# Joker parsing from latifa.uz


# jokes = {}

# url = f"https://maqollar.uz/"
# ten_jokes = {}
# HEADER = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
# page = requests.get(url=url, headers=HEADER)
# soup = bs(page.text, "html.parser")
# divs = soup.findAll("h2", class_="proverb-uzbek h4 font-weight-normal m-0")   
# ind = 0
# for i in divs:
#     ind += 1
#     text = i.text.replace("\n", "").replace("\\", "").replace('\"', '"').replace("\r", "")
#     ten_jokes.update({f"{ind}":text})
#     print(i)
# jokes.update(ten_jokes)

# with open("parser.json", "w+", encoding="utf-8") as file:
#     file.write(json.dumps(jokes,ensure_ascii=False))