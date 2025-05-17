import requests
from bs4 import BeautifulSoup
from .models import Book
import re

def scrape_books():
    url = 'http://books.toscrape.com/catalogue/page-1.html'
    response = requests.get(url)
    response.encoding = 'utf-8'  # pastikan encoding benar
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.select('article.product_pod'):
        try:
            title = book.h3.a['title']

            # ambil dan bersihkan harga
            price_raw = book.select_one('.price_color').text
            price_clean = re.sub(r'[^\d.]', '', price_raw)  # hapus semua kecuali angka & titik
            price = float(price_clean)

            availability = book.select_one('.availability').text.strip()
            rating = book.p['class'][1]
            link = "http://books.toscrape.com/catalogue/" + book.h3.a['href']

            Book.objects.update_or_create(
                title=title,
                defaults={
                    'price': price,
                    'availability': availability,
                    'rating': rating,
                    'link': link
                }
            )
        except Exception as e:
            print(f"[ERROR] Gagal scrape 1 buku: {e}")
