from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Book
from .utils import scrape_books
import json

def home(request):
    scrape_books()
    books = Book.objects.all()

    avg_price = books.aggregate(Avg('price'))['price__avg']
    rating_count = books.values('rating').annotate(count=Count('rating'))

    # Siapkan data chart
    rating_labels = [r['rating'] for r in rating_count]
    rating_values = [r['count'] for r in rating_count]

    return render(request, 'books/home.html', {
        'books': books,
        'avg_price': avg_price,
        'rating_count': rating_count,
        'rating_labels': json.dumps(rating_labels),
        'rating_values': json.dumps(rating_values),
    })
