import aiohttp
from bs4 import BeautifulSoup

from src.dao.lamoda_dao import LamodaItemDAO
from src.config.database import Database


async def parse_lamoda_items(database: Database, url: str, page: int = 1):
    url_on_page = f'{url}?page={page}'

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url_on_page) as response:
            html_content = await response.text()

    soup = BeautifulSoup(html_content, 'html.parser')

    items = soup.find_all('div', class_='x-product-card__card')
    category = soup.find('h1', class_='d-catalog-header__title-text').text.strip()

    data = []

    for item in items:
        data.append({
            'id': item.find('a').get('href').split('/')[2].strip(),
            'brand': item.find('div', class_='x-product-card-description__brand-name').text.strip(),
            'title': item.find('div', class_='x-product-card-description__product-name').text.strip(),
            'category': category,
            'price': item.find('span', class_='x-product-card-description__price-WEB8507_price_no_bold').text.strip()
        })

    lamoda_items_dao = LamodaItemDAO(database)
    lamoda_items_dao.create_or_update(data)
