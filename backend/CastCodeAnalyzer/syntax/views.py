from rest_framework.generice import ListAPIView, RetrieveAPIView

from .models import Syntax
from .serializers import SyntaxSerializers

class SyntaxListView(ListAPIView):
    queryset = Syntax.objects.all()
    serializers_class = SyntaxSerializers

class SyntaxDetailView(RetrieveAPIView):
    queryset = Syntax.objects.all()
    serializers_class = SyntaxSerializers