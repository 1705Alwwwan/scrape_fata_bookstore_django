from django.contrib import admin
from .models import Book
import csv
import json
from django.http import HttpResponse


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'availability', 'rating']
    actions = ['export_as_csv', 'export_as_json']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=books.csv'

        writer = csv.writer(response)
        writer.writerow(['Title', 'Price', 'Availability', 'Rating', 'Link'])

        for book in queryset:
            writer.writerow([book.title, book.price, book.availability, book.rating, book.link])
        return response

    export_as_csv.short_description = "Export selected books to CSV"

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=books.json'

        data = list(queryset.values('title', 'price', 'availability', 'rating', 'link'))
        response.write(json.dumps(data, indent=2))
        return response

    export_as_json.short_description = "Export selected books to JSON"
