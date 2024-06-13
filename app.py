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
    # content = '\n'.join([p.text for p in paragraphs])
    specific_class = 'post-author-bio'  # Replace with the class you want to remove
    for div in soup.find_all('div', class_=specific_class):
        div.decompose()

    specific_class_form = 'comment-form'  # Replace with the class you want to remove
    for form in soup.find_all('form', class_=specific_class_form):
        form.decompose()

    heading = soup.find('h1').text
    content = [p.text for p in paragraphs]

    return heading, content

@app.route('/')
def home():
    articles = scrape_news()
    return render_template('home.html', articles=articles)

@app.route('/article')
def article():
    article_url = request.args.get('url')
    heading, content = scrape_article_content(article_url)
    return render_template('article.html', heading=heading, content=content)

if __name__ == '__main__':
    app.run(debug=True)
