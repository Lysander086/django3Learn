from django.urls import path

from .views import EbookListCreateAPIView, ReviewCreateAPIView, ReviewDetailAPIView, EbookDetailsAPIView,  QuoteListCreateView

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="ebook-list"),
    path("quotes/", QuoteListCreateView.as_view(), name="quote-list"),
    path("ebooks/<int:pk>/", EbookDetailsAPIView.as_view(), name="ebook-detail"),
    path("ebooks/<int:ebook_pk>/review", ReviewCreateAPIView.as_view(), name="ebook-review"),
    path("reviews/<int:pk>/", ReviewDetailAPIView.as_view(), name="review-detail"),

]
