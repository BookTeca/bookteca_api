from django.urls import path
from books.views import BookFollowingView, BookView, BookDetailView


urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:book_id>/", BookDetailView.as_view()),
    path("books/<int:book_id>/following/", BookFollowingView.as_view())
]