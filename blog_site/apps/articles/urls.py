from django.urls import path
from .views import ArticleAPIView, TestAPIView

app_name = "articles"

urlpatterns = [
    path("articles_list/", ArticleAPIView.as_view(), name="articles_list"),
    path("test/", TestAPIView.as_view(), name="test"),
    path("test/<int:pk>/", TestAPIView.as_view(), name="update"),
]
