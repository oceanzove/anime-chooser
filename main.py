from bs4 import BeautifulSoup
from requests import get
import time
import random

url = 'https://shikimori.one/zove/list/anime'
anime = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.3"
}
response = get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')

# Находим заголовок с классом "status-0" - запланированные
header_status_0 = html_soup.find("header", class_="status-0")

# Если заголовок найден, получаем таблицу идущию после него
if header_status_0:
    table = header_status_0.find_next_sibling("table", class_="b-table list-lines")
    # Если таблца найдена получаем все строчки
    if table:
        anime_data = table.find_all('tr', class_="user_rate")
        if anime_data:
            anime.extend(anime_data)
            value = random.random()
            scaled_value = 1 + (value * (9 - 5))
            print(scaled_value)
            time.sleep(scaled_value)
    else:
        print('Таблица не найдена после заголовка status-0')
else:
    print('Заголовок status-0 не найден')

print(len(anime))
print()
n = int(len(anime)) - 1
count = 0
while count <= n:  # count <= n
    info = anime[int(count)]
    index = info.find('td', class_='index').text
    name = info.find('span', {"class": "name-ru"}).text
    print(index, ' ', name)
    count += 1
