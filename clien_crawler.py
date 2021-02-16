import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "Shoose.settings")
import django

django.setup()

from main.models import Post

def Nike_data():
    result = []
    url = 'https://www.nike.com/kr/launch/?type=upcoming&activeDate=date-filter:AFTER'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    response = requests.get(url, headers=header)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    for i in range(1,30):
        title = soup.select_one(f'body > section > section > section > div.category-max-width > div > ul > li:nth-child({i}) > a > div.info-sect > div.text-box > p.txt-description')
        try:
            title = title.text
            month = soup.select_one(f'body > section > section > section > div.category-max-width > div > ul > li:nth-child({i}) > a > div.img-sect > div > span.month').text
            day = soup.select_one(f'body > section > section > section > div.category-max-width > div > ul > li:nth-child({i}) > a > div.img-sect > div > span.day').text
            date = month + day + '일'
            date_int = month.replace('월','') + day

            image = str(soup.select_one(f'body > section > section > section > div.category-max-width > div > ul > li:nth-child({i}) > a > div.img-sect > img')).split('data-src="')[1].split('?snkrBrowse"/>')[0]

            item_obj = {
                'brand' : 'Nike',
                'title': title,
                'date' : date,
                'date_int' : int(date_int),
                'image' : image
            }
            result.append(item_obj)
            print(result)
        except AttributeError:
            pass
    return result


if __name__ =='__main__':
    data = Nike_data()
    for item in data:
        Post(
            brand = 'Nike',
            title = item['title'],
            date = item['date'],
            date_int = item['date_int'],
            image = item['image']
        ).save()

def Converse_data():
    result = []

    url = 'https://www.converse.co.kr/category/launch-calendar?pageSize=200&type=upcoming&activeDate=date-filter:AFTER'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    response = requests.get(url, headers=header)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    for i in range(10):

        try:
            image = str(soup.select_one(f'#limited-edition-list > div.list-content-container > div > div:nth-child({i}) > div.product-tile.ratio-standard > a > div > img')).split('src="')[1].split("?browse")[0]
            title = soup.select_one(f'#limited-edition-list > div.list-content-container > div > div:nth-child({i}) > div.product-tile-details > p.name > a').text
            day = soup.select_one(f'#limited-edition-list > div.list-content-container > div > div:nth-child({i}) > div.product-tile.ratio-standard > div.product-badge-date.pointer-none.flex.flex-direction-col.flex-justify-between > div.day').text
            month = soup.select_one(f'#limited-edition-list > div.list-content-container > div > div:nth-child({i}) > div.product-tile.ratio-standard > div.product-badge-date.pointer-none.flex.flex-direction-col.flex-justify-between > div.month').text
            date = month+'월' + day+'일'
            date_int = month + day
            item_obj = {
                'brand': 'Converse',
                'title': title,
                'date': date,
                'date_int' : int(date_int),
                'image': image
            }
            result.append(item_obj)
            print(result)

        except:
            pass
    return result

if __name__ =='__main__':
    data = Converse_data()
    for item in data:
        Post(
            brand = 'Converse',
            title = item['title'],
            date = item['date'],
            date_int=item['date_int'],
            image = item['image']
        ).save()