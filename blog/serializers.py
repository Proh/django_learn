from rest_framework import serializers
from blog.models import Article,Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    cat = CategorySerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'