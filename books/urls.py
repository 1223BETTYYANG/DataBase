from django.urls import re_path as url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^art_music_list/$', views.art_music_list),
    url(r'^science_engineering_list/$', views.science_engineering_list),
    url(r'^biology_medicine_list/$', views.biology_medicine_list),
    url(r'^financial_business_list/$', views.financial_business_list),
    url(r'^literature_social_list/$', views.literature_social_list),
    url(r'^other_list/$', views.other_list),
    url(r'^release_books/$', views.release_books),
    url(r'^release/$', views.release),
    url(r'^books_details/$', views.books_details),
    url(r'^after_search/$', views.after_search),
    url(r'^book_expensive/$', views.book_expensive),
]
