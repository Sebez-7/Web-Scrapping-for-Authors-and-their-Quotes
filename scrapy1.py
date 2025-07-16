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
    # Step 4: Instructions to add your code to a new GitHub repository

    # 1. Initialize a git repository in your project folder:
    #    git init

    # 2. Add your code file:
    #    git add scrapy1.py

    # 3. Commit your changes:
    #    git commit -m "Initial commit"

    # 4. Link your local repo to the remote GitHub repo (replace <repo-url> with your repo's URL):
    #    git remote add origin <repo-url>

    # 5. Push your code to GitHub:
    #    git push -u origin main

    # To change the name of your previous GitHub repo:
    # - Go to your repo page on GitHub.
    # - Click "Settings" (top right).
    # - Edit the "Repository name" field and save.
    # - No need to change anything locally unless you want to rename your local folder.

    # To change your GitHub repo from private to public:
    # - Go to your repo page on GitHub.
    # - Click "Settings" (top right).
    # - Scroll down to the "Danger Zone" section.
    # - Click "Change repository visibility".
    # - Select "Public" and confirm.

    # If you get "error: src refspec main does not match any", it means you don't have a branch named 'main'.
    # To fix:
    # 1. Create an initial commit if you haven't:
    #    git add scrapy1.py
    #    git commit -m "Initial commit"
    # 2. Create the 'main' branch:
    #    git branch -M main
    # 3. Push again:
    #    git push -u origin main
