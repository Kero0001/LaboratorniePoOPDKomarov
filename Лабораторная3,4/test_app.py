import unittest
from app import app


class FlaskTest(unittest.TestCase):

    def setUp(self):
        """
        Создание тестового клиента
        """
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_get(self):
        """
        Проверка открытия главной страницы
        """
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Конвертор курсов валют".encode("utf-8"),
            response.data
        )

    def test_usd_to_rub(self):
        """
        Проверка конвертации USD -> RUB
        """
        response = self.client.post(
            '/',
            data={
                'amount': '10',
                'from_currency': 'USD',
                'to_currency': 'RUB'
            }
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b'10.0 USD = 900.0 RUB',
            response.data
        )

    def test_rub_to_usd(self):
        """
        Проверка конвертации RUB -> USD
        """
        response = self.client.post(
            '/',
            data={
                'amount': '180',
                'from_currency': 'RUB',
                'to_currency': 'USD'
            }
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b'180.0 RUB = 2.0 USD',
            response.data
        )

    def test_eur_to_kzt(self):
        """
        Проверка конвертации EUR -> KZT
        """
        response = self.client.post(
            '/',
            data={
                'amount': '2',
                'from_currency': 'EUR',
                'to_currency': 'KZT'
            }
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b'2.0 EUR = 980.0 KZT',
            response.data
        )

    def test_invalid_amount(self):
        """
        Проверка неправильного ввода
        """
        response = self.client.post(
            '/',
            data={
                'amount': 'abc',
                'from_currency': 'USD',
                'to_currency': 'RUB'
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_index_route(self):
        """
        Проверка маршрута /index
        """
        response = self.client.get('/index')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
