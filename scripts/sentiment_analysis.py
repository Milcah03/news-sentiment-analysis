import json
import sys
from transformers import pipeline

# Load sentiment pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="af0f99b"
)

def analyze_sentiment(text: str):
    result = sentiment_pipeline(text)[0]
    return {"label": result["label"], "score": float(result["score"])}

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as f:
        articles = json.load(f)

    for article in articles:
        content = article.get("description") or article.get("title", "")
        sentiment = analyze_sentiment(content)
        article["sentiment_label"] = sentiment["label"]
        article["sentiment_score"] = sentiment["score"]

    with open(output_file, "w") as f:
        json.dump(articles, f)

    print(f"Processed {len(articles)} articles and saved to {output_file}")
