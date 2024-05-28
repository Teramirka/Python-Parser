from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# Вход на сайт
work = Session()
work.get("https://quotes.toscrape.com/", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)       # Вход в панель логин
soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")                                # Забираем токен
data = {"csrf_token": token, "username": "root", "password": "PASSWORD"}            # Форма для логина
result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

soup = BeautifulSoup(result.text, "lxml")                                   # Обновляем soup с новым ответом после логина
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
print(f"Initial quotes: {quotes}")
print(f"Initial authors: {authors}")

def url_addr():
    x = 1
    while True:
        yield f"https://quotes.toscrape.com/page/{x}"
        x += 1

def array():
    if len(quotes) != 0:
        for web_url in url_addr():
            print(f"Fetching URL: {web_url}")
            response = work.get(web_url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            data = soup.find_all("div", class_="quote")

            if not data:
                print("No more quotes found on the page.")
                break

            for quote_block in data:
                quote = quote_block.find("span", class_="text").text
                author = quote_block.find("small", class_="author").text
                authbio = "https://quotes.toscrape.com" + quote_block.find("a")["href"]

                yield quote, author, authbio
                sleep(1)

    else:
        print("No quotes found")