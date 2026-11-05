from django.shortcuts import render

from apps.models import Book


def home_view(request):
    return render(request, 'home.html')


def book_list_view(request):
    books = Book.objects.order_by('name')
    return render(request, 'book_list.html', {'books': books})