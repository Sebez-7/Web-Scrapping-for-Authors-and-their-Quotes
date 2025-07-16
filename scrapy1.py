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
    # Step 4: Instructions to push this project to GitHub

    # 1. Initialize a git repository in your project folder:
    #    Open terminal/cmd, navigate to your project directory, and run:
    #    git init

    # 2. Add your file(s) to the repository:
    #    git add scrapy1.py

    # 3. Commit your changes:
    #    git commit -m "Initial commit"

    # 4. Create a new repository on GitHub (via the website).

    # 5. Link your local repo to GitHub:
    #    git remote add origin https://github.com/your-username/your-repo-name.git

    # 6. Push your code:
    #    git push -u origin master