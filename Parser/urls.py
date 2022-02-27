from django.urls import path
from . import views


app_name = 'parser'
urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name="parser"),
    path('review/', views.FilmListView.as_view(), name="review_list"),
    path('review/<int:id>/', views.FilmsDetailView.as_view(), name="review_detail")
]