from django.urls import path

from .views import UrlsDetail, UrlsView


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', UrlsView.as_view()),
    path('<short_url>/', UrlsDetail.as_view()),
]
