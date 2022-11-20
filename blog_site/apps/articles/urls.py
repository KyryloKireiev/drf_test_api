from django.urls import path
from .views import ArticleAPIView, TestAPIView, ArticleUpdateAPIView, ArticleCRUDAPIView, GetArticlesNames, GetManyColumns

app_name = "articles"

urlpatterns = [
    path("articles_list/", ArticleAPIView.as_view(), name="articles_list"),
    path("test/", TestAPIView.as_view(), name="test"),
    path("test/<int:pk>/", TestAPIView.as_view(), name="update"),
    path("articles_list/update/<int:pk>/", ArticleUpdateAPIView.as_view(), name="update"),
    path("articles_crud/<int:pk>/", ArticleCRUDAPIView.as_view(), name="article_crud"),
    path("articles_titles/", GetArticlesNames.as_view(), name="articles_names"),
    path("articles_columns/", GetManyColumns.as_view(), name="many_columns"),
]
