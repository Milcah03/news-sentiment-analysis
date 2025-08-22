import os
import sys
import json
import hashlib
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()


def generate_article_id(url, published_at):
    """Generate a unique ID for each article using MD5 hash."""
    raw = f"{url}_{published_at}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def load_to_snowflake(articles):
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )
    cur = conn.cursor()

    # Create table with article_id as primary key
    cur.execute("""
        CREATE TABLE IF NOT EXISTS NEWS_DB.PUBLIC.news_articles (
            article_id STRING PRIMARY KEY,
            title STRING,
            description STRING,
            url STRING,
            published_at TIMESTAMP,
            category STRING,
            sentiment_label STRING,
            sentiment_score FLOAT
        )
    """)

    for article in articles:
        article_id = generate_article_id(article.get("url"), article.get("publishedAt"))

        # Use MERGE to avoid duplicates
        cur.execute("""
            MERGE INTO NEWS_DB.PUBLIC.news_articles AS target
            USING (SELECT %s AS article_id, %s AS title, %s AS description,
                          %s AS url, %s AS published_at, %s AS category,
                          %s AS sentiment_label, %s AS sentiment_score) AS source
            ON target.article_id = source.article_id
            WHEN MATCHED THEN UPDATE SET
                target.sentiment_label = source.sentiment_label,
                target.sentiment_score = source.sentiment_score
            WHEN NOT MATCHED THEN INSERT (
                article_id, title, description, url, published_at, category, sentiment_label, sentiment_score
            ) VALUES (
                source.article_id, source.title, source.description, source.url, source.published_at,
                source.category, source.sentiment_label, source.sentiment_score
            )
        """, (
            article_id,
            article.get("title"),
            article.get("description"),
            article.get("url"),
            article.get("publishedAt"),
            article.get("category"),
            article.get("sentiment_label"),
            article.get("sentiment_score"),
        ))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    articles_file = sys.argv[1]
    if os.path.exists(articles_file):
        with open(articles_file, "r") as f:
            articles = json.load(f)
        load_to_snowflake(articles)
        print(f"Loaded {len(articles)} articles to Snowflake ✅")
    else:
        print(f"No articles file found at {articles_file} ❌")
