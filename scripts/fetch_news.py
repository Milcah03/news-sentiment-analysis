import os
import requests
import sys
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")
BASE_URL = "https://gnews.io/api/v4/top-headlines"

CATEGORIES = ["politics", "business", "technology", "science", "health"]

def fetch_news(category):
    params = {"token": API_KEY, "lang": "en", "topic": category, "max": 10}
    response = requests.get(BASE_URL, params=params)
    return response.json().get("articles", [])

def get_all_articles():
    """Fetch news from all categories and return as a single list"""
    all_articles = []
    for category in CATEGORIES:
        articles = fetch_news(category)
        for article in articles:
            article["category"] = category  # <-- attach the category
            all_articles.append(article)
    return all_articles

if __name__ == "__main__":
    output_file = sys.argv[1]  # get path from command line
    articles = get_all_articles()
    print(f"Fetched {len(articles)} articles across all categories")
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(articles, f)
    print(f"Saved articles to {output_file}")
