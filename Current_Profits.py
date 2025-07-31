import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time

class Investment:
    def __init__(self, name, bought_value, stocks_bought, link):
        self.name = name
        self.bought_value = bought_value
        self.stocks_bought = stocks_bought
        self.link = link

    def add_stocks(self, number_stocks, price):
        self.bought_value = (self.bought_value * self.stocks_bought + price * number_stocks) / (
            number_stocks + self.stocks_bought
        )
        self.stocks_bought += number_stocks

    def remove_stocks(self, number_stocks):
        self.stocks_bought -= number_stocks

sp500 = Investment('sp500', 400, 1, 'https://finance.yahoo.com/quote/IVVB11.SA/)
world = Investment('world', 200, 20, 'https://finance.yahoo.com/quote/VWCE.DE/')
investments = [sp500, world]

def main():
    now = datetime.now()
    formatted_date = now.strftime(f'%H:%M\t%d-%m-%Y')
    cookie = {
        '-INSERT-': '-INSERT COOKIE HERE-',
        '-INSERT-': '-INSERT COOKIE HERE-',
        '-INSERT-': '-INSERT COOKIE HERE-',
        '-INSERT-': '-INSERT COOKIE HERE-',
    }

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/115.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }

    values = {}

    for investment in investments:
         temp_html = requests.get(investment.link, headers = header, cookies = cookie).text
         temp_soup = bs(temp_html, 'html.parser')
         values[investment] = temp_soup.find('div', class_ = 'YMlKec fxKbKc').text
         values[investment] = values[investment].removeprefix('€')
    profits = []

    for investment in investments:
        profits.append((float(values[investment]) - investment.bought_value) * investment.stocks_bought)
    readable_file = open('Stocks_file', 'r').read()

    if datetime.now().strftime('%d-%m-%Y') in readable_file:
        lines = readable_file.split('\n')
        del lines[-1]
        with open('Stocks_file', 'w') as file:
            print("ATTENTION! YOU ALREADY SCANNED TODAY!")
            print(f"The profits are: {sum(profits)}")
            final_text = ''
            for line in lines[:len(lines) - 1]:
                final_text += line + '\n'
            final_text += f'{formatted_date}\t {sum(profits)}\n'
            file.write(final_text)
    else:
        file = open('Stocks_file', 'a')
        print(f"The profits are: {sum(profits)}")
        file.write(f"{formatted_date}\t {sum(profits)}\n")
        file.close()

main()
time.sleep(1.3)
