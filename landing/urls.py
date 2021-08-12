from django.urls import path
from django.urls.resolvers import URLPattern
from landing.views import Index

urlpatterns =[
    path('', Index.as_view(), name='index')
]