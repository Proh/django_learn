from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Article,Category
from blog.serializers import ArticleSerializer,CategorySerializer
# Create your views here.

@api_view(['GET'])
def get_articles(request):
    aq = Article.objects.all()
    ser_aq = ArticleSerializer(aq, many = True)
    return Response(ser_aq.data)

@api_view(['POST'])
def change_article(request, pk):
    article = Article.objects.get(pk = pk)
    article.title = article.title + '_foo'
    article.save()
    ser= ArticleSerializer(article)
    return Response(ser.data)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()