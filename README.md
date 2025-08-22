# 📰 News Sentiment Analysis Pipeline  

This project automates the process of fetching news articles, analyzing sentiment, and storing results in **Snowflake** for visualization.  

---

## 📌 Project Overview  
The pipeline:  
1. Fetches news articles from **GNews API** across multiple categories.  
2. Performs **sentiment analysis** using a pre-trained NLP model.  
3. Loads structured data into **Snowflake**.  
4. Visualizes insights with **Snowflake Dashboard**.  

---

## 📂 Project Structure  

news-sentiment-analysis/
│── dags/ # Airflow DAGs
│── scripts/ # Python scripts (fetch, sentiment, load)
│── requirements.txt # Dependencies
│── .env # Environment variables (not committed)
│── README.md # Project documentation


---

## ⚙️ Tech Stack  

- **Apache Airflow** → Workflow orchestration  
- **GNews API** → Data source  
- **Python** → Data processing & sentiment analysis  
- **Snowflake** → Data warehouse & dashboard visualization  
- **WSL (Linux)** → Development environment  
- **Git + GitHub** → Version control  

---

## 🏗️ Architecture Diagram  

![Architecture](https://chatgpt.com/s/m_68a860bd4b688191977228004bb90187)  

---

