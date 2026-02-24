# 📊 Twitch Real-Time Chat Data Pipeline & Analytics

A robust, asynchronous data ingestion system designed to capture, store, and prepare live streaming data for large-scale analysis. This project serves as a foundational component for a Big Data Analytics suite, bridging the gap between live social interactions and structured data insights.

## 🌟 Project Overview
In the world of Big Data, the first and most critical step is **Data Ingestion**. This tool connects to Twitch's IRC servers via WebSockets to stream live chat data into a local SQLite database. It is built to handle high-velocity message streams, ensuring no data point is lost during peak engagement moments.

## 🚀 Technical Stack
* **Language:** Python 3.12
* **API Framework:** `twitchio` (Asynchronous Python wrapper for Twitch API)
* **Database:** `SQLite` (Lightweight, serverless structured storage)
* **Concurrency:** `asyncio` for non-blocking message processing

## 🛠️ Key Features
* **Real-Time Streaming:** Captures messages, usernames, and precise timestamps as they happen.
* **Automated Schema Management:** Automatically initializes the database and required tables on first run.
* **Developer Experience:** Features a color-coded terminal interface for real-time monitoring of the data flow.
* **Analytics Ready:** The resulting database is structured for immediate use with `pandas`, sentiment analysis models, or visualization tools like `Matplotlib`.

## 📂 Project Structure
```text
Twitch-Chat-Insight/
├── scraper.py        # The core data ingestion engine
└── README.md         # Documentation and project overview


---
**Author:** Muhammed Ali Uzun
**Role:** Big Data Analytics Student & Discord Bot Developer