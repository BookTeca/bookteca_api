from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, RetrieveDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserCollaborator
from users.permission import IsUserOwnerOrCollaborator
from books.models import Book
from .models import Copy, Loan
from .serializers import CopySerializer, LoanSerializer
from django.shortcuts import get_object_or_404
import ipdb
from users.models import User
from datetime import datetime as dt, timedelta as td
from .api_exceptions import UserBlockedException, BookCopyNotAvailableException, LoanBookAlreadyExistsException


class CopyListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    serializer_class = CopySerializer
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        obj_book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        # Copy.objects.filter(book=obj_book)
        return obj_book.book_copies.all()


class CopyDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    lookup_url_kwarg = "copy_id"

    def perform_destroy(self, instance: Copy):
        if instance.state == "Danificado":
            instance.is_available = False
            instance.book["quantity"] -= 1
            instance.book.save()
            instance.save()


class LoanCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        today = dt.now().date()
        obj_user = get_object_or_404(User, pk=serializer.validated_data["user"])

        if obj_user.is_blocked and obj_user.blocked_until > today:
            return self.raise_uncaught_exception(exc=UserBlockedException())

        obj_book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        if not obj_book.quantity or not obj_book.is_active:
            return self.raise_uncaught_exception(exc=BookCopyNotAvailableException())

        obj_copy_borrow = Copy.objects.filter(is_available=True, book=obj_book).first()
        obj_exists_loan_copy = Loan.objects.filter(copy__book=obj_book, user=obj_user, return_date__isnull=True, estimated_return_date__gte=today).exists()
        
        if obj_exists_loan_copy:
            return self.raise_uncaught_exception(exc=LoanBookAlreadyExistsException())

        return serializer.save(copy=obj_copy_borrow, user=obj_user)


class LoanListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwnerOrCollaborator]

    serializer_class = LoanSerializer

    def get_queryset(self):
        obj_user = get_object_or_404(User, pk=self.kwargs["user_id"])
        today = dt.now().date()
        
        self.check_object_permissions(self.request, obj_user)
        
        return Loan.objects.filter(user=obj_user).select_related('copy').select_related("user")


class LoanDetailView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    lookup_url_kwarg = "loan_id"

    def perform_destroy(self, instance: Loan):
        instance.return_date = dt.now().date()
        instance.copy.is_available = True

        estimated_return_difference = instance.estimated_return_date - instance.loan_date
        current_return_difference = instance.estimated_return_date - instance.return_date

        if current_return_difference.days > estimated_return_difference.days:
            instance.user.is_blocked = True
            if instance.return_date.isoweekday() == 5:
                instance.user.blocked_until = instance.return_date + td(days=3)
            instance.user.blocked_until = instance.return_date + td(days=1)
            instance.user.save()
            instance.save()
