import requests
from bs4 import BeautifulSoup

url = 'https://etechsc.com/'
response = requests.get(url)

# Parse the content
soup = BeautifulSoup(response.text, 'html.parser') 

# Example: extract all headingsl
headings = soup.find_all('p')
for h in headings:
    print(h.text)

inks = soup.find_all("a", href=True)
for a in inks:
    print(a['href'])
    # Save hrefs to a CSV file
    with open('links.csv', 'a', encoding='utf-8') as f:
        f.write(f"{a['href']}\n")
