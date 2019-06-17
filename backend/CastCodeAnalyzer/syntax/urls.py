from django.urls import path

from .views import SyntaxListView, SyntaxDetailView

urlpatterns = [
    path('', SyntaxListView.as_view()),
    path('<pk>', SyntaxDetailView.as_view())
]
