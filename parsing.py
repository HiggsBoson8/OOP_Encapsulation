import requests
from bs4 import BeautifulSoup

URL = "https://ifin.kz/exchange/almaty"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
}

def get_html(URL = URL, HEADERS = HEADERS):
    response = requests.get(url = URL, headers = HEADERS)
    if response.status_code == 200:
        with open("html/index.html", "w") as fh:
            fh.write(str(response.text))
        with open("html/index.html", "r") as fh:
            table = fh.read()
        return table
    return f"Плохой запрос {response.status_code}"

def get_response(response):
    soup = BeautifulSoup(response, "lxml")
    return soup.find("div", class_="view").find("div", class_="list links-list links-list-white").find_all("a", class_="item-content exchange-item external row-high ")


def main():
    responce = get_html()
    soup = get_response(responce)
    
    with open("html/index.html", "w") as fh:
        fh.write(str(soup))
    return soup

print(main())


