from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Article, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import ArticleSerializer, ArticleTestSerializer
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .pagination import MyCursorPagination


class ArticleAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TestAPIView(APIView):

    def get(self, request):
        obj = Article.objects.all()
        return Response({"posts": ArticleTestSerializer(obj, many=True).data})

    def post(self, request):
        serializer = ArticleTestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # new_post = Article.objects.create(
        #     title=request.data["title"],
        #     content=request.data["content"],
        #     cat_id=request.data["cat_id"]
        # )
        return Response({"new_post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put not allowed"})

        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = ArticleTestSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"update_post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method delete not allowed"})

        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        instance.delete()
        return Response({"delete": "post" + str(pk)})


class GetArticlesNames(APIView):

    def get(self, request):
        instance = Article.objects.values("title")
        return Response({"titles": list(instance)})


class GetManyColumns(APIView):

    def get(self, request):
        columns = Article.objects.values("id", "title", "cat")
        for elem in columns:
            number_of_cat = elem["cat"]
            cat = Category.objects.get(id=number_of_cat).name
            elem["cat"] = cat
        return Response({"id, title, category": columns})


class ArticleViewSets(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=["get"], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({"categories": [c.name for c in cats]})


class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    permission_classes = (IsAuthenticated, )
    pagination_class = MyCursorPagination


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )


class ArticleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )


@api_view(["GET", ])
def my_view(request):
    elements_per_page = 3
    start_idx = int(request.query_params.get("start", 1))
    articles = Article.objects.filter(pk__gt=start_idx - 1)[:elements_per_page]

    length = Article.objects.count()

    next_pg = length

    if start_idx > elements_per_page:
        prev_pg = start_idx - elements_per_page
    else:
        prev_pg = 0

    if start_idx <= length - elements_per_page:
        next_pg = start_idx + elements_per_page

    # articles = Article.objects.all()[start_idx: start_idx + elements_per_page:]
    # print(request.get_full_path())
    # print(request.build_absolute_uri())

    if Article.objects.get(pk=1) != articles[0]:
        prev_pg_url = request.build_absolute_uri(f"/api/v1/custom_cursor_pagination/?start={prev_pg}")
    else:
        prev_pg_url = None

    if next_pg < length:
        next_pg_url = request.build_absolute_uri(f"/api/v1/custom_cursor_pagination/?start={next_pg}")
    else:
        next_pg_url = None

    counter = len(articles)

    return Response({
        "counter_objects_on_page": counter,
        "prev_page": prev_pg_url,
        "next_page": next_pg_url,
        "elements": ArticleSerializer(articles, many=True).data,
    })

