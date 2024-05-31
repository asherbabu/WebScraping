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
    # Select <a> tags within <h3> tags that contain the news headings
    for item in soup.find_all('h3'):
        a_tag = item.find('a')
        if a_tag:
            title = a_tag.text.strip()
            link = a_tag['href']
            articles.append({'title': title, 'link': link})
    
    return articles

# Example usage
if __name__ == "__main__":
    news_articles = scrape_news()
    for article in news_articles:
        print(article['title'])
        print(article['link'])
        print()
