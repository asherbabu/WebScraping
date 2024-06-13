import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = 'https://www.agribusinessglobal.com/agrochemicals/'
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to access the website")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    for item in soup.find_all('h3'):
        a_tag = item.find('a')
        if a_tag:
            title = a_tag.text.strip()
            link = a_tag['href']
            articles.append({'title': title, 'link': link})
    
    return articles

def scrape_article_content(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to access the article")
        return "Failed to load content"

    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    content = '\n'.join([p.text for p in paragraphs])
    return content
