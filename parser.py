from wsgiref import headers
import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 "
               "Safari/537.36"}

#Downloading the files
def download(url):
    response = requests.get(url, stream=True)
    r = open("D:\\DevOPS\\Python\\Parser\\Image\\" + url.split("/")[-1], "wb")
    for value in response.iter_content(1024*2048):
        r.write(value)
    r.close()

#Taking url for entering the link
def get_url():
    for count in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page=2{count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="w-full rounded border")

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url

#Opening links and getting parser exit values
def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(2)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="my-8 w-full rounded border")

        name = data.find("h3", class_="card-title").text
        price = data.find("h4", class_="my-4 card-price").text
        url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top").get("src")
        description = data.find("p", class_="card-description").text

        download(url_img)
        yield name, price, url_img, description
