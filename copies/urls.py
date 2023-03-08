from django.urls import path
from copies.views import CopyView, CopieDetailView


urlpatterns = [
    path("books/<int:book_id>/copies/", CopyView.as_view()),
    path("copies/<int:copy_id>/", CopieDetailView.as_view())
]
# borrowings/
# borrowings/<int:borrowing_id>/