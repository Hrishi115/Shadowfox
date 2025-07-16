import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/"

response = requests.get(base_url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

all_titles = []
all_prices = []

titles = soup.find_all("h3")
prices = soup.find_all("div", class_="product_price")

for title in titles:
    head = title.find("a")["title"]
    all_titles.append(head)
    # print(f"Title = {head}")
for price in prices:
    cost = price.find("p", class_="price_color").get_text().strip()
    all_prices.append(cost)
    # print(f"Costs= {cost}")

for i,title in enumerate (all_titles):
    print(f"{title} : {all_prices[i]}")