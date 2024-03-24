import requests
from bs4 import BeautifulSoup
url = "https://github.com/azizbek0606"
r = requests.get(url)
arr = ""
if r.status_code == 200:
    soup = BeautifulSoup(r.content, "html.parser")
    h2_tag = soup.find("h2", class_="f4 text-normal mb-2")

    if h2_tag:
        print(h2_tag.get_text())
        arr.join(h2_tag.get_text().split())
    else:
        print("Bunday element saxifada mavjud emasa !!!")
else:
    print("Saxifa topilmadi\nInternet aloqasini tekshiring !!!")
print(arr)
