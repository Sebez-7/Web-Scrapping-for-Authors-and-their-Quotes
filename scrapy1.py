import requests
from bs4 import BeautifulSoup

# Step 1: Send GET request
url = 'http://quotes.toscrape.com'
response = requests.get(url)
x= requests.get('http://quotes.toscrape.com')

# Step 2: Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract quotes and authors
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(f'{text} - {author}')
