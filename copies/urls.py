from django.urls import path
from copies.views import CopyView, CopyDetailView, BorrowingsView, BorrowingsDetailView


urlpatterns = [
    path("books/<int:book_id>/copies/", CopyView.as_view()),
    path("copies/<int:copy_id>/", CopyDetailView.as_view()),
    path("borrowings/", BorrowingsView.as_view()),
    path("borrowings/<int:borrowing_id>/", BorrowingsDetailView.as_view())

]
