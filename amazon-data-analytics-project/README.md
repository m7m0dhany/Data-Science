# Amazon Sales Data Analytics Project

A data analytics project built for the CodeAlpha internship task list, covering four core data analytics skills: web scraping, exploratory data analysis, data visualization, and sentiment analysis.

## 📋 Overview

This project is built around the **Amazon Sales Dataset** (1,465 products with pricing, ratings, and customer reviews), with an additional standalone web scraping module demonstrating data collection from a live website.

## ✅ Tasks Completed

### 1. Web Scraping
- Built a custom 100-record dataset by scraping [books.toscrape.com](http://books.toscrape.com) (a public sandbox site for scraping practice)
- Used `requests` + `BeautifulSoup` to parse paginated HTML listings
- Extracted: title, price, star rating, availability, and product URL
- Script: [`scrape_books.py`](./scrape_books.py) · Output: [`scraped_books.csv`](./scraped_books.csv)

### 2. Exploratory Data Analysis (EDA)
- Cleaned raw price/discount/rating fields (currency symbols, commas, invalid values)
- Explored category distribution, rating statistics, and correlations between price, discount, and rating
- Ran a formal hypothesis test (independent-samples t-test) comparing ratings between high-discount and low-discount products

### 3. Data Visualization
- Built 6+ charts with Matplotlib/Seaborn: category distribution, rating distribution, discount vs. rating, rating by category, and a correlation heatmap

### 4. Sentiment Analysis
- Applied VADER (NLTK-based) sentiment scoring to customer review text
- Classified reviews as Positive / Negative / Neutral
- Compared text sentiment against the actual star rating to flag mismatched reviews (e.g. high rating with negative text)

## 🛠️ Tools & Libraries

Python · pandas · NumPy · Matplotlib · Seaborn · BeautifulSoup · requests · VADER Sentiment · SciPy

## 📁 Project Files

| File | Description |
|---|---|
| `amazon_analytics_project.ipynb` | Main notebook — all four tasks, fully executed |
| `amazon_analytics_project.html` | Read-only HTML export of the notebook (view without running code) |
| `amazon.csv` | Source dataset (Amazon Sales Dataset) |
| `scrape_books.py` | Standalone web scraper script |
| `scraped_books.csv` | Dataset produced by the scraper |

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib seaborn beautifulsoup4 requests vaderSentiment scipy
jupyter notebook amazon_analytics_project.ipynb
```

## 📊 Key Findings

- The catalog is dominated by a handful of categories (electronics, accessories, cables); average discount is high (~47%) across products.
- Discount percentage has only a weak negative correlation with rating — heavy discounting is not a strong quality signal in this dataset.
- The large majority of review text is Positive, consistent with generally high star ratings — but a small subset of reviews show a mismatch between text sentiment and numeric rating, a useful signal for flagging reviews worth a closer look.

## 👤 Author

Mahmoud — AI Student, Delta University for Science and Technology
