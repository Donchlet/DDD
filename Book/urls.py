from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('books/', views.book_all, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path("books/<int:id>/update/", views.put_book_update, name="book_update"),
    path("books/<int:id>/delete/", views.book_delete, name="book_delete"),
    path("add-book/", views.add_book, name="add_book")
]