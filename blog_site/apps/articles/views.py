from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Article, Category
from .serializers import ArticleSerializer, ArticleTestSerializer
from rest_framework.views import APIView


class ArticleAPIView(generics.ListAPIView):
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

