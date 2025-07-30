import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

def main():
    now = datetime.now()
    formatted_date = now.strftime('%H:%M %d-%m-%Y')
    investments = {
        'sp500': {
            'bought_value': -INSERT VALUE HERE-,
            'stocks_bought': -INSERT NUMBER HERE-,
            'link':'https://finance.yahoo.com/quote/SXR8.DE/',
        },
        'world': {
            'bought_value': -INSERT VALUE HERE-,
            'stocks_bought': -INSERT NUMBER HERE-,
            'link': 'https://finance.yahoo.com/quote/IWDA.AS/',
        },
    }

    cookie = {
        'A1S': 'IMPORT COOKIE',
        'A1': 'IMPORT COOKIE',
        'A3': 'IMPORT COOKIE',
        'cmp': 'IMPORT COOKIE',
        'EuConsent': 'IMPORT COOKIE',
        'GUCS': 'IMPORT COOKIE',
        'GUC': 'IMPORT COOKIE',
        'PRF': 'IMPORT COOKIE',
    }

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/115.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }

    values = {}

    for investment in investments:
         temp_html = requests.get(investments[investment]['link'], headers = header, cookies = cookie).text
         temp_soup = bs(temp_html, 'html.parser')
         values[investment] = temp_soup.find('span', class_ = 'yf-ipw1h0 base').text

    profits = []

    for investment in investments:
        profits.append((float(values[investment]) - float(investments[investment]['bought_value'])) * int(investments[investment]['stocks_bought']) )
    file = open('Stocks_file', 'a')
    print(f"The profits are: {sum(profits)}")
    file.write(f"\n{formatted_date}\t {sum(profits)}")
    file.close()

main()