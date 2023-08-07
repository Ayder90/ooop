from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager import ChromeDriverManager
import time

url = "https://animego.org/anime"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_valid_range=10).install()))
driver.get(url)

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
flag = False
while(flag == False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        flag == True
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
f = open(r"C:\Users\Poisoned\Desktop\ANIME_RND\anime_list.txt", "w", encoding="utf-8")
for anime in soup.find_all("div", class_="col-12"):
    for anime2 in anime.find_all("div", class_="h5 font-weight-normal mb-1"):
        anime_title = anime2.get_text()
        anime_link = anime2.find("a")
        anime_link = anime_link.get("href")
        print(anime_link)
        f.write(f"{anime_title} - {anime_link}\n")
f.close()