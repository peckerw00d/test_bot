from typing import List, Tuple

import requests
from lxml import html

def element_by_xpath(url: str, xpath: str):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    element = tree.xpath(xpath)

    if element:
        price = element[0].text_content().strip()
        return int("".join(filter(str.isdigit, price)))

    else:
        print(f"Элемент по пути: {xpath} не найден.")


def average_price(data: List[Tuple]):
    price_list = []

    for row in data:
        price = element_by_xpath(row[1], row[2])
        if price:
            price_list.append(price)

    return sum(price_list) / len(price_list)