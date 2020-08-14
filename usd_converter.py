import requests


class Converter:

    def __init__(self, url, user_value: float):
        self.url = url
        self.user_value = user_value
        self.raw_exchange = {}
        self.exchange_values = {}

    def connect(self):
        """
        Method is defined to connect to API and get all avaliable exchange values
        It returns dict with all avaliable exchange courses
        """
        try:
            get_raw = requests.get(self.url)
            status_code = get_raw.status_code
        except requests.exceptions.ConnectionError:
            status_code = 666
        if status_code != 200:
            message = 'Please check URL - {} status code is returned'.format(status_code)
            raise ConnectionError(message)
        self.raw_exchange = get_raw.json()
        return self.raw_exchange

    def parse_exchanges(self):
        """
        Method is defined to parse USD and EUR values from raw_exchange values
        It returns dict with current USD and EUR courses, like this {'USD' : 61.16, 'EUR' : 70.07}
        """
        for key, value in self.raw_exchange['Valute'].items():
            if key == 'USD':
                self.exchange_values['USD'] = value['Value']
            elif key == 'EUR':
                self.exchange_values['EUR'] = value['Value']
        return self.exchange_values


if __name__ == "__main__":

    url = r'https://www.cbr-xml-daily.ru/daily_json.js'
    user_input = ''
    while type(user_input) != float:
        try:
            user_input = float(input('Введите сумму (десятичную часть введите через точку, например - 42.6): '))
        except ValueError:
            print('Некорректный ввод! Попробуйте ещё раз. ')
    converter = Converter(url, user_input)
    converter.connect()
    converted_value = user_input * converter.parse_exchanges()['USD']

    print('\n{0} USD = {1} RUB'.format(user_input, round(converted_value, 2)))
    input('\nДля выхода нажмите Enter')
