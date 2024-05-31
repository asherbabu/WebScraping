from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

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

@app.route('/')
def home():
    articles = scrape_news()
    return render_template('home.html', articles=articles)

@app.route('/article')
def article():
    article_url = request.args.get('url')
    content = scrape_article_content(article_url)
    return render_template('article.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
