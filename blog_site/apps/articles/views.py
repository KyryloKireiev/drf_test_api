from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Article, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import ArticleSerializer, ArticleTestSerializer
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


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


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )


class ArticleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )
