
from django.http import HttpResponse
from django.urls import path

from question import views


urlpatterns = [
    path('question', views.question),
    path('', views.home),
    path('answer', views.answer),
    path('about', views.about),
    path('contact', views.contact),
]
