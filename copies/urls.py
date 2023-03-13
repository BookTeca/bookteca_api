from django.urls import path
from copies.views import CopyListView, CopyDetailView, LoanCreateView, LoanListView, LoanDetailView


urlpatterns = [
    path("books/<int:book_id>/copies/", CopyListView.as_view()),
    path("copies/<int:copy_id>/", CopyDetailView.as_view()),
    path("loans/books/<int:book_id>/", LoanCreateView.as_view()),
    path("loans/users/<int:user_id>/", LoanListView.as_view()),
    path("loans/<int:loan_id>/", LoanDetailView.as_view())

]
