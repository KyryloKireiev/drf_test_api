from django.urls import path, include
from .views import ArticleAPIView, \
    TestAPIView, \
    ArticleUpdateAPIView, \
    ArticleCRUDAPIView, \
    GetArticlesNames, \
    GetManyColumns, \
    ArticleViewSets, \
    ArticleAPIList, \
    ArticleAPIUpdate, \
    ArticleAPIDestroy

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"articles", ArticleViewSets)

app_name = "articles"

urlpatterns = [
    path("articles_list/", ArticleAPIView.as_view(), name="articles_list"),
    path("test/", TestAPIView.as_view(), name="test"),
    path("test/<int:pk>/", TestAPIView.as_view(), name="update"),
    path("articles_list/update/<int:pk>/", ArticleUpdateAPIView.as_view(), name="update"),
    path("articles_crud/<int:pk>/", ArticleCRUDAPIView.as_view(), name="article_crud"),
    path("articles_titles/", GetArticlesNames.as_view(), name="articles_names"),
    path("articles_columns/", GetManyColumns.as_view(), name="many_columns"),

    path("articles_view_sets/", ArticleViewSets.as_view({"get": "list"})),
    path("articles_view_sets/<int:pk>/", ArticleViewSets.as_view({"put": "update"})),

    path("", include(router.urls), name="article "),

    path("articles_api_list/", ArticleAPIList.as_view(), name="articles_api_list"),
    path("articles_api_update/<int:pk>/", ArticleAPIUpdate.as_view(), name="articles_api_update"),
    path("articles_api_destroy/<int:pk>/", ArticleAPIDestroy.as_view(), name="articles_api_destroy"),
]
