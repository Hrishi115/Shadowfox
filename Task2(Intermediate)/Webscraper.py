import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
base_url = "https://books.toscrape.com/"

# Sending HTTP GET request to the website
response = requests.get(base_url)

# Setting the correct encoding to avoid symbol issues (like Â£)
response.encoding = "utf-8"

# Parsing the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# Declaring lists to store scraped book titles and prices
all_titles = []
all_prices = []

# Extracting all required tags which contain data
titles = soup.find_all("h3")
prices = soup.find_all("div", class_="product_price")

# Loop through each title element and extract the 'title' attribute from <a> tag
for title in titles:
    head = title.find("a")["title"]
    all_titles.append(head)

# Loop through each price element and extract the price text
for price in prices:
    cost = price.find("p", class_="price_color").get_text().strip()
    all_prices.append(cost)

# Printing book titles and their corresponding prices
for i, title in enumerate(all_titles):
    print(f"{title} : {all_prices[i]}")