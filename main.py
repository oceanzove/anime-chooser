from os import system
from platform import platform

from utils import green, white, red

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

while True:
    system("cls" if platform().startswith("Windows") else "clear")
    # Header
    anime_length = len(anime)

    if len(anime):
        header = (
            f"Запланированно аниме: {anime_length}"
        )

    print(header)

    for i, name in enumerate([
        "Выбрать рандомное аниме",
        "Удалить последнее занятие",
        "Изменить время последнего занятия",
        "Добавить подпись к последнему занятию"
    ]):
        print(f"{green}{'edci'[i]}{white}: {name}")

    print()

    # Gain input
    session_id = input("\nВвод: ")
    if session_id.isdigit():
        session_id = int(session_id)
    elif session_id in ('e', 'd', 'c', 'i'):
        session_id = "edci".index(session_id) + 1
    else:
        session_id = 0


    if session_id == 1:
        print("Рандомное аниме:")

        random_index = random.randint(0, n)
        info = anime[int(random_index)]

        a_url_anime = info.find('a', class_='tooltipped')
        url_anime = a_url_anime['href']
        url = "https://shikimori.one" + url_anime
        link_text = "Ссылка на аниме"
        print(f"{link_text}: {url}")

        response = get(url, headers=headers)
        html_soup = BeautifulSoup(response.text, 'html.parser')

        anime_block = html_soup.find("div", class_="block")

        index = info.find('td', class_='index').text
        name = info.find('span', {"class": "name-ru"}).text
        print(index, ' ', name)
        input(f"\n{red}Действие отменено{white}")