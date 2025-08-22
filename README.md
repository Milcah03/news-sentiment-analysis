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

│── .env # Environment variables 

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

 <img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/55a4ac44-6fa4-46fb-bf55-b7a879f854a4" />
 

---


