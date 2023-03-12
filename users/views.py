from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permission import IsUserOwner


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):

        self.check_object_permissions(self.request, self.request.user)

        if self.request.user.is_superuser:
            return User.objects.all()

        return User.objects.filter(email=self.request.user.email)


class UserDetailView(DestroyAPIView, UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
