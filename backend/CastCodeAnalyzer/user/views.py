from rest_framework.generic import ListAPIView, RetrieveAPIView

from .models import User
from .serializers import UserSerializers

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializers

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializers