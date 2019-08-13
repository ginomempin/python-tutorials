"""
This shows how to scrape information from the
https://www.century21.com/ website (cached in
www.pyclass.com/real-estate/rock-springs-wy).

In the future, this should be replaced by a
static website that displays the holidays for
a year.
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests


def parse_page(url):
    req = requests.get(
        url,
        headers={
            'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
    )

    html = req.content
    # print(html)

    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())

    return soup


def parse_properties_on_page(page):
    divs = page.find_all("div", {"class": "propertyRow"})
    # print(len(divs))

    properties_on_page = []
    for div in divs:
        prop = {}

        price = div.find("h4", {"class": "propPrice"})
        price = price.text.strip()
        prop["price"] = price

        addrs = div.find_all("span", {"class": "propAddressCollapse"})
        addrs = [addr.text.strip() for addr in addrs]
        addr = " ".join(addrs)
        prop["addr"] = addr

        beds = div.find("span", {"class": "infoBed"})
        if beds is not None:
            beds = int(beds.find("b").text.strip())
        prop["beds"] = beds

        baths = div.find("span", {"class": "infoValueFullBath"})
        if baths is not None:
            baths = int(baths.find("b").text.strip())
        prop["baths"] = baths

        area = div.find("span", {"class": "infoSqFt"})
        if area is not None:
            area = area.find("b").text.strip() + "Sq. Ft"
        prop["area"] = area

        features = div.find("div", {"class": "propertyFeatures"})
        feature_groups = features.find_all("div", {"class": "columnGroup"})
        for fg in feature_groups:
            name = fg.find("span", {"class": "featureGroup"})
            if name is None:
                continue
            name = name.text.strip()
            if "Lot Size:" in name:
                lot_size = fg.find("span", {"class": "featureName"})
                lot_size = lot_size.text.strip()
                break
        else:
            lot_size = None
        prop["lot_size"] = lot_size

        # print(prop)
        properties_on_page.append(prop)

    print(f"Found {len(properties_on_page)} properties!")
    return properties_on_page

BASE_URL = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"

base_page = parse_page(BASE_URL)
paginator = base_page.find("span", {"class": "PageNumbers"})
# print(paginator.prettify())

page_links = paginator.find_all("a", {"class": "Page"})
last_page = int(page_links[-1].text.strip())
# print(last_page)

PAGINATED_URL = BASE_URL + "#t=0&s="
all_properties = []
for page_num in range(0, (last_page * 10), 10):
    page_url = PAGINATED_URL + str(page_num)
    print(page_url)
    curr_page = parse_page(page_url)
    all_properties.extend(parse_properties_on_page(curr_page))

print(f"Found total of {len(all_properties)} properties!")

df = pd.DataFrame(all_properties)
print(df)

df.to_csv("properties.csv")
