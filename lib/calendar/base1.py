"""
This shows how to scrape information from static
webpages using BeautifulSoup (specifically, bs4).
"""

from bs4 import BeautifulSoup
import requests


req = requests.get(
    "http://www.pyclass.com/example.html",
    headers={
        'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }
)

html = req.content
# print(html)

soup = BeautifulSoup(html, features="html.parser")
# print(soup.prettify())

divs = soup.find_all("div", {"class": "cities"})
# print(type(divs))
print(divs)

for div in divs:
    city_name = div.find("h2")
    # print(type(city_name), city_name)
    print(city_name.string)
    city_desc = div.find("p")
    # print(type(city_desc), city_desc)
    print(city_desc.string)
