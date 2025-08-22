from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os


DATA_DIR = "/home/milkah/airflow_data"
os.makedirs(DATA_DIR, exist_ok=True) 

PYTHON_PATH = "/mnt/c/Users/Administrator/news/airflow-venv/bin/python"
SCRIPTS_DIR = "/mnt/c/Users/Administrator/news/scripts"

default_args = {
    "owner": "milcah",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "news_pipeline",
    default_args=default_args,
    description="Fetch, analyze and load news data",
    schedule="0 8,20 * * *",
    start_date=datetime(2025, 8, 20),
    catchup=False,
    tags=["news", "pipeline"],
) as dag:

    fetch_news_task = BashOperator(
        task_id="fetch_news",
        bash_command=f"{PYTHON_PATH} {SCRIPTS_DIR}/fetch_news.py {DATA_DIR}/fetched_articles.json",
    )

    sentiment_analysis_task = BashOperator(
        task_id="sentiment_analysis",
        bash_command=f"{PYTHON_PATH} {SCRIPTS_DIR}/sentiment_analysis.py {DATA_DIR}/fetched_articles.json {DATA_DIR}/processed_articles.json",
    )

    load_task = BashOperator(
        task_id="load_data",
        bash_command=f"{PYTHON_PATH} {SCRIPTS_DIR}/load.py {DATA_DIR}/processed_articles.json",
    )

    # Task dependencies
    fetch_news_task >> sentiment_analysis_task >> load_task
