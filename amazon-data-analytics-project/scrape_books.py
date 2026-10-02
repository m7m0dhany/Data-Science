"""
Web scraper for books.toscrape.com — a public sandbox site for scraping practice.
Extracts: title, price, star rating, availability, and product URL for every book
across all paginated catalogue pages.

Usage:
    python scrape_books.py
Requires:
    pip install requests beautifulsoup4
"""
import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (educational scraping project)"}

RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def scrape_page(page_num):
    url = BASE_URL.format(page_num)
    response = requests.get(url, headers=HEADERS, timeout=10)
    if response.status_code != 200:
        return None  # signals "no more pages"

    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    page_rows = []
    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", "").strip())

        availability = book.find("p", class_="instock availability").text.strip()

        rating_class = book.find("p", class_="star-rating")["class"]
        rating_word = [c for c in rating_class if c != "star-rating"][0]
        rating = RATING_WORDS.get(rating_word, None)

        relative_link = book.h3.a["href"]
        product_url = "http://books.toscrape.com/catalogue/" + relative_link.replace("../../../", "")

        page_rows.append({
            "title": title,
            "price_gbp": price,
            "rating": rating,
            "availability": availability,
            "product_url": product_url
        })
    return page_rows


def scrape_all_pages(max_pages=50, delay=0.5):
    all_rows = []
    page_num = 1
    while page_num <= max_pages:
        print(f"Scraping page {page_num}...")
        rows = scrape_page(page_num)
        if not rows:
            break
        all_rows.extend(rows)
        page_num += 1
        time.sleep(delay)  # polite delay between requests
    return all_rows


if __name__ == "__main__":
    data = scrape_all_pages()
    with open("all_books.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price_gbp", "rating", "availability", "product_url"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Done. Saved {len(data)} books to all_books.csv")
