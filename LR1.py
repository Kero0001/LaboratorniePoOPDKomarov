import requests
from bs4 import BeautifulSoup

def parse_cars():
    url = 'https://omsk.110km.ru/vybor/kupit-novie-omsk/'

    try:
        response = requests.get(url)
        print(f'Статус код: {response.status_code}')

        if response.status_code != 200:
            print('Не удалось загрузить страницу')
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all("a", class_="sale-prev__header link")[:20]
        prices = soup.find_all("span", class_="sale-prev__price-cost")[:20]
        areas = soup.find_all("p", class_="sale-prev__area")[:20]

        if not titles:
            print("Данные не найдены.")
            return

        with open("new_cars.txt", "w", encoding="utf-8") as file:
            header = "Продажи новых авто в Омске"
            print("\n" + header)
            print("=" * 50)
            file.write(header + "\n")
            file.write("=" * 50 + "\n\n")

            for i, (title, price, area) in enumerate(zip(titles, prices, areas), 1):
                car_title = title.text.strip()
                car_price = price.text.strip()
                car_area = area.text.strip()

                line = (
                    f"{i}. {car_title}\n"
                    f"Цена: {car_price}\n"
                    f"Регион: {car_area}\n"
                    f"{'-' * 50}\n"
                )

                print(line)
                file.write(line)

            print("Результаты сохранены в файл 'new_cars.txt'")

    except requests.exceptions.ConnectionError:
        print("Ошибка подключения.")

if __name__ == "__main__":
    parse_cars()