import requests
from collections import Counter

url = 'https://www.python.org'


def main(url: str):
    responce = requests.get(url).text
    str_responce = ''.join(responce.split())
    counter = Counter(str_responce)
    with open('readme.md', 'w', encoding='Utf-8') as file:
        file.write(f'## Количество символов в коде страницы {url}:\n')
        for char, count in counter.most_common():
            file.write(f'### Количество символов " {char} " в данной странице - {count}\n')


if __name__ == '__main__':
    main(url)
