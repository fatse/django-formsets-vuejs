from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author/', views.author_books_formset, name='author'),
]
